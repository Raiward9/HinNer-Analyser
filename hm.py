from __future__ import annotations
from dataclasses import dataclass
import streamlit as st
from graphviz import Graph

from antlr4 import *
from hmLexer import hmLexer
from hmParser import hmParser   
from hmVisitor import hmVisitor
from pickle import dumps, loads
import pandas as pd
import copy

# utilitzar st.session_state
# per poder guardar, caldra serialitzar els valors
# usar llibreria pickle de python
# aquesta llibreria te dumps -> guardar, loads -> recuperar
# abans de que s'acabi el codi, fer un dumps, i abans de fer el parser, fer un loads

class Buit:
    pass

@dataclass
class Node:
    simbol: str
    children: list
    tipus: Arbre

Arbre = Node | Buit

class TreeVisitor(hmVisitor):
    def __init__(self, taulaSimbols):
        self.taulaSimbols = [copy.deepcopy(taulaSimbols)]
        self.taulaSimbolsDefinicions = taulaSimbols
        self.simbolLliure = 'a'

    def getSimbolLliure(self):
        lletraActual = self.simbolLliure
        self.simbolLliure = chr(ord(self.simbolLliure) + 1)
        return lletraActual
    
    def buscaTaulaSimbols(self, simbol):
        for taulaSimbol in self.taulaSimbols:
                if simbol in taulaSimbol:
                    return Node(simbol, [], taulaSimbol[simbol])
        
        tipus = self.getSimbolLliure()
        self.taulaSimbols[0][simbol] = tipus
        return Node(simbol, [], Node(tipus, [], Buit)) 

    def visitRoot(self, ctx:hmParser.RootContext):
        exprs = list(ctx.getChildren())
        res = []
        for expr in exprs:
            resExpr = self.visit(expr)
            if resExpr != None:
                res.append(resExpr)
        return res
    
    def visitExprStmt(self, ctx: hmParser.ExprStmtContext):
        [expr] = list(ctx.getChildren())
        return self.visit(expr)
    
    def visitDefinicioStmt(self, ctx: hmParser.DefinicioStmtContext):
        [definicio] = list(ctx.getChildren())
        return self.visit(definicio)
    
    def visitDefinicio(self, ctx: hmParser.DefinicioStmtContext):
        [expr, _, _, tipus] = list(ctx.getChildren())
        arbreTipus = self.visit(tipus)
        nomExpr = str(expr.getText())
        self.taulaSimbols[-1][nomExpr] = arbreTipus
        self.taulaSimbolsDefinicions[nomExpr] = arbreTipus
        return None
    
    def visitTipusSimple(self, ctx: hmParser.TipusSimpleContext):
        [tipus] = list(ctx.getChildren())
        tipus = str(ctx.getText())
        return Node(tipus, [], Buit)
    
    def visitTipusAssociatiu(self, ctx: hmParser.TipusAssociatiuContext):
        [tipus1, arrow, tipus2] = list(ctx.getChildren())
        arbreTipus1 = self.visit(tipus1)
        arbreTipus2 = self.visit(tipus2)
        return Node('->', [arbreTipus1, arbreTipus2],  Buit)
    
    def visitTipusParentesis(self, ctx: hmParser.TipusParentesisContext):
        [lpar, tipus, rpar] = list(ctx.getChildren())
        arbreTipus = self.visit(tipus)
        return Node('()', [arbreTipus], Buit)

    def visitParentesis(self, ctx: hmParser.ParentesisContext):
        [_, expr, _] = list(ctx.getChildren())
        return self.visit(expr)
    
    def visitAplicacioExpr(self, ctx: hmParser.AplicacioExprContext):
        [expr1, expr2] = list(ctx.getChildren())
        simbol = self.getSimbolLliure()

        arbreExpr1 = self.visit(expr1)
        arbreExpr2 = self.visit(expr2)

        return Node('@', [arbreExpr1, arbreExpr2], Node(simbol, [], Buit))

    def visitAbstraccioExpr(self, ctx: hmParser.AbstraccioExprContext):
        [expr] = list(ctx.getChildren())
        return self.visit(expr)
    
    def visitNumero(self, ctx: hmParser.NumeroContext):
        numero = str(ctx.getText())
        return self.buscaTaulaSimbols(numero)
    
    def visitIdent(self, ctx: hmParser.IdentContext):
        identificador = str(ctx.getText())
        return self.buscaTaulaSimbols(identificador)
    
    def visitFuncioAnonima(self, ctx: hmParser.FuncioAnonimaContext):
        [_, ident, _, expr] = list(ctx.getChildren())

        simbol = self.getSimbolLliure()
        simbolActual = self.simbolLliure

        self.taulaSimbols.append({})
        
        simbolIdent = self.getSimbolLliure()
        self.taulaSimbols[0][str(ident)] = simbolIdent
        arbreIdent = Node(str(ident), [], Node(simbolIdent, [], Buit))

        arbreExpr = self.visit(expr)
        
        self.taulaSimbols.pop(0)
        self.simbolLliure = simbolActual
            
        return Node('λ', [arbreIdent, arbreExpr], Node(simbol, [], Buit)) 

    def visitOperadorInfix(self, ctx: hmParser.OperadorInfixContext):
        operador = str(ctx.getText())
        return self.buscaTaulaSimbols(operador)
    

