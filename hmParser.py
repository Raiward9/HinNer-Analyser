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
        4,1,10,72,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,5,
        0,14,8,0,10,0,12,0,17,9,0,1,0,1,0,1,1,1,1,3,1,23,8,1,1,2,1,2,1,2,
        1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,3,3,36,8,3,1,3,1,3,1,3,5,3,41,8,
        3,10,3,12,3,44,9,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,54,8,4,1,
        4,1,4,5,4,58,8,4,10,4,12,4,61,9,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,
        5,70,8,5,1,5,0,2,6,8,6,0,2,4,6,8,10,0,0,74,0,15,1,0,0,0,2,22,1,0,
        0,0,4,24,1,0,0,0,6,35,1,0,0,0,8,53,1,0,0,0,10,69,1,0,0,0,12,14,3,
        2,1,0,13,12,1,0,0,0,14,17,1,0,0,0,15,13,1,0,0,0,15,16,1,0,0,0,16,
        18,1,0,0,0,17,15,1,0,0,0,18,19,5,0,0,1,19,1,1,0,0,0,20,23,3,8,4,
        0,21,23,3,4,2,0,22,20,1,0,0,0,22,21,1,0,0,0,23,3,1,0,0,0,24,25,3,
        8,4,0,25,26,5,3,0,0,26,27,5,3,0,0,27,28,3,6,3,0,28,5,1,0,0,0,29,
        30,6,3,-1,0,30,36,5,8,0,0,31,32,5,5,0,0,32,33,3,6,3,0,33,34,5,6,
        0,0,34,36,1,0,0,0,35,29,1,0,0,0,35,31,1,0,0,0,36,42,1,0,0,0,37,38,
        10,2,0,0,38,39,5,1,0,0,39,41,3,6,3,2,40,37,1,0,0,0,41,44,1,0,0,0,
        42,40,1,0,0,0,42,43,1,0,0,0,43,7,1,0,0,0,44,42,1,0,0,0,45,46,6,4,
        -1,0,46,47,5,5,0,0,47,48,3,8,4,0,48,49,5,6,0,0,49,54,1,0,0,0,50,
        54,3,10,5,0,51,54,5,7,0,0,52,54,5,9,0,0,53,45,1,0,0,0,53,50,1,0,
        0,0,53,51,1,0,0,0,53,52,1,0,0,0,54,59,1,0,0,0,55,56,10,4,0,0,56,
        58,3,8,4,5,57,55,1,0,0,0,58,61,1,0,0,0,59,57,1,0,0,0,59,60,1,0,0,
        0,60,9,1,0,0,0,61,59,1,0,0,0,62,63,5,2,0,0,63,64,5,9,0,0,64,65,5,
        1,0,0,65,70,3,8,4,0,66,67,5,5,0,0,67,68,5,4,0,0,68,70,5,6,0,0,69,
        62,1,0,0,0,69,66,1,0,0,0,70,11,1,0,0,0,7,15,22,35,42,53,59,69
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

        def EOF(self):
            return self.getToken(hmParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(hmParser.StatementContext)
            else:
                return self.getTypedRuleContext(hmParser.StatementContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 676) != 0):
                self.state = 12
                self.statement()
                self.state = 17
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 18
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
            self.state = 22
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = hmParser.ExprStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = hmParser.DefinicioStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 21
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
            self.state = 24
            self.expr(0)
            self.state = 25
            self.match(hmParser.DOSPUNTS)
            self.state = 26
            self.match(hmParser.DOSPUNTS)
            self.state = 27
            self.tipus(0)
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


        def getRuleIndex(self):
            return hmParser.RULE_tipus

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class TipusAssociatiuContext(TipusContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.TipusContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def tipus(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(hmParser.TipusContext)
            else:
                return self.getTypedRuleContext(hmParser.TipusContext,i)

        def ARROW(self):
            return self.getToken(hmParser.ARROW, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipusAssociatiu" ):
                return visitor.visitTipusAssociatiu(self)
            else:
                return visitor.visitChildren(self)


    class TipusParentesisContext(TipusContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.TipusContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAR(self):
            return self.getToken(hmParser.LPAR, 0)
        def tipus(self):
            return self.getTypedRuleContext(hmParser.TipusContext,0)

        def RPAR(self):
            return self.getToken(hmParser.RPAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipusParentesis" ):
                return visitor.visitTipusParentesis(self)
            else:
                return visitor.visitChildren(self)


    class TipusSimpleContext(TipusContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.TipusContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TIPUS(self):
            return self.getToken(hmParser.TIPUS, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipusSimple" ):
                return visitor.visitTipusSimple(self)
            else:
                return visitor.visitChildren(self)



    def tipus(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = hmParser.TipusContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_tipus, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                localctx = hmParser.TipusSimpleContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 30
                self.match(hmParser.TIPUS)
                pass
            elif token in [5]:
                localctx = hmParser.TipusParentesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 31
                self.match(hmParser.LPAR)
                self.state = 32
                self.tipus(0)
                self.state = 33
                self.match(hmParser.RPAR)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 42
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = hmParser.TipusAssociatiuContext(self, hmParser.TipusContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_tipus)
                    self.state = 37
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 38
                    self.match(hmParser.ARROW)
                    self.state = 39
                    self.tipus(2) 
                self.state = 44
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
            self.state = 53
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = hmParser.ParentesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 46
                self.match(hmParser.LPAR)
                self.state = 47
                self.expr(0)
                self.state = 48
                self.match(hmParser.RPAR)
                pass

            elif la_ == 2:
                localctx = hmParser.AbstraccioExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 50
                self.abstraccio()
                pass

            elif la_ == 3:
                localctx = hmParser.NumeroContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 51
                self.match(hmParser.NUM)
                pass

            elif la_ == 4:
                localctx = hmParser.IdentContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 52
                self.match(hmParser.IDENT)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 59
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = hmParser.AplicacioExprContext(self, hmParser.ExprContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 55
                    if not self.precpred(self._ctx, 4):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                    self.state = 56
                    self.expr(5) 
                self.state = 61
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

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
            self.state = 69
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                localctx = hmParser.FuncioAnonimaContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.match(hmParser.SLASH)
                self.state = 63
                self.match(hmParser.IDENT)
                self.state = 64
                self.match(hmParser.ARROW)
                self.state = 65
                self.expr(0)
                pass
            elif token in [5]:
                localctx = hmParser.OperadorInfixContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 66
                self.match(hmParser.LPAR)
                self.state = 67
                self.match(hmParser.SUMA)
                self.state = 68
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
        self._predicates[3] = self.tipus_sempred
        self._predicates[4] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def tipus_sempred(self, localctx:TipusContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




