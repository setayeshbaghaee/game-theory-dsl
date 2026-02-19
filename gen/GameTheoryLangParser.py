# Generated from GameTheoryLang.g4 by ANTLR 4.13.1
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
        4,1,21,113,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,5,0,26,8,0,10,
        0,12,0,29,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,
        2,1,3,1,3,1,3,1,3,1,3,5,3,49,8,3,10,3,12,3,52,9,3,1,4,1,4,1,5,1,
        5,1,5,4,5,59,8,5,11,5,12,5,60,1,6,1,6,1,6,1,6,1,6,5,6,68,8,6,10,
        6,12,6,71,9,6,1,7,1,7,1,8,1,8,1,8,4,8,78,8,8,11,8,12,8,79,1,9,1,
        9,1,9,1,9,5,9,86,8,9,10,9,12,9,89,9,9,1,9,1,9,1,9,1,9,1,9,1,9,5,
        9,97,8,9,10,9,12,9,100,9,9,1,9,1,9,1,10,1,10,1,10,1,10,1,11,3,11,
        109,8,11,1,11,1,11,1,11,0,0,12,0,2,4,6,8,10,12,14,16,18,20,22,0,
        1,1,0,11,13,108,0,27,1,0,0,0,2,32,1,0,0,0,4,41,1,0,0,0,6,43,1,0,
        0,0,8,53,1,0,0,0,10,55,1,0,0,0,12,62,1,0,0,0,14,72,1,0,0,0,16,74,
        1,0,0,0,18,81,1,0,0,0,20,103,1,0,0,0,22,108,1,0,0,0,24,26,3,2,1,
        0,25,24,1,0,0,0,26,29,1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,28,30,
        1,0,0,0,29,27,1,0,0,0,30,31,5,0,0,1,31,1,1,0,0,0,32,33,5,1,0,0,33,
        34,3,4,2,0,34,35,5,2,0,0,35,36,3,6,3,0,36,37,3,10,5,0,37,38,3,16,
        8,0,38,39,3,20,10,0,39,40,5,3,0,0,40,3,1,0,0,0,41,42,5,17,0,0,42,
        5,1,0,0,0,43,44,5,4,0,0,44,45,5,5,0,0,45,50,3,8,4,0,46,47,5,6,0,
        0,47,49,3,8,4,0,48,46,1,0,0,0,49,52,1,0,0,0,50,48,1,0,0,0,50,51,
        1,0,0,0,51,7,1,0,0,0,52,50,1,0,0,0,53,54,5,17,0,0,54,9,1,0,0,0,55,
        56,5,7,0,0,56,58,5,5,0,0,57,59,3,12,6,0,58,57,1,0,0,0,59,60,1,0,
        0,0,60,58,1,0,0,0,60,61,1,0,0,0,61,11,1,0,0,0,62,63,3,8,4,0,63,64,
        5,5,0,0,64,69,3,14,7,0,65,66,5,6,0,0,66,68,3,14,7,0,67,65,1,0,0,
        0,68,71,1,0,0,0,69,67,1,0,0,0,69,70,1,0,0,0,70,13,1,0,0,0,71,69,
        1,0,0,0,72,73,5,17,0,0,73,15,1,0,0,0,74,75,5,8,0,0,75,77,5,5,0,0,
        76,78,3,18,9,0,77,76,1,0,0,0,78,79,1,0,0,0,79,77,1,0,0,0,79,80,1,
        0,0,0,80,17,1,0,0,0,81,82,5,15,0,0,82,87,3,14,7,0,83,84,5,6,0,0,
        84,86,3,14,7,0,85,83,1,0,0,0,86,89,1,0,0,0,87,85,1,0,0,0,87,88,1,
        0,0,0,88,90,1,0,0,0,89,87,1,0,0,0,90,91,5,16,0,0,91,92,5,9,0,0,92,
        93,5,15,0,0,93,98,3,22,11,0,94,95,5,6,0,0,95,97,3,22,11,0,96,94,
        1,0,0,0,97,100,1,0,0,0,98,96,1,0,0,0,98,99,1,0,0,0,99,101,1,0,0,
        0,100,98,1,0,0,0,101,102,5,16,0,0,102,19,1,0,0,0,103,104,5,10,0,
        0,104,105,5,5,0,0,105,106,7,0,0,0,106,21,1,0,0,0,107,109,5,14,0,
        0,108,107,1,0,0,0,108,109,1,0,0,0,109,110,1,0,0,0,110,111,5,18,0,
        0,111,23,1,0,0,0,8,27,50,60,69,79,87,98,108
    ]

