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


    # Visit a parse tree produced by hmParser#exprStmt.
    def visitExprStmt(self, ctx:hmParser.ExprStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#definicioStmt.
    def visitDefinicioStmt(self, ctx:hmParser.DefinicioStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#definicio.
    def visitDefinicio(self, ctx:hmParser.DefinicioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#tipusAssociatiu.
    def visitTipusAssociatiu(self, ctx:hmParser.TipusAssociatiuContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#tipusParentesis.
    def visitTipusParentesis(self, ctx:hmParser.TipusParentesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#tipusSimple.
    def visitTipusSimple(self, ctx:hmParser.TipusSimpleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#parentesis.
    def visitParentesis(self, ctx:hmParser.ParentesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#aplicacioExpr.
    def visitAplicacioExpr(self, ctx:hmParser.AplicacioExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#numero.
    def visitNumero(self, ctx:hmParser.NumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#abstraccioExpr.
    def visitAbstraccioExpr(self, ctx:hmParser.AbstraccioExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#ident.
    def visitIdent(self, ctx:hmParser.IdentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#funcioAnonima.
    def visitFuncioAnonima(self, ctx:hmParser.FuncioAnonimaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#operadorInfix.
    def visitOperadorInfix(self, ctx:hmParser.OperadorInfixContext):
        return self.visitChildren(ctx)



del hmParser