def generarArbre(root):
    graph = Graph()
    nodes = [["n0",root]]
    numNode = 0

    tipus = passarArbreDeTipusAString(root.tipus)
    graph.node(f"n{numNode}", f"{root.simbol}\n{tipus}")
    numNode += 1
    
    while len(nodes) != 0:
        numNodeParent, node = nodes.pop(0)
        for child in node.children:
            numNodeChild = f"n{numNode}"
            tipus = passarArbreDeTipusAString(child.tipus)
            graph.node(numNodeChild, f"{child.simbol}\n{tipus}")
            nodes.append([numNodeChild, child])
            numNode += 1
            graph.edge(numNodeParent, numNodeChild)

    return graph

def passarArbreDeTipusAString(root):
    res = passarArbreDeTipusAStringRec(root)
    if len(res) > 1:
        return "(" + res + ")"
    else:
        return res

def passarArbreDeTipusAStringRec(root):
    match root:
        case Node('->', [child1, child2], _):
            textChild1 = passarArbreDeTipusAStringRec(child1)
            textChild2 = passarArbreDeTipusAStringRec(child2)
            if len(textChild2) > 1:
                res = textChild1 + " -> " + "(" + textChild2 + ")"
            else:
                res =  textChild1 + " -> " + textChild2
            return res
        
        case Node('()', [child1], _):
            textChild1 = passarArbreDeTipusAStringRec(child1)
            res = "(" + textChild1 + ")"
            return res
        
        case Node(x, [], _):
            return x
        case _:
            return root
        
def createDataTable(taulaSimbols):
    columns = ["Tipus"]
    indexes = []
    data = []
    for key, arbreTipus in taulaSimbols.items():
        tipus = passarArbreDeTipusAString(arbreTipus)
        indexes.append(key)
        data.append(tipus)

    return pd.DataFrame(data=data, index=indexes, columns=columns)


if __name__ == "__main__":
    taulaSimbols = {}
    if 'taulaSimbols' in st.session_state:
        taulaSimbols = st.session_state["taulaSimbols"]
        taulaSimbols = loads(taulaSimbols)

    dataTable = createDataTable(taulaSimbols)
    table = st.table(dataTable)

    visitor = TreeVisitor(taulaSimbols)
    
    input = st.text_area(label='Expressió:')
    button_stream = st.button(label='fer')

    if button_stream:
        input_stream = InputStream(input)
        lexer = hmLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = hmParser(token_stream)
        tree = parser.root()
        
        if parser.getNumberOfSyntaxErrors() == 0:
            arbresSemantic = visitor.visit(tree)
            for arbreSemantic in arbresSemantic:
                
                arbreDOT = generarArbre(arbreSemantic)
                st.graphviz_chart(arbreDOT)
            
            taulaSimbolsDefinicions = visitor.taulaSimbolsDefinicions
            st.session_state["taulaSimbols"] = dumps(taulaSimbolsDefinicions)
            table.dataframe(createDataTable(taulaSimbolsDefinicions), use_container_width=True)
                
        else:
            st.write(str(parser.getNumberOfSyntaxErrors()) +  'errors de sintaxi.')

        #st.write(tree.toStringTree(recog=parser))