class GameTheoryLangParser ( Parser ):

    grammarFileName = "GameTheoryLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'game'", "'{'", "'}'", "'players'", "':'", 
                     "','", "'strategies'", "'payoff'", "'->'", "'compute'", 
                     "'ShowMatrix'", "'BestResponses'", "'Nash'", "'-'", 
                     "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "LPAREN", "RPAREN", 
                      "IDENTIFIER", "NUMBER", "WS", "LINE_COMMENT", "BLOCK_COMMENT" ]

    RULE_program = 0
    RULE_game = 1
    RULE_gamename = 2
    RULE_players = 3
    RULE_player = 4
    RULE_strategies = 5
    RULE_strategyLine = 6
    RULE_startegy = 7
    RULE_payoff = 8
    RULE_payoffLine = 9
    RULE_compute = 10
    RULE_signedNumber = 11

    ruleNames =  [ "program", "game", "gamename", "players", "player", "strategies", 
                   "strategyLine", "startegy", "payoff", "payoffLine", "compute", 
                   "signedNumber" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    LPAREN=15
    RPAREN=16
    IDENTIFIER=17
    NUMBER=18
    WS=19
    LINE_COMMENT=20
    BLOCK_COMMENT=21

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(GameTheoryLangParser.EOF, 0)

        def game(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GameTheoryLangParser.GameContext)
            else:
                return self.getTypedRuleContext(GameTheoryLangParser.GameContext,i)


        def getRuleIndex(self):
            return GameTheoryLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = GameTheoryLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 24
                self.game()
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 30
            self.match(GameTheoryLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def gamename(self):
            return self.getTypedRuleContext(GameTheoryLangParser.GamenameContext,0)


        def players(self):
            return self.getTypedRuleContext(GameTheoryLangParser.PlayersContext,0)


        def strategies(self):
            return self.getTypedRuleContext(GameTheoryLangParser.StrategiesContext,0)


        def payoff(self):
            return self.getTypedRuleContext(GameTheoryLangParser.PayoffContext,0)


        def compute(self):
            return self.getTypedRuleContext(GameTheoryLangParser.ComputeContext,0)


        def getRuleIndex(self):
            return GameTheoryLangParser.RULE_game

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGame" ):
                listener.enterGame(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGame" ):
                listener.exitGame(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGame" ):
                return visitor.visitGame(self)
            else:
                return visitor.visitChildren(self)




    def game(self):

        localctx = GameTheoryLangParser.GameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_game)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(GameTheoryLangParser.T__0)
            self.state = 33
            self.gamename()
            self.state = 34
            self.match(GameTheoryLangParser.T__1)
            self.state = 35
            self.players()
            self.state = 36
            self.strategies()
            self.state = 37
            self.payoff()
            self.state = 38
            self.compute()
            self.state = 39
            self.match(GameTheoryLangParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GamenameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(GameTheoryLangParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return GameTheoryLangParser.RULE_gamename

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGamename" ):
                listener.enterGamename(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGamename" ):
                listener.exitGamename(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGamename" ):
                return visitor.visitGamename(self)
            else:
                return visitor.visitChildren(self)




    def gamename(self):

        localctx = GameTheoryLangParser.GamenameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_gamename)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(GameTheoryLangParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PlayersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def player(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GameTheoryLangParser.PlayerContext)
            else:
                return self.getTypedRuleContext(GameTheoryLangParser.PlayerContext,i)


        def getRuleIndex(self):
            return GameTheoryLangParser.RULE_players

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlayers" ):
                listener.enterPlayers(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlayers" ):
                listener.exitPlayers(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPlayers" ):
                return visitor.visitPlayers(self)
            else:
                return visitor.visitChildren(self)




    def players(self):

        localctx = GameTheoryLangParser.PlayersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_players)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(GameTheoryLangParser.T__3)
            self.state = 44
            self.match(GameTheoryLangParser.T__4)
            self.state = 45
            self.player()
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 46
                self.match(GameTheoryLangParser.T__5)
                self.state = 47
                self.player()
                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PlayerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(GameTheoryLangParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return GameTheoryLangParser.RULE_player

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlayer" ):
                listener.enterPlayer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlayer" ):
                listener.exitPlayer(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPlayer" ):
                return visitor.visitPlayer(self)
            else:
                return visitor.visitChildren(self)




    def player(self):

        localctx = GameTheoryLangParser.PlayerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_player)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(GameTheoryLangParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StrategiesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def strategyLine(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GameTheoryLangParser.StrategyLineContext)
            else:
                return self.getTypedRuleContext(GameTheoryLangParser.StrategyLineContext,i)


        def getRuleIndex(self):
            return GameTheoryLangParser.RULE_strategies

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStrategies" ):
                listener.enterStrategies(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStrategies" ):
                listener.exitStrategies(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStrategies" ):
                return visitor.visitStrategies(self)
            else:
                return visitor.visitChildren(self)




    def strategies(self):

        localctx = GameTheoryLangParser.StrategiesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_strategies)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(GameTheoryLangParser.T__6)
            self.state = 56
            self.match(GameTheoryLangParser.T__4)
            self.state = 58 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 57
                self.strategyLine()
                self.state = 60 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==17):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StrategyLineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def player(self):
            return self.getTypedRuleContext(GameTheoryLangParser.PlayerContext,0)


        def startegy(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GameTheoryLangParser.StartegyContext)
            else:
                return self.getTypedRuleContext(GameTheoryLangParser.StartegyContext,i)


        def getRuleIndex(self):
            return GameTheoryLangParser.RULE_strategyLine

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStrategyLine" ):
                listener.enterStrategyLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStrategyLine" ):
                listener.exitStrategyLine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStrategyLine" ):
                return visitor.visitStrategyLine(self)
            else:
                return visitor.visitChildren(self)




    def strategyLine(self):

        localctx = GameTheoryLangParser.StrategyLineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_strategyLine)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.player()
            self.state = 63
            self.match(GameTheoryLangParser.T__4)
            self.state = 64
            self.startegy()
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 65
                self.match(GameTheoryLangParser.T__5)
                self.state = 66
                self.startegy()
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StartegyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(GameTheoryLangParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return GameTheoryLangParser.RULE_startegy

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStartegy" ):
                listener.enterStartegy(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStartegy" ):
                listener.exitStartegy(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStartegy" ):
                return visitor.visitStartegy(self)
            else:
                return visitor.visitChildren(self)




    def startegy(self):

        localctx = GameTheoryLangParser.StartegyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_startegy)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(GameTheoryLangParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PayoffContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def payoffLine(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GameTheoryLangParser.PayoffLineContext)
            else:
                return self.getTypedRuleContext(GameTheoryLangParser.PayoffLineContext,i)


        def getRuleIndex(self):
            return GameTheoryLangParser.RULE_payoff

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPayoff" ):
                listener.enterPayoff(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPayoff" ):
                listener.exitPayoff(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPayoff" ):
                return visitor.visitPayoff(self)
            else:
                return visitor.visitChildren(self)




    def payoff(self):

        localctx = GameTheoryLangParser.PayoffContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_payoff)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(GameTheoryLangParser.T__7)
            self.state = 75
            self.match(GameTheoryLangParser.T__4)
            self.state = 77 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 76
                self.payoffLine()
                self.state = 79 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==15):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PayoffLineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(GameTheoryLangParser.LPAREN)
            else:
                return self.getToken(GameTheoryLangParser.LPAREN, i)

        def startegy(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GameTheoryLangParser.StartegyContext)
            else:
                return self.getTypedRuleContext(GameTheoryLangParser.StartegyContext,i)


        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(GameTheoryLangParser.RPAREN)
            else:
                return self.getToken(GameTheoryLangParser.RPAREN, i)

        def signedNumber(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GameTheoryLangParser.SignedNumberContext)
            else:
                return self.getTypedRuleContext(GameTheoryLangParser.SignedNumberContext,i)


        def getRuleIndex(self):
            return GameTheoryLangParser.RULE_payoffLine

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPayoffLine" ):
                listener.enterPayoffLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPayoffLine" ):
                listener.exitPayoffLine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPayoffLine" ):
                return visitor.visitPayoffLine(self)
            else:
                return visitor.visitChildren(self)




    def payoffLine(self):

        localctx = GameTheoryLangParser.PayoffLineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_payoffLine)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(GameTheoryLangParser.LPAREN)
            self.state = 82
            self.startegy()
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 83
                self.match(GameTheoryLangParser.T__5)
                self.state = 84
                self.startegy()
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 90
            self.match(GameTheoryLangParser.RPAREN)
            self.state = 91
            self.match(GameTheoryLangParser.T__8)
            self.state = 92
            self.match(GameTheoryLangParser.LPAREN)
            self.state = 93
            self.signedNumber()
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 94
                self.match(GameTheoryLangParser.T__5)
                self.state = 95
                self.signedNumber()
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 101
            self.match(GameTheoryLangParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComputeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GameTheoryLangParser.RULE_compute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompute" ):
                listener.enterCompute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompute" ):
                listener.exitCompute(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompute" ):
                return visitor.visitCompute(self)
            else:
                return visitor.visitChildren(self)




    def compute(self):

        localctx = GameTheoryLangParser.ComputeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_compute)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(GameTheoryLangParser.T__9)
            self.state = 104
            self.match(GameTheoryLangParser.T__4)
            self.state = 105
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14336) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SignedNumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(GameTheoryLangParser.NUMBER, 0)

        def getRuleIndex(self):
            return GameTheoryLangParser.RULE_signedNumber

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSignedNumber" ):
                listener.enterSignedNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSignedNumber" ):
                listener.exitSignedNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSignedNumber" ):
                return visitor.visitSignedNumber(self)
            else:
                return visitor.visitChildren(self)




    def signedNumber(self):

        localctx = GameTheoryLangParser.SignedNumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_signedNumber)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 107
                self.match(GameTheoryLangParser.T__13)


            self.state = 110
            self.match(GameTheoryLangParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





