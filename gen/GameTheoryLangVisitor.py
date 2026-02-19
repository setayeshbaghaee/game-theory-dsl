# Generated from GameTheoryLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .GameTheoryLangParser import GameTheoryLangParser
else:
    from GameTheoryLangParser import GameTheoryLangParser

# This class defines a complete generic visitor for a parse tree produced by GameTheoryLangParser.

class GameTheoryLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GameTheoryLangParser#program.
    def visitProgram(self, ctx:GameTheoryLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GameTheoryLangParser#game.
    def visitGame(self, ctx:GameTheoryLangParser.GameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GameTheoryLangParser#gamename.
    def visitGamename(self, ctx:GameTheoryLangParser.GamenameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GameTheoryLangParser#players.
    def visitPlayers(self, ctx:GameTheoryLangParser.PlayersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GameTheoryLangParser#player.
    def visitPlayer(self, ctx:GameTheoryLangParser.PlayerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GameTheoryLangParser#strategies.
    def visitStrategies(self, ctx:GameTheoryLangParser.StrategiesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GameTheoryLangParser#strategyLine.
    def visitStrategyLine(self, ctx:GameTheoryLangParser.StrategyLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GameTheoryLangParser#startegy.
    def visitStartegy(self, ctx:GameTheoryLangParser.StartegyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GameTheoryLangParser#payoff.
    def visitPayoff(self, ctx:GameTheoryLangParser.PayoffContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GameTheoryLangParser#payoffLine.
    def visitPayoffLine(self, ctx:GameTheoryLangParser.PayoffLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GameTheoryLangParser#compute.
    def visitCompute(self, ctx:GameTheoryLangParser.ComputeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GameTheoryLangParser#signedNumber.
    def visitSignedNumber(self, ctx:GameTheoryLangParser.SignedNumberContext):
        return self.visitChildren(ctx)



del GameTheoryLangParser