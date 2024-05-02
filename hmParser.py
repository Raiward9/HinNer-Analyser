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
        4,1,8,35,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,3,1,17,8,1,1,1,1,1,5,1,21,8,1,10,1,12,1,24,9,1,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,3,2,33,8,2,1,2,0,1,2,3,0,2,4,0,0,36,0,6,1,0,0,
        0,2,16,1,0,0,0,4,32,1,0,0,0,6,7,3,2,1,0,7,1,1,0,0,0,8,9,6,1,-1,0,
        9,10,5,4,0,0,10,11,3,2,1,0,11,12,5,5,0,0,12,17,1,0,0,0,13,17,3,4,
        2,0,14,17,5,6,0,0,15,17,5,7,0,0,16,8,1,0,0,0,16,13,1,0,0,0,16,14,
        1,0,0,0,16,15,1,0,0,0,17,22,1,0,0,0,18,19,10,4,0,0,19,21,3,2,1,5,
        20,18,1,0,0,0,21,24,1,0,0,0,22,20,1,0,0,0,22,23,1,0,0,0,23,3,1,0,
        0,0,24,22,1,0,0,0,25,26,5,2,0,0,26,27,5,7,0,0,27,28,5,1,0,0,28,33,
        3,2,1,0,29,30,5,4,0,0,30,31,5,3,0,0,31,33,5,5,0,0,32,25,1,0,0,0,
        32,29,1,0,0,0,33,5,1,0,0,0,3,16,22,32
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
    RULE_abstraccio = 2

    ruleNames =  [ "root", "expr", "abstraccio" ]

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
            self.state = 6
            self.expr(0)
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


    class AplicacioExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(hmParser.ExprContext)
            else:
                return self.getTypedRuleContext(hmParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAplicacioExpr" ):
                return visitor.visitAplicacioExpr(self)
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


    class AbstraccioExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def abstraccio(self):
            return self.getTypedRuleContext(hmParser.AbstraccioContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAbstraccioExpr" ):
                return visitor.visitAbstraccioExpr(self)
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



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = hmParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                localctx = hmParser.ParentesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 9
                self.match(hmParser.LPAR)
                self.state = 10
                self.expr(0)
                self.state = 11
                self.match(hmParser.RPAR)
                pass

            elif la_ == 2:
                localctx = hmParser.AbstraccioExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 13
                self.abstraccio()
                pass

            elif la_ == 3:
                localctx = hmParser.NumeroContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 14
                self.match(hmParser.NUM)
                pass

            elif la_ == 4:
                localctx = hmParser.IdentContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 15
                self.match(hmParser.IDENT)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 22
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = hmParser.AplicacioExprContext(self, hmParser.ExprContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 18
                    if not self.precpred(self._ctx, 4):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                    self.state = 19
                    self.expr(5) 
                self.state = 24
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AbstraccioContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return hmParser.RULE_abstraccio

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class OperadorInfixContext(AbstraccioContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.AbstraccioContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAR(self):
            return self.getToken(hmParser.LPAR, 0)
        def SUMA(self):
            return self.getToken(hmParser.SUMA, 0)
        def RPAR(self):
            return self.getToken(hmParser.RPAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperadorInfix" ):
                return visitor.visitOperadorInfix(self)
            else:
                return visitor.visitChildren(self)


    class FuncioAnonimaContext(AbstraccioContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.AbstraccioContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SLASH(self):
            return self.getToken(hmParser.SLASH, 0)
        def IDENT(self):
            return self.getToken(hmParser.IDENT, 0)
        def ARROW(self):
            return self.getToken(hmParser.ARROW, 0)
        def expr(self):
            return self.getTypedRuleContext(hmParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncioAnonima" ):
                return visitor.visitFuncioAnonima(self)
            else:
                return visitor.visitChildren(self)



    def abstraccio(self):

        localctx = hmParser.AbstraccioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_abstraccio)
        try:
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                localctx = hmParser.FuncioAnonimaContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.match(hmParser.SLASH)
                self.state = 26
                self.match(hmParser.IDENT)
                self.state = 27
                self.match(hmParser.ARROW)
                self.state = 28
                self.expr(0)
                pass
            elif token in [4]:
                localctx = hmParser.OperadorInfixContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.match(hmParser.LPAR)
                self.state = 30
                self.match(hmParser.SUMA)
                self.state = 31
                self.match(hmParser.RPAR)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         




