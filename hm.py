import streamlit as st
from graphviz import Graph

from antlr4 import *
from hmLexer import hmLexer
from hmParser import hmParser   
from pickle import dumps, loads
import pandas as pd
from treeVisitor import TreeVisitor
from node import Node, Tree, Empty
from inferer import inferType

# genera la instancia de Graph corresponent a l'arbre root,
# fa us d'un diccionari amb type coneguts (symbolsTable)
def generateVisualTree(root: Node, symbolsTable: dict) -> Graph:
    graph = Graph()
    nodes = [["n0",root]]
    numNode = 0

    type = typeTreeToString(root.type, symbolsTable)
    graph.node(f"n{numNode}", f"{root.symbol}\n{type}")
    numNode += 1
    
    while len(nodes) != 0:
        numNodeParent, node = nodes.pop(0)
        for child in node.children:
            numNodeChild = f"n{numNode}"
            type = typeTreeToString(child.type, symbolsTable)
            graph.node(numNodeChild, f"{child.symbol}\n{type}")
            nodes.append([numNodeChild, child])
            numNode += 1
            graph.edge(numNodeParent, numNodeChild)

    return graph

# passa un arbre de type a string, fa us d'un diccionari (symbolsTable)
# amb type sabuts
def typeTreeToString(root: Node, symbolsTable: dict) -> str:
    match root:
        case Node('->', [child1, child2], _):
            return f"({typeTreeToString(child1, symbolsTable)} -> {typeTreeToString(child2, symbolsTable)})"
        case Node(x, [], _):
            if x in symbolsTable:
                return typeTreeToString(symbolsTable[x], symbolsTable)
            
            return x

# crea un dataframe a partir d'un diccionari de type
def createDataTable(symbolsTable: dict) -> pd.DataFrame:
    columns = ["Type"]
    indices = []
    data = []
    for key, typeTree in symbolsTable.items():
        type = typeTreeToString(typeTree, symbolsTable)
        indices.append(key)
        data.append(type)

    return pd.DataFrame(data=data, index=indices, columns=columns)

# Executa tot el proces necessari per avaluar, inferir el type i mostrar un statement
def executeAnalyser(statement: str):

    input_stream = InputStream(statement)
    lexer = hmLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = hmParser(token_stream)
    tree = parser.root()
    
    if parser.getNumberOfSyntaxErrors() == 0:
        semanticTree = visitor.visit(tree)
        if semanticTree is None:
            return
        
        arbreDOT = generateVisualTree(semanticTree, {})
        st.graphviz_chart(arbreDOT)

        inferedSymbolsTable = {}
        try:
            inferedSymbolsTable = inferType(semanticTree, inferedSymbolsTable)

            arbreDOT = generateVisualTree(semanticTree, inferedSymbolsTable)
            st.graphviz_chart(arbreDOT)

            dataTable2 = createDataTable(inferedSymbolsTable)
            st.table(dataTable2)

        except TypeError as error:
            errorMsg = "TypeError: " + str(error)
            st.write(errorMsg)
            
        definitionsSymbolsTable = visitor.definitionsSymbolsTable
        st.session_state["symbolsTable"] = dumps(definitionsSymbolsTable)
        table.dataframe(createDataTable(definitionsSymbolsTable), use_container_width=True)
            
    else:
        st.write(str(parser.getNumberOfSyntaxErrors()) +  'syntaxis errors.')

if __name__ == "__main__":
    symbolsTable = {}
    if 'symbolsTable' in st.session_state:
        symbolsTable = st.session_state["symbolsTable"]
        symbolsTable = loads(symbolsTable)

    dataTable = createDataTable(symbolsTable)
    table = st.table(dataTable)

    visitor = TreeVisitor(symbolsTable)
    
    input = st.text_area(label='Expression:')
    button_stream = st.button(label='do')

    if button_stream:
        statements = input.split("\n")
        
        for statement in input.split("\n"):
            executeAnalyser(statement)



