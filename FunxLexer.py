# Generated from Funx.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\21")
        buf.write("Q\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\3\3\3\3\4\3\4\3\5")
        buf.write("\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\17\6\17G\n\17\r\17\16\17H\3\20\6")
        buf.write("\20L\n\20\r\20\16\20M\3\20\3\20\2\2\21\3\3\5\4\7\5\t\6")
        buf.write("\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\37\21\3\2\4\3\2\62;\4\2\f\f\"\"\2R\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2")
        buf.write("\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2")
        buf.write("\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2")
        buf.write("\37\3\2\2\2\3!\3\2\2\2\5#\3\2\2\2\7%\3\2\2\2\t\'\3\2\2")
        buf.write("\2\13)\3\2\2\2\r+\3\2\2\2\17-\3\2\2\2\21\60\3\2\2\2\23")
        buf.write("\62\3\2\2\2\25\64\3\2\2\2\27\67\3\2\2\2\31:\3\2\2\2\33")
        buf.write("?\3\2\2\2\35F\3\2\2\2\37K\3\2\2\2!\"\7,\2\2\"\4\3\2\2")
        buf.write("\2#$\7\61\2\2$\6\3\2\2\2%&\7\'\2\2&\b\3\2\2\2\'(\7-\2")
        buf.write("\2(\n\3\2\2\2)*\7/\2\2*\f\3\2\2\2+,\7?\2\2,\16\3\2\2\2")
        buf.write("-.\7#\2\2./\7?\2\2/\20\3\2\2\2\60\61\7>\2\2\61\22\3\2")
        buf.write("\2\2\62\63\7@\2\2\63\24\3\2\2\2\64\65\7>\2\2\65\66\7?")
        buf.write("\2\2\66\26\3\2\2\2\678\7@\2\289\7?\2\29\30\3\2\2\2:;\7")
        buf.write("V\2\2;<\7t\2\2<=\7w\2\2=>\7g\2\2>\32\3\2\2\2?@\7H\2\2")
        buf.write("@A\7c\2\2AB\7n\2\2BC\7u\2\2CD\7g\2\2D\34\3\2\2\2EG\t\2")
        buf.write("\2\2FE\3\2\2\2GH\3\2\2\2HF\3\2\2\2HI\3\2\2\2I\36\3\2\2")
        buf.write("\2JL\t\3\2\2KJ\3\2\2\2LM\3\2\2\2MK\3\2\2\2MN\3\2\2\2N")
        buf.write("O\3\2\2\2OP\b\20\2\2P \3\2\2\2\5\2HM\3\b\2\2")
        return buf.getvalue()


class FunxLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    TRUE = 12
    FALSE = 13
    INT = 14
    WS = 15

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'*'", "'/'", "'%'", "'+'", "'-'", "'='", "'!='", "'<'", "'>'", 
            "'<='", "'>='", "'True'", "'False'" ]

    symbolicNames = [ "<INVALID>",
            "TRUE", "FALSE", "INT", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "TRUE", "FALSE", "INT", 
                  "WS" ]

    grammarFileName = "Funx.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


