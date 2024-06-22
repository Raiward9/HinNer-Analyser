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
        4,1,10,67,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,
        0,1,0,1,1,1,1,3,1,18,8,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,
        1,3,3,3,31,8,3,1,3,1,3,1,3,5,3,36,8,3,10,3,12,3,39,9,3,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,3,4,49,8,4,1,4,1,4,5,4,53,8,4,10,4,12,4,56,
        9,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,65,8,5,1,5,0,2,6,8,6,0,2,4,6,
        8,10,0,0,68,0,12,1,0,0,0,2,17,1,0,0,0,4,19,1,0,0,0,6,30,1,0,0,0,
        8,48,1,0,0,0,10,64,1,0,0,0,12,13,3,2,1,0,13,14,5,0,0,1,14,1,1,0,
        0,0,15,18,3,8,4,0,16,18,3,4,2,0,17,15,1,0,0,0,17,16,1,0,0,0,18,3,
        1,0,0,0,19,20,3,8,4,0,20,21,5,3,0,0,21,22,5,3,0,0,22,23,3,6,3,0,
        23,5,1,0,0,0,24,25,6,3,-1,0,25,31,5,8,0,0,26,27,5,5,0,0,27,28,3,
        6,3,0,28,29,5,6,0,0,29,31,1,0,0,0,30,24,1,0,0,0,30,26,1,0,0,0,31,
        37,1,0,0,0,32,33,10,2,0,0,33,34,5,1,0,0,34,36,3,6,3,2,35,32,1,0,
        0,0,36,39,1,0,0,0,37,35,1,0,0,0,37,38,1,0,0,0,38,7,1,0,0,0,39,37,
        1,0,0,0,40,41,6,4,-1,0,41,42,5,5,0,0,42,43,3,8,4,0,43,44,5,6,0,0,
        44,49,1,0,0,0,45,49,3,10,5,0,46,49,5,7,0,0,47,49,5,9,0,0,48,40,1,
        0,0,0,48,45,1,0,0,0,48,46,1,0,0,0,48,47,1,0,0,0,49,54,1,0,0,0,50,
        51,10,4,0,0,51,53,3,8,4,5,52,50,1,0,0,0,53,56,1,0,0,0,54,52,1,0,
        0,0,54,55,1,0,0,0,55,9,1,0,0,0,56,54,1,0,0,0,57,58,5,2,0,0,58,59,
        5,9,0,0,59,60,5,1,0,0,60,65,3,8,4,0,61,62,5,5,0,0,62,63,5,4,0,0,
        63,65,5,6,0,0,64,57,1,0,0,0,64,61,1,0,0,0,65,11,1,0,0,0,6,17,30,
        37,48,54,64
    ]

