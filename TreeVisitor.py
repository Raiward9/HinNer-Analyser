from __future__ import annotations
from dataclasses import dataclass

from hmParser import hmParser
from hmVisitor import hmVisitor

@dataclass
class Node:
    simbol: str
    child: list

class TreeVisitor(hmVisitor):
    def visitRoot(self, ctx:hmParser.RootContext):
        [expr1, _] = list(ctx.getChildren())
        return self.visit(expr1)
    
    def visitParentesis(self, ctx: hmParser.ParentesisContext):
        [expr] = list(ctx.getChildren())
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