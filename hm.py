import sys
from antlr4 import *
from hmLexer import hmLexer
from exprsParser import exprsParser
from evalVisitor import EvalVisitor

if __name__ == "__main__":
    if len(sys.argv) != 1: 
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = StdinStream()

    lexer = hmLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = exprsParser(token_stream)
    tree = parser.root()

    if parser.getNumberOfSyntaxErrors() == 0:
        visitor = EvalVisitor()
        visitor.visit(tree)
    else:
        print(parser.getNumberOfSyntaxErrors(), 'errors de sintaxi.')
        print(tree.toStringTree(recog=parser))