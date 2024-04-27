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
    
    def visitStatement(self, ctx:hmParser.StatementContext):
        return self.visitChildren(ctx)
    
    def visitExpressioStmt(self, ctx:hmParser.ExpressioStmtContext):
        return self.visitChildren(ctx)
    
    def visitFuncioStmt(self, ctx:hmParser.FuncioStmtContext):
        return self.visitChildren(ctx)
    
    def visitFuncio(self, ctx:hmParser.FuncioContext):
        return self.visitChildren(ctx)

    def visitOperador(self, ctx:hmParser.OperadorContext):
        return self.visitChildren(ctx)
    
    def visitParentesis(self, ctx:hmParser.ParentesisContext):
        return self.visitChildren(ctx)
    
    def visitFuncioParametres(self, ctx:hmParser.FuncioParametresContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by hmParser#numero.
    def visitNumero(self, ctx:hmParser.NumeroContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by hmParser#ident.
    def visitIdent(self, ctx:hmParser.IdentContext):
        return self.visitChildren(ctx)



del hmParser