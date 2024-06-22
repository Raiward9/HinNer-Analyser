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


    # Visit a parse tree produced by hmParser#definitionStmt.
    def visitDefinitionStmt(self, ctx:hmParser.DefinitionStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#definition.
    def visitDefinition(self, ctx:hmParser.DefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#typeParenthesis.
    def visitTypeParenthesis(self, ctx:hmParser.TypeParenthesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#typeSimple.
    def visitTypeSimple(self, ctx:hmParser.TypeSimpleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#typeAssociative.
    def visitTypeAssociative(self, ctx:hmParser.TypeAssociativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#number.
    def visitNumber(self, ctx:hmParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#ident.
    def visitIdent(self, ctx:hmParser.IdentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#abstractionExpr.
    def visitAbstractionExpr(self, ctx:hmParser.AbstractionExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#aplicationExpr.
    def visitAplicationExpr(self, ctx:hmParser.AplicationExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#parenthesis.
    def visitParenthesis(self, ctx:hmParser.ParenthesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#anonymousFunction.
    def visitAnonymousFunction(self, ctx:hmParser.AnonymousFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#infixOperator.
    def visitInfixOperator(self, ctx:hmParser.InfixOperatorContext):
        return self.visitChildren(ctx)



del hmParser