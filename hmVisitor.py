# Generated from hm.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .hmParser import hmParser
else:
    from hmParser import hmParser

# This class defines a complete generic visitor for a parse tree produced by hmParser.

class hmVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by hmParser#root.
    def visitRoot(self, ctx:hmParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#parentesis.
    def visitParentesis(self, ctx:hmParser.ParentesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#aplicacio.
    def visitAplicacio(self, ctx:hmParser.AplicacioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#funcioExpr.
    def visitFuncioExpr(self, ctx:hmParser.FuncioExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#operadorExpr.
    def visitOperadorExpr(self, ctx:hmParser.OperadorExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#numero.
    def visitNumero(self, ctx:hmParser.NumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#ident.
    def visitIdent(self, ctx:hmParser.IdentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#funcio.
    def visitFuncio(self, ctx:hmParser.FuncioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#operadorInfix.
    def visitOperadorInfix(self, ctx:hmParser.OperadorInfixContext):
        return self.visitChildren(ctx)



del hmParser