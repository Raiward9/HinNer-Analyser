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
        self.simbolLliure = 0

    def getSimbolLliure(self):
        lletraActual = f"t{self.simbolLliure}"
        self.simbolLliure += 1
        return lletraActual
    
    def buscaTaulaSimbols(self, simbol: str) -> Node:
        for taulaSimbol in self.taulaSimbols:
                if simbol in taulaSimbol:
                    return Node(simbol, [], taulaSimbol[simbol])
        
        tipus = self.getSimbolLliure()
        self.taulaSimbols[0][simbol] = Node(tipus, [], Buit)
        return Node(simbol, [], Node(tipus, [], Buit)) 

    def visitRoot(self, ctx:hmParser.RootContext):
        [statement, eof] = list(ctx.getChildren())
        resStatement = self.visit(statement)
        return resStatement
    
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
        return self.visit(tipus)

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
        self.taulaSimbols.insert(0, {})

        simbol = self.getSimbolLliure()
        
        simbolIdent = self.getSimbolLliure()
        self.taulaSimbols[0][str(ident)] = Node(simbolIdent, [], Buit)
        
        arbreIdent = Node(str(ident), [], Node(simbolIdent, [], Buit))
        arbreExpr = self.visit(expr)

        self.taulaSimbols.pop(0)
            
        return Node('λ', [arbreIdent, arbreExpr], Node(simbol, [], Buit)) 

    def visitOperadorInfix(self, ctx: hmParser.OperadorInfixContext):
        operador = str(ctx.getText())
        return self.buscaTaulaSimbols(operador)
    

def generarArbre(root: Node, taulaSimbols: dict) -> Graph:
    graph = Graph()
    nodes = [["n0",root]]
    numNode = 0

    tipus = passarArbreDeTipusAString(root.tipus, taulaSimbols)
    graph.node(f"n{numNode}", f"{root.simbol}\n{tipus}")
    numNode += 1
    
    while len(nodes) != 0:
        numNodeParent, node = nodes.pop(0)
        for child in node.children:
            numNodeChild = f"n{numNode}"
            tipus = passarArbreDeTipusAString(child.tipus, taulaSimbols)
            graph.node(numNodeChild, f"{child.simbol}\n{tipus}")
            nodes.append([numNodeChild, child])
            numNode += 1
            graph.edge(numNodeParent, numNodeChild)

    return graph

def passarArbreDeTipusAString(root: Node, taulaSimbols: dict) -> str:
    match root:
        case Node('->', [child1, child2], _):
            return f"({passarArbreDeTipusAString(child1, taulaSimbols)} -> {passarArbreDeTipusAString(child2, taulaSimbols)})"
        case Node(x, [], _):
            if x in taulaSimbols:
                return passarArbreDeTipusAString(taulaSimbols[x], taulaSimbols)
            
            return x
   

def is_a_term(root: Node) -> bool:
    return root.simbol.isupper()

def is_a_variable(root: Node) -> bool:
    if len(root.simbol) >= 2:
        return root.simbol[0] == "t" and root.simbol[1:].isnumeric()
    else:
        return False 
    
def are_equal(x: Node, y: Node) -> bool:
    if len(x.children) != len(y.children):
        return False
    elif x.children == []:
        return x.simbol == y.simbol
    else:
        return x.simbol == y.simbol and are_equal(x.children[0], y.children[0]) and are_equal(x.children[1], y.children[1])
    
def is_complex_type(root):
    return root.simbol == "->"

def unify(x: Node, y: Node, subst: dict) -> dict:
    if subst is None:
        return None
    elif are_equal(x,y):
        return subst
    elif is_a_variable(x):
        return unify_variable(x, y, subst)
    elif is_a_variable(y):
        return unify_variable(y, x, subst)
    elif is_complex_type(x) and is_complex_type(y):
        for childInd in range(2):
            subst = unify(x.children[childInd], y.children[childInd], subst)
        
        return subst
    else:
        raise TypeError(f"{passarArbreDeTipusAString(x, subst)} vs {passarArbreDeTipusAString(y, subst)}")
    
