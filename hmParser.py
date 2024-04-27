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
        4,1,8,49,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,5,0,10,8,0,10,0,12,
        0,13,9,0,1,1,1,1,3,1,17,8,1,1,2,1,2,1,2,1,2,4,2,23,8,2,11,2,12,2,
        24,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,35,8,2,10,2,12,2,38,9,2,1,
        2,1,2,3,2,42,8,2,1,3,1,3,1,3,1,3,1,3,1,3,0,0,4,0,2,4,6,0,1,1,0,6,
        7,52,0,11,1,0,0,0,2,16,1,0,0,0,4,41,1,0,0,0,6,43,1,0,0,0,8,10,3,
        2,1,0,9,8,1,0,0,0,10,13,1,0,0,0,11,9,1,0,0,0,11,12,1,0,0,0,12,1,
        1,0,0,0,13,11,1,0,0,0,14,17,3,4,2,0,15,17,3,6,3,0,16,14,1,0,0,0,
        16,15,1,0,0,0,17,3,1,0,0,0,18,19,5,4,0,0,19,20,5,3,0,0,20,22,5,5,
        0,0,21,23,7,0,0,0,22,21,1,0,0,0,23,24,1,0,0,0,24,22,1,0,0,0,24,25,
        1,0,0,0,25,42,1,0,0,0,26,27,5,4,0,0,27,28,3,4,2,0,28,29,5,5,0,0,
        29,42,1,0,0,0,30,31,5,4,0,0,31,32,3,6,3,0,32,36,5,5,0,0,33,35,7,
        0,0,0,34,33,1,0,0,0,35,38,1,0,0,0,36,34,1,0,0,0,36,37,1,0,0,0,37,
        42,1,0,0,0,38,36,1,0,0,0,39,42,5,6,0,0,40,42,5,7,0,0,41,18,1,0,0,
        0,41,26,1,0,0,0,41,30,1,0,0,0,41,39,1,0,0,0,41,40,1,0,0,0,42,5,1,
        0,0,0,43,44,5,2,0,0,44,45,5,7,0,0,45,46,5,1,0,0,46,47,3,4,2,0,47,
        7,1,0,0,0,5,11,16,24,36,41
    ]

class hmParser ( Parser ):

    grammarFileName = "hm.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'->'", "'\\'", "<INVALID>", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "ARROW", "SLASH", "OPERADOR", "LPAR", 
                      "RPAR", "NUM", "IDENT", "WS" ]

    RULE_root = 0
    RULE_statement = 1
    RULE_expr = 2
    RULE_funcio = 3

    ruleNames =  [ "root", "statement", "expr", "funcio" ]

    EOF = Token.EOF
    ARROW=1
    SLASH=2
    OPERADOR=3
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

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(hmParser.StatementContext)
            else:
                return self.getTypedRuleContext(hmParser.StatementContext,i)


        def getRuleIndex(self):
            return hmParser.RULE_root




    def root(self):

        localctx = hmParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 212) != 0):
                self.state = 8
                self.statement()
                self.state = 13
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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



    class ExpressioStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(hmParser.ExprContext,0)



    class FuncioStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def funcio(self):
            return self.getTypedRuleContext(hmParser.FuncioContext,0)




    def statement(self):

        localctx = hmParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 16
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 6, 7]:
                localctx = hmParser.ExpressioStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 14
                self.expr()
                pass
            elif token in [2]:
                localctx = hmParser.FuncioStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 15
                self.funcio()
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


    class FuncioParametresContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAR(self):
            return self.getToken(hmParser.LPAR, 0)
        def funcio(self):
            return self.getTypedRuleContext(hmParser.FuncioContext,0)

        def RPAR(self):
            return self.getToken(hmParser.RPAR, 0)
        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(hmParser.IDENT)
            else:
                return self.getToken(hmParser.IDENT, i)
        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(hmParser.NUM)
            else:
                return self.getToken(hmParser.NUM, i)


    class NumeroContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(hmParser.NUM, 0)


    class IdentContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENT(self):
            return self.getToken(hmParser.IDENT, 0)


    class OperadorContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAR(self):
            return self.getToken(hmParser.LPAR, 0)
        def OPERADOR(self):
            return self.getToken(hmParser.OPERADOR, 0)
        def RPAR(self):
            return self.getToken(hmParser.RPAR, 0)
        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(hmParser.IDENT)
            else:
                return self.getToken(hmParser.IDENT, i)
        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(hmParser.NUM)
            else:
                return self.getToken(hmParser.NUM, i)



    def expr(self):

        localctx = hmParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 41
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = hmParser.OperadorContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 18
                self.match(hmParser.LPAR)
                self.state = 19
                self.match(hmParser.OPERADOR)
                self.state = 20
                self.match(hmParser.RPAR)
                self.state = 22 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 21
                        _la = self._input.LA(1)
                        if not(_la==6 or _la==7):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()

                    else:
                        raise NoViableAltException(self)
                    self.state = 24 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                pass

            elif la_ == 2:
                localctx = hmParser.ParentesisContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.match(hmParser.LPAR)
                self.state = 27
                self.expr()
                self.state = 28
                self.match(hmParser.RPAR)
                pass

            elif la_ == 3:
                localctx = hmParser.FuncioParametresContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 30
                self.match(hmParser.LPAR)
                self.state = 31
                self.funcio()
                self.state = 32
                self.match(hmParser.RPAR)
                self.state = 36
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 33
                        _la = self._input.LA(1)
                        if not(_la==6 or _la==7):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume() 
                    self.state = 38
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

                pass

            elif la_ == 4:
                localctx = hmParser.NumeroContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 39
                self.match(hmParser.NUM)
                pass

            elif la_ == 5:
                localctx = hmParser.IdentContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 40
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




    def funcio(self):

        localctx = hmParser.FuncioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_funcio)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(hmParser.SLASH)
            self.state = 44
            self.match(hmParser.IDENT)
            self.state = 45
            self.match(hmParser.ARROW)
            self.state = 46
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





