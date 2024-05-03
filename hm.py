from __future__ import annotations
from dataclasses import dataclass
import streamlit as st
from graphviz import Graph

from antlr4 import *
from hmLexer import hmLexer
from hmParser import hmParser   
from hmVisitor import hmVisitor

@dataclass
class Node:
    simbol: str
    children: list

class TreeVisitor(hmVisitor):
    def __init__(self):
        self.symbolsTable = {}
        print("Crida innit")

    def visitRoot(self, ctx:hmParser.RootContext):
        [expr1, _] = list(ctx.getChildren())
        return self.visit(expr1)
    
    def visitExprStmt(self, ctx: hmParser.ExprStmtContext):
        [expr] = list(ctx.getChildren())
        return self.visit(expr)
    
    def visitDefinicioStmt(self, ctx: hmParser.DefinicioStmtContext):
        [definicio] = list(ctx.getChildren())
        return self.visit(definicio)
    
    def visitDefinicio(self, ctx: hmParser.DefinicioStmtContext):
        [expr, _, _, tipus] = list(ctx.getChildren())
        self.symbolsTable[str(expr.getText())] = str(tipus.getText())
        print(self.symbolsTable)
        return None
    
    def visitParentesis(self, ctx: hmParser.ParentesisContext):
        [_, expr, _] = list(ctx.getChildren())
        return self.visit(expr)
    
    def visitAplicacioExpr(self, ctx: hmParser.AplicacioExprContext):
        [expr1, expr2] = list(ctx.getChildren())
        arbreExpr1 = self.visit(expr1)
        arbreExpr2 = self.visit(expr2)
        return Node('@', [arbreExpr1, arbreExpr2])

    def visitAbstraccioExpr(self, ctx: hmParser.AbstraccioExprContext):
        [expr] = list(ctx.getChildren())
        return self.visit(expr)
    
    def visitNumero(self, ctx: hmParser.NumeroContext):
        [numero] = list(ctx.getChildren())
        numero = str(ctx.getText())
        return Node(numero, [])
    
    def visitIdent(self, ctx: hmParser.IdentContext):
        [identificador] = list(ctx.getChildren())
        identificador = str(ctx.getText())
        return Node(identificador, [])
    
    def visitFuncioAnonima(self, ctx: hmParser.FuncioAnonimaContext):
        [_, ident, _, expr] = list(ctx.getChildren())
        arbreIdent = Node(str(ident), [])
        arbreExpr = self.visit(expr)
        return Node('λ', [arbreIdent, arbreExpr]) 

    def visitOperadorInfix(self, ctx: hmParser.OperadorInfixContext):
        return Node('(+)', [])
    

def generarArbre(root):
    graph = Graph()
    nodes = [["n0",root]]
    numNode = 0

    graph.node(f"n{numNode}", root.simbol)
    numNode += 1
    
    while len(nodes) != 0:
        numNodeParent, node = nodes.pop(0)
        for child in node.children:
            numNodeChild = f"n{numNode}"
            graph.node(numNodeChild, child.simbol)
            nodes.append([numNodeChild, child])
            numNode += 1
            graph.edge(numNodeParent, numNodeChild)

    return graph

@st.cache_resource
def initialize_tree_visitor():
    return TreeVisitor()

if __name__ == "__main__":
    visitor = initialize_tree_visitor()


    input = st.text_input(label='Expressió:')
    button_stream = st.button(label='fer')

    if button_stream:
        input_stream = InputStream(input)
        lexer = hmLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = hmParser(token_stream)
        tree = parser.root()
        
        if parser.getNumberOfSyntaxErrors() == 0:
            arbreSematic = visitor.visit(tree)

            if arbreSematic != None:
                arbreDOT = generarArbre(arbreSematic)
                st.graphviz_chart(arbreDOT)

        else:
            st.write(str(parser.getNumberOfSyntaxErrors()) +  'errors de sintaxi.')

        #st.write(tree.toStringTree(recog=parser))