class hmParser ( Parser ):

    grammarFileName = "hm.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'->'", "'\\'", "':'", "'+'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "ARROW", "SLASH", "TWOPOINTS", "SUM", 
                      "LPAR", "RPAR", "NUM", "TYPE", "IDENT", "WS" ]

    RULE_root = 0
    RULE_statement = 1
    RULE_definition = 2
    RULE_type = 3
    RULE_expr = 4
    RULE_abstraction = 5

    ruleNames =  [ "root", "statement", "definition", "type", "expr", "abstraction" ]

    EOF = Token.EOF
    ARROW=1
    SLASH=2
    TWOPOINTS=3
    SUM=4
    LPAR=5
    RPAR=6
    NUM=7
    TYPE=8
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


    class DefinitionStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def definition(self):
            return self.getTypedRuleContext(hmParser.DefinitionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefinitionStmt" ):
                return visitor.visitDefinitionStmt(self)
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
                localctx = hmParser.DefinitionStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                self.definition()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(hmParser.ExprContext,0)


        def TWOPOINTS(self, i:int=None):
            if i is None:
                return self.getTokens(hmParser.TWOPOINTS)
            else:
                return self.getToken(hmParser.TWOPOINTS, i)

        def type_(self):
            return self.getTypedRuleContext(hmParser.TypeContext,0)


        def getRuleIndex(self):
            return hmParser.RULE_definition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefinition" ):
                return visitor.visitDefinition(self)
            else:
                return visitor.visitChildren(self)




    def definition(self):

        localctx = hmParser.DefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_definition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.expr(0)
            self.state = 20
            self.match(hmParser.TWOPOINTS)
            self.state = 21
            self.match(hmParser.TWOPOINTS)
            self.state = 22
            self.type_(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return hmParser.RULE_type

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class TypeParenthesisContext(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAR(self):
            return self.getToken(hmParser.LPAR, 0)
        def type_(self):
            return self.getTypedRuleContext(hmParser.TypeContext,0)

        def RPAR(self):
            return self.getToken(hmParser.RPAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeParenthesis" ):
                return visitor.visitTypeParenthesis(self)
            else:
                return visitor.visitChildren(self)


    class TypeSimpleContext(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TYPE(self):
            return self.getToken(hmParser.TYPE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeSimple" ):
                return visitor.visitTypeSimple(self)
            else:
                return visitor.visitChildren(self)


    class TypeAssociativeContext(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def type_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(hmParser.TypeContext)
            else:
                return self.getTypedRuleContext(hmParser.TypeContext,i)

        def ARROW(self):
            return self.getToken(hmParser.ARROW, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeAssociative" ):
                return visitor.visitTypeAssociative(self)
            else:
                return visitor.visitChildren(self)



    def type_(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = hmParser.TypeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_type, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                localctx = hmParser.TypeSimpleContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 25
                self.match(hmParser.TYPE)
                pass
            elif token in [5]:
                localctx = hmParser.TypeParenthesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 26
                self.match(hmParser.LPAR)
                self.state = 27
                self.type_(0)
                self.state = 28
                self.match(hmParser.RPAR)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 37
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = hmParser.TypeAssociativeContext(self, hmParser.TypeContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_type)
                    self.state = 32
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 33
                    self.match(hmParser.ARROW)
                    self.state = 34
                    self.type_(2) 
                self.state = 39
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

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


    class NumberContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(hmParser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
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


    class AbstractionExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def abstraction(self):
            return self.getTypedRuleContext(hmParser.AbstractionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAbstractionExpr" ):
                return visitor.visitAbstractionExpr(self)
            else:
                return visitor.visitChildren(self)


    class AplicationExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(hmParser.ExprContext)
            else:
                return self.getTypedRuleContext(hmParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAplicationExpr" ):
                return visitor.visitAplicationExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenthesisContext(ExprContext):

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
            if hasattr( visitor, "visitParenthesis" ):
                return visitor.visitParenthesis(self)
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
            self.state = 48
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = hmParser.ParenthesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 41
                self.match(hmParser.LPAR)
                self.state = 42
                self.expr(0)
                self.state = 43
                self.match(hmParser.RPAR)
                pass

            elif la_ == 2:
                localctx = hmParser.AbstractionExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 45
                self.abstraction()
                pass

            elif la_ == 3:
                localctx = hmParser.NumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 46
                self.match(hmParser.NUM)
                pass

            elif la_ == 4:
                localctx = hmParser.IdentContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 47
                self.match(hmParser.IDENT)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 54
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = hmParser.AplicationExprContext(self, hmParser.ExprContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 50
                    if not self.precpred(self._ctx, 4):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                    self.state = 51
                    self.expr(5) 
                self.state = 56
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AbstractionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return hmParser.RULE_abstraction

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AnonymousFunctionContext(AbstractionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.AbstractionContext
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
            if hasattr( visitor, "visitAnonymousFunction" ):
                return visitor.visitAnonymousFunction(self)
            else:
                return visitor.visitChildren(self)


    class InfixOperatorContext(AbstractionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.AbstractionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAR(self):
            return self.getToken(hmParser.LPAR, 0)
        def SUM(self):
            return self.getToken(hmParser.SUM, 0)
        def RPAR(self):
            return self.getToken(hmParser.RPAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInfixOperator" ):
                return visitor.visitInfixOperator(self)
            else:
                return visitor.visitChildren(self)



    def abstraction(self):

        localctx = hmParser.AbstractionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_abstraction)
        try:
            self.state = 64
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                localctx = hmParser.AnonymousFunctionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 57
                self.match(hmParser.SLASH)
                self.state = 58
                self.match(hmParser.IDENT)
                self.state = 59
                self.match(hmParser.ARROW)
                self.state = 60
                self.expr(0)
                pass
            elif token in [5]:
                localctx = hmParser.InfixOperatorContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 61
                self.match(hmParser.LPAR)
                self.state = 62
                self.match(hmParser.SUM)
                self.state = 63
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
        self._predicates[3] = self.type_sempred
        self._predicates[4] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def type_sempred(self, localctx:TypeContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




