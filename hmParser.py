# Generated from hm.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,8,43,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,3,1,20,8,1,1,1,5,1,23,8,1,10,1,12,1,26,9,1,1,
        1,1,1,1,1,1,1,3,1,32,8,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,
        0,0,4,0,2,4,6,0,0,45,0,8,1,0,0,0,2,31,1,0,0,0,4,33,1,0,0,0,6,38,
        1,0,0,0,8,9,3,2,1,0,9,1,1,0,0,0,10,11,5,4,0,0,11,12,3,2,1,0,12,13,
        5,5,0,0,13,32,1,0,0,0,14,15,5,4,0,0,15,16,3,4,2,0,16,17,5,5,0,0,
        17,20,1,0,0,0,18,20,3,6,3,0,19,14,1,0,0,0,19,18,1,0,0,0,20,24,1,
        0,0,0,21,23,3,2,1,0,22,21,1,0,0,0,23,26,1,0,0,0,24,22,1,0,0,0,24,
        25,1,0,0,0,25,32,1,0,0,0,26,24,1,0,0,0,27,32,3,4,2,0,28,32,3,6,3,
        0,29,32,5,6,0,0,30,32,5,7,0,0,31,10,1,0,0,0,31,19,1,0,0,0,31,27,
        1,0,0,0,31,28,1,0,0,0,31,29,1,0,0,0,31,30,1,0,0,0,32,3,1,0,0,0,33,
        34,5,2,0,0,34,35,5,7,0,0,35,36,5,1,0,0,36,37,3,2,1,0,37,5,1,0,0,
        0,38,39,5,4,0,0,39,40,5,3,0,0,40,41,5,5,0,0,41,7,1,0,0,0,3,19,24,
        31
    ]

class hmParser ( Parser ):

    grammarFileName = "hm.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'->'", "'\\'", "'+'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "ARROW", "SLASH", "SUMA", "LPAR", "RPAR", 
                      "NUM", "IDENT", "WS" ]

    RULE_root = 0
    RULE_expr = 1
    RULE_funcio = 2
    RULE_operadorInfix = 3

    ruleNames =  [ "root", "expr", "funcio", "operadorInfix" ]

    EOF = Token.EOF
    ARROW=1
    SLASH=2
    SUMA=3
    LPAR=4
    RPAR=5
    NUM=6
    IDENT=7
    WS=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(hmParser.ExprContext,0)


        def getRuleIndex(self):
            return hmParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = hmParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return hmParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ParentesisContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAR(self):
            return self.getToken(hmParser.LPAR, 0)
        def expr(self):
            return self.getTypedRuleContext(hmParser.ExprContext,0)

        def RPAR(self):
            return self.getToken(hmParser.RPAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParentesis" ):
                return visitor.visitParentesis(self)
            else:
                return visitor.visitChildren(self)


    class FuncioExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def funcio(self):
            return self.getTypedRuleContext(hmParser.FuncioContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncioExpr" ):
                return visitor.visitFuncioExpr(self)
            else:
                return visitor.visitChildren(self)


    class OperadorExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def operadorInfix(self):
            return self.getTypedRuleContext(hmParser.OperadorInfixContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperadorExpr" ):
                return visitor.visitOperadorExpr(self)
            else:
                return visitor.visitChildren(self)


    class NumeroContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(hmParser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumero" ):
                return visitor.visitNumero(self)
            else:
                return visitor.visitChildren(self)


    class IdentContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENT(self):
            return self.getToken(hmParser.IDENT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdent" ):
                return visitor.visitIdent(self)
            else:
                return visitor.visitChildren(self)


    class AplicacioContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAR(self):
            return self.getToken(hmParser.LPAR, 0)
        def funcio(self):
            return self.getTypedRuleContext(hmParser.FuncioContext,0)

        def RPAR(self):
            return self.getToken(hmParser.RPAR, 0)
        def operadorInfix(self):
            return self.getTypedRuleContext(hmParser.OperadorInfixContext,0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(hmParser.ExprContext)
            else:
                return self.getTypedRuleContext(hmParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAplicacio" ):
                return visitor.visitAplicacio(self)
            else:
                return visitor.visitChildren(self)



    def expr(self):

        localctx = hmParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.state = 31
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = hmParser.ParentesisContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 10
                self.match(hmParser.LPAR)
                self.state = 11
                self.expr()
                self.state = 12
                self.match(hmParser.RPAR)
                pass

            elif la_ == 2:
                localctx = hmParser.AplicacioContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 19
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 14
                    self.match(hmParser.LPAR)
                    self.state = 15
                    self.funcio()
                    self.state = 16
                    self.match(hmParser.RPAR)
                    pass

                elif la_ == 2:
                    self.state = 18
                    self.operadorInfix()
                    pass


                self.state = 24
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 21
                        self.expr() 
                    self.state = 26
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

                pass

            elif la_ == 3:
                localctx = hmParser.FuncioExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 27
                self.funcio()
                pass

            elif la_ == 4:
                localctx = hmParser.OperadorExprContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 28
                self.operadorInfix()
                pass

            elif la_ == 5:
                localctx = hmParser.NumeroContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 29
                self.match(hmParser.NUM)
                pass

            elif la_ == 6:
                localctx = hmParser.IdentContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 30
                self.match(hmParser.IDENT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncioContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SLASH(self):
            return self.getToken(hmParser.SLASH, 0)

        def IDENT(self):
            return self.getToken(hmParser.IDENT, 0)

        def ARROW(self):
            return self.getToken(hmParser.ARROW, 0)

        def expr(self):
            return self.getTypedRuleContext(hmParser.ExprContext,0)


        def getRuleIndex(self):
            return hmParser.RULE_funcio

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncio" ):
                return visitor.visitFuncio(self)
            else:
                return visitor.visitChildren(self)




    def funcio(self):

        localctx = hmParser.FuncioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_funcio)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(hmParser.SLASH)
            self.state = 34
            self.match(hmParser.IDENT)
            self.state = 35
            self.match(hmParser.ARROW)
            self.state = 36
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperadorInfixContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAR(self):
            return self.getToken(hmParser.LPAR, 0)

        def SUMA(self):
            return self.getToken(hmParser.SUMA, 0)

        def RPAR(self):
            return self.getToken(hmParser.RPAR, 0)

        def getRuleIndex(self):
            return hmParser.RULE_operadorInfix

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperadorInfix" ):
                return visitor.visitOperadorInfix(self)
            else:
                return visitor.visitChildren(self)




    def operadorInfix(self):

        localctx = hmParser.OperadorInfixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_operadorInfix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(hmParser.LPAR)
            self.state = 39
            self.match(hmParser.SUMA)
            self.state = 40
            self.match(hmParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





