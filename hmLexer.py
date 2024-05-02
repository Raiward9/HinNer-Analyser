# Generated from hm.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,8,52,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,1,0,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,4,
        5,30,8,5,11,5,12,5,31,1,6,3,6,35,8,6,1,6,3,6,38,8,6,1,6,5,6,41,8,
        6,10,6,12,6,44,9,6,1,7,4,7,47,8,7,11,7,12,7,48,1,7,1,7,0,0,8,1,1,
        3,2,5,3,7,4,9,5,11,6,13,7,15,8,1,0,3,1,0,48,57,2,0,65,90,97,122,
        3,0,9,10,13,13,32,32,55,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,
        1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,1,17,
        1,0,0,0,3,20,1,0,0,0,5,22,1,0,0,0,7,24,1,0,0,0,9,26,1,0,0,0,11,29,
        1,0,0,0,13,34,1,0,0,0,15,46,1,0,0,0,17,18,5,45,0,0,18,19,5,62,0,
        0,19,2,1,0,0,0,20,21,5,92,0,0,21,4,1,0,0,0,22,23,5,43,0,0,23,6,1,
        0,0,0,24,25,5,40,0,0,25,8,1,0,0,0,26,27,5,41,0,0,27,10,1,0,0,0,28,
        30,7,0,0,0,29,28,1,0,0,0,30,31,1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,
        0,32,12,1,0,0,0,33,35,7,1,0,0,34,33,1,0,0,0,35,42,1,0,0,0,36,38,
        7,1,0,0,37,36,1,0,0,0,38,41,1,0,0,0,39,41,7,0,0,0,40,37,1,0,0,0,
        40,39,1,0,0,0,41,44,1,0,0,0,42,40,1,0,0,0,42,43,1,0,0,0,43,14,1,
        0,0,0,44,42,1,0,0,0,45,47,7,2,0,0,46,45,1,0,0,0,47,48,1,0,0,0,48,
        46,1,0,0,0,48,49,1,0,0,0,49,50,1,0,0,0,50,51,6,7,0,0,51,16,1,0,0,
        0,7,0,31,34,37,40,42,48,1,6,0,0
    ]

class hmLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ARROW = 1
    SLASH = 2
    SUMA = 3
    LPAR = 4
    RPAR = 5
    NUM = 6
    IDENT = 7
    WS = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'->'", "'\\'", "'+'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "ARROW", "SLASH", "SUMA", "LPAR", "RPAR", "NUM", "IDENT", "WS" ]

    ruleNames = [ "ARROW", "SLASH", "SUMA", "LPAR", "RPAR", "NUM", "IDENT", 
                  "WS" ]

    grammarFileName = "hm.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


