from hmParser import hmParser
from hmVisitor import hmVisitor
from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Node:
    simbol: str
    child: list

class TreeVisitor(hmVisitor):
    def visitFuncioAnonima(self, ctx: hmParser.FuncioAnonimaContext):
        [slash, ident, arrow, expr] = list(ctx.getChildren())
        fillEsquerre = self.visit(ident)
        fillDret = self.visit(expr)
        return Node('λ', [fillEsquerre, fillDret]) 

    def visitOperadorInfix(self, ctx: hmParser.OperadorInfixContext):
        return Node('(+)', [])
    
    def visitNumero(self, ctx: hmParser.NumeroContext):
        numero = str(ctx.getText())
        return Node(numero, [])
    
    def visitIdent(self, ctx: hmParser.IdentContext):
        identificador = str(ctx.getText())
        return Node(identificador, [])