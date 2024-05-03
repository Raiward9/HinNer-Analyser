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
        4,1,10,59,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,
        0,1,0,1,1,1,1,3,1,18,8,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,5,3,28,
        8,3,10,3,12,3,31,9,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,41,8,4,
        1,4,1,4,5,4,45,8,4,10,4,12,4,48,9,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        3,5,57,8,5,1,5,0,1,8,6,0,2,4,6,8,10,0,0,59,0,12,1,0,0,0,2,17,1,0,
        0,0,4,19,1,0,0,0,6,24,1,0,0,0,8,40,1,0,0,0,10,56,1,0,0,0,12,13,3,
        2,1,0,13,14,5,0,0,1,14,1,1,0,0,0,15,18,3,8,4,0,16,18,3,4,2,0,17,
        15,1,0,0,0,17,16,1,0,0,0,18,3,1,0,0,0,19,20,3,8,4,0,20,21,5,3,0,
        0,21,22,5,3,0,0,22,23,3,6,3,0,23,5,1,0,0,0,24,29,5,8,0,0,25,26,5,
        1,0,0,26,28,5,8,0,0,27,25,1,0,0,0,28,31,1,0,0,0,29,27,1,0,0,0,29,
        30,1,0,0,0,30,7,1,0,0,0,31,29,1,0,0,0,32,33,6,4,-1,0,33,34,5,5,0,
        0,34,35,3,8,4,0,35,36,5,6,0,0,36,41,1,0,0,0,37,41,3,10,5,0,38,41,
        5,7,0,0,39,41,5,9,0,0,40,32,1,0,0,0,40,37,1,0,0,0,40,38,1,0,0,0,
        40,39,1,0,0,0,41,46,1,0,0,0,42,43,10,4,0,0,43,45,3,8,4,5,44,42,1,
        0,0,0,45,48,1,0,0,0,46,44,1,0,0,0,46,47,1,0,0,0,47,9,1,0,0,0,48,
        46,1,0,0,0,49,50,5,2,0,0,50,51,5,9,0,0,51,52,5,1,0,0,52,57,3,8,4,
        0,53,54,5,5,0,0,54,55,5,4,0,0,55,57,5,6,0,0,56,49,1,0,0,0,56,53,
        1,0,0,0,57,11,1,0,0,0,5,17,29,40,46,56
    ]

class hmParser ( Parser ):

    grammarFileName = "hm.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'->'", "'\\'", "':'", "'+'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "ARROW", "SLASH", "DOSPUNTS", "SUMA", 
                      "LPAR", "RPAR", "NUM", "TIPUS", "IDENT", "WS" ]

    RULE_root = 0
    RULE_statement = 1
    RULE_definicio = 2
    RULE_tipus = 3
    RULE_expr = 4
    RULE_abstraccio = 5

    ruleNames =  [ "root", "statement", "definicio", "tipus", "expr", "abstraccio" ]

    EOF = Token.EOF
    ARROW=1
    SLASH=2
    DOSPUNTS=3
    SUMA=4
    LPAR=5
    RPAR=6
    NUM=7
    TIPUS=8
    IDENT=9
    WS=10

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

        def statement(self):
            return self.getTypedRuleContext(hmParser.StatementContext,0)


        def EOF(self):
            return self.getToken(hmParser.EOF, 0)

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
            self.state = 12
            self.statement()
            self.state = 13
            self.match(hmParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return hmParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ExprStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(hmParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprStmt" ):
                return visitor.visitExprStmt(self)
            else:
                return visitor.visitChildren(self)


    class DefinicioStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def definicio(self):
            return self.getTypedRuleContext(hmParser.DefinicioContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefinicioStmt" ):
                return visitor.visitDefinicioStmt(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = hmParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 17
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                localctx = hmParser.ExprStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 15
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = hmParser.DefinicioStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                self.definicio()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefinicioContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(hmParser.ExprContext,0)


        def DOSPUNTS(self, i:int=None):
            if i is None:
                return self.getTokens(hmParser.DOSPUNTS)
            else:
                return self.getToken(hmParser.DOSPUNTS, i)

        def tipus(self):
            return self.getTypedRuleContext(hmParser.TipusContext,0)


        def getRuleIndex(self):
            return hmParser.RULE_definicio

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefinicio" ):
                return visitor.visitDefinicio(self)
            else:
                return visitor.visitChildren(self)




    def definicio(self):

        localctx = hmParser.DefinicioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_definicio)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.expr(0)
            self.state = 20
            self.match(hmParser.DOSPUNTS)
            self.state = 21
            self.match(hmParser.DOSPUNTS)
            self.state = 22
            self.tipus()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipusContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TIPUS(self, i:int=None):
            if i is None:
                return self.getTokens(hmParser.TIPUS)
            else:
                return self.getToken(hmParser.TIPUS, i)

        def ARROW(self, i:int=None):
            if i is None:
                return self.getTokens(hmParser.ARROW)
            else:
                return self.getToken(hmParser.ARROW, i)

        def getRuleIndex(self):
            return hmParser.RULE_tipus

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipus" ):
                return visitor.visitTipus(self)
            else:
                return visitor.visitChildren(self)




    def tipus(self):

        localctx = hmParser.TipusContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_tipus)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(hmParser.TIPUS)
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 25
                self.match(hmParser.ARROW)
                self.state = 26
                self.match(hmParser.TIPUS)
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = hmParser.ParentesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 33
                self.match(hmParser.LPAR)
                self.state = 34
                self.expr(0)
                self.state = 35
                self.match(hmParser.RPAR)
                pass

            elif la_ == 2:
                localctx = hmParser.AbstraccioExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 37
                self.abstraccio()
                pass

            elif la_ == 3:
                localctx = hmParser.NumeroContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 38
                self.match(hmParser.NUM)
                pass

            elif la_ == 4:
                localctx = hmParser.IdentContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 39
                self.match(hmParser.IDENT)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 46
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = hmParser.AplicacioExprContext(self, hmParser.ExprContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 42
                    if not self.precpred(self._ctx, 4):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                    self.state = 43
                    self.expr(5) 
                self.state = 48
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

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
        self.enterRule(localctx, 10, self.RULE_abstraccio)
        try:
            self.state = 56
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                localctx = hmParser.FuncioAnonimaContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                self.match(hmParser.SLASH)
                self.state = 50
                self.match(hmParser.IDENT)
                self.state = 51
                self.match(hmParser.ARROW)
                self.state = 52
                self.expr(0)
                pass
            elif token in [5]:
                localctx = hmParser.OperadorInfixContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                self.match(hmParser.LPAR)
                self.state = 54
                self.match(hmParser.SUMA)
                self.state = 55
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
        self._predicates[4] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         