def unify_variable(v: Node, x: Node, subst: dict) -> dict:
    assert(is_a_variable(v))
    if v.simbol in subst:
        return unify(subst[v.simbol], x, subst)
    elif is_a_variable(x) and x.simbol in subst:
        return unify(v, subst[x.simbol], subst)
    elif occurs_check(v, x, subst):
        raise TypeError(f"{passarArbreDeTipusAString(v, {})} vs {passarArbreDeTipusAString(x, {})}")
    else:
        return {**subst, v.simbol: x}

def occurs_check(v: Node, term: Node, subst: dict) -> bool:
    assert(is_a_variable(v))
    if are_equal(v, term):
        return True
    elif is_a_variable(term) and term.simbol in subst:
        return occurs_check(v, subst[term.simbol], subst)
    elif is_complex_type(term):
        return any(occurs_check(v, child, subst) for child in term.children)
    else:
        return False

def inferirTipus(root, taulaSimbolsInferida):
    children = root.children
    if children != []:
        match root:
            case Node('@', [child1, child2], _):
                tipusRealChild1 = child1.tipus
                tipusInferitChild1 = Node("->", [child2.tipus, root.tipus], Buit)

                taulaSimbolsInferida = unify(tipusRealChild1, tipusInferitChild1, taulaSimbolsInferida)

                taulaSimbolsInferida = inferirTipus(child1, taulaSimbolsInferida)
                taulaSimbolsInferida = inferirTipus(child2, taulaSimbolsInferida)

            case Node('λ', [child1, child2], _):
                tipusRealRoot = root.tipus
                tipusInferitRoot = Node("->", [child1.tipus, child2.tipus], Buit)

                taulaSimbolsInferida = unify(tipusRealRoot, tipusInferitRoot, taulaSimbolsInferida)

                taulaSimbolsInferida = inferirTipus(child1, taulaSimbolsInferida)
                taulaSimbolsInferida = inferirTipus(child2, taulaSimbolsInferida)

    return taulaSimbolsInferida

def createDataTable(taulaSimbols):
    columns = ["Tipus"]
    indexes = []
    data = []
    for key, arbreTipus in taulaSimbols.items():
        tipus = passarArbreDeTipusAString(arbreTipus, taulaSimbols)
        indexes.append(key)
        data.append(tipus)

    return pd.DataFrame(data=data, index=indexes, columns=columns)

def executeAnalizer(statement: str):

    input_stream = InputStream(statement)
    lexer = hmLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = hmParser(token_stream)
    tree = parser.root()
    
    if parser.getNumberOfSyntaxErrors() == 0:
        arbreSemantic = visitor.visit(tree)
        if arbreSemantic is None:
            return
        
        arbreDOT = generarArbre(arbreSemantic, {})
        st.graphviz_chart(arbreDOT)

        taulaSimbolsInferida = {}
        try:
            taulaSimbolsInferida = inferirTipus(arbreSemantic, taulaSimbolsInferida)

            arbreDOT = generarArbre(arbreSemantic, taulaSimbolsInferida)
            st.graphviz_chart(arbreDOT)

            dataTable2 = createDataTable(taulaSimbolsInferida)
            st.table(dataTable2)

        except TypeError as error:
            errorMsg = "TypeError: " + str(error)
            st.write(errorMsg)
            
        taulaSimbolsDefinicions = visitor.taulaSimbolsDefinicions
        st.session_state["taulaSimbols"] = dumps(taulaSimbolsDefinicions)
        table.dataframe(createDataTable(taulaSimbolsDefinicions), use_container_width=True)
            
    else:
        st.write(str(parser.getNumberOfSyntaxErrors()) +  'errors de sintaxi.')

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
        statements = input.split("\n")
        
        for statement in input.split("\n"):
            executeAnalizer(statement)



