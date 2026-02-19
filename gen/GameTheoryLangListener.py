# Generated from GameTheoryLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .GameTheoryLangParser import GameTheoryLangParser
else:
    from GameTheoryLangParser import GameTheoryLangParser

# This class defines a complete listener for a parse tree produced by GameTheoryLangParser.
class GameTheoryLangListener(ParseTreeListener):

    # Enter a parse tree produced by GameTheoryLangParser#program.
    def enterProgram(self, ctx:GameTheoryLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by GameTheoryLangParser#program.
    def exitProgram(self, ctx:GameTheoryLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by GameTheoryLangParser#game.
    def enterGame(self, ctx:GameTheoryLangParser.GameContext):
        pass

    # Exit a parse tree produced by GameTheoryLangParser#game.
    def exitGame(self, ctx:GameTheoryLangParser.GameContext):
        pass


    # Enter a parse tree produced by GameTheoryLangParser#gamename.
    def enterGamename(self, ctx:GameTheoryLangParser.GamenameContext):
        pass

    # Exit a parse tree produced by GameTheoryLangParser#gamename.
    def exitGamename(self, ctx:GameTheoryLangParser.GamenameContext):
        pass


    # Enter a parse tree produced by GameTheoryLangParser#players.
    def enterPlayers(self, ctx:GameTheoryLangParser.PlayersContext):
        pass

    # Exit a parse tree produced by GameTheoryLangParser#players.
    def exitPlayers(self, ctx:GameTheoryLangParser.PlayersContext):
        pass


    # Enter a parse tree produced by GameTheoryLangParser#player.
    def enterPlayer(self, ctx:GameTheoryLangParser.PlayerContext):
        pass

    # Exit a parse tree produced by GameTheoryLangParser#player.
    def exitPlayer(self, ctx:GameTheoryLangParser.PlayerContext):
        pass


    # Enter a parse tree produced by GameTheoryLangParser#strategies.
    def enterStrategies(self, ctx:GameTheoryLangParser.StrategiesContext):
        pass

    # Exit a parse tree produced by GameTheoryLangParser#strategies.
    def exitStrategies(self, ctx:GameTheoryLangParser.StrategiesContext):
        pass


    # Enter a parse tree produced by GameTheoryLangParser#strategyLine.
    def enterStrategyLine(self, ctx:GameTheoryLangParser.StrategyLineContext):
        pass

    # Exit a parse tree produced by GameTheoryLangParser#strategyLine.
    def exitStrategyLine(self, ctx:GameTheoryLangParser.StrategyLineContext):
        pass


    # Enter a parse tree produced by GameTheoryLangParser#startegy.
    def enterStartegy(self, ctx:GameTheoryLangParser.StartegyContext):
        pass

    # Exit a parse tree produced by GameTheoryLangParser#startegy.
    def exitStartegy(self, ctx:GameTheoryLangParser.StartegyContext):
        pass


    # Enter a parse tree produced by GameTheoryLangParser#payoff.
    def enterPayoff(self, ctx:GameTheoryLangParser.PayoffContext):
        pass

    # Exit a parse tree produced by GameTheoryLangParser#payoff.
    def exitPayoff(self, ctx:GameTheoryLangParser.PayoffContext):
        pass


    # Enter a parse tree produced by GameTheoryLangParser#payoffLine.
    def enterPayoffLine(self, ctx:GameTheoryLangParser.PayoffLineContext):
        pass

    # Exit a parse tree produced by GameTheoryLangParser#payoffLine.
    def exitPayoffLine(self, ctx:GameTheoryLangParser.PayoffLineContext):
        pass


    # Enter a parse tree produced by GameTheoryLangParser#compute.
    def enterCompute(self, ctx:GameTheoryLangParser.ComputeContext):
        pass

    # Exit a parse tree produced by GameTheoryLangParser#compute.
    def exitCompute(self, ctx:GameTheoryLangParser.ComputeContext):
        pass


    # Enter a parse tree produced by GameTheoryLangParser#signedNumber.
    def enterSignedNumber(self, ctx:GameTheoryLangParser.SignedNumberContext):
        pass

    # Exit a parse tree produced by GameTheoryLangParser#signedNumber.
    def exitSignedNumber(self, ctx:GameTheoryLangParser.SignedNumberContext):
        pass



del GameTheoryLangParser