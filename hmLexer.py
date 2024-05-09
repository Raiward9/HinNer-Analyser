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
        4,0,9,51,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,1,0,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,
        4,1,5,1,5,1,6,4,6,34,8,6,11,6,12,6,35,1,7,1,7,5,7,40,8,7,10,7,12,
        7,43,9,7,1,8,4,8,46,8,8,11,8,12,8,47,1,8,1,8,0,0,9,1,1,3,2,5,3,7,
        4,9,5,11,6,13,7,15,8,17,9,1,0,4,1,0,48,57,2,0,65,90,97,122,3,0,48,
        57,65,90,97,122,3,0,9,10,13,13,32,32,53,0,1,1,0,0,0,0,3,1,0,0,0,
        0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,
        15,1,0,0,0,0,17,1,0,0,0,1,19,1,0,0,0,3,22,1,0,0,0,5,24,1,0,0,0,7,
        26,1,0,0,0,9,28,1,0,0,0,11,30,1,0,0,0,13,33,1,0,0,0,15,37,1,0,0,
        0,17,45,1,0,0,0,19,20,5,45,0,0,20,21,5,62,0,0,21,2,1,0,0,0,22,23,
        5,92,0,0,23,4,1,0,0,0,24,25,5,58,0,0,25,6,1,0,0,0,26,27,5,43,0,0,
        27,8,1,0,0,0,28,29,5,40,0,0,29,10,1,0,0,0,30,31,5,41,0,0,31,12,1,
        0,0,0,32,34,7,0,0,0,33,32,1,0,0,0,34,35,1,0,0,0,35,33,1,0,0,0,35,
        36,1,0,0,0,36,14,1,0,0,0,37,41,7,1,0,0,38,40,7,2,0,0,39,38,1,0,0,
        0,40,43,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,16,1,0,0,0,43,41,
        1,0,0,0,44,46,7,3,0,0,45,44,1,0,0,0,46,47,1,0,0,0,47,45,1,0,0,0,
        47,48,1,0,0,0,48,49,1,0,0,0,49,50,6,8,0,0,50,18,1,0,0,0,4,0,35,41,
        47,1,6,0,0
    ]

class hmLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ARROW = 1
    SLASH = 2
    DOSPUNTS = 3
    SUMA = 4
    LPAR = 5
    RPAR = 6
    NUM = 7
    IDENT = 8
    WS = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'->'", "'\\'", "':'", "'+'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "ARROW", "SLASH", "DOSPUNTS", "SUMA", "LPAR", "RPAR", "NUM", 
            "IDENT", "WS" ]

    ruleNames = [ "ARROW", "SLASH", "DOSPUNTS", "SUMA", "LPAR", "RPAR", 
                  "NUM", "IDENT", "WS" ]

    grammarFileName = "hm.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


