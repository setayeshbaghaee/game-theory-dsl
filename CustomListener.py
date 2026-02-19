
from antlr4 import *
from gen.GameTheoryLangListener import GameTheoryLangListener
from gen.GameTheoryLangParser import GameTheoryLangParser

from Ast import AST


class MyASTListener(GameTheoryLangListener):
    def __init__(self):
        self.ast = AST()

    def print_tree(self, node, prefix="", is_last=True):
        if node is None:
            return
    
        branch = "└── " if is_last else "├── "
        print(prefix + branch + str(node.value))
    
        children = []
        c = node.child
        while c is not None:
            children.append(c)
            c = c.brother
    
        for i, ch in enumerate(children):
            last = (i == len(children) - 1)
            new_prefix = prefix + ("    " if is_last else "│   ")
            self.print_tree(ch, new_prefix, last)


    def exitProgram(self, ctx: GameTheoryLangParser.ProgramContext):
        prog = self.ast.makeNode("Program", child=None, brother=None)
        games = ctx.game()
        if len(games) > 0:
            self.ast.addChild(prog, games[0].value_attr)
            for i in range(1, len(games)):
                self.ast.addBrother(games[i-1].value_attr, games[i].value_attr)

        ctx.value_attr = prog
        self.ast.root = prog

    def exitGame(self, ctx: GameTheoryLangParser.GameContext):
        name_leaf = self.ast.makeLeaf(ctx.gamename().getText())
        game_node = self.ast.makeNode("Game", child=name_leaf, brother=None)

        self.ast.addBrother(name_leaf, ctx.players().value_attr)
        self.ast.addBrother(ctx.players().value_attr, ctx.strategies().value_attr)
        self.ast.addBrother(ctx.strategies().value_attr, ctx.payoff().value_attr)
        self.ast.addBrother(ctx.payoff().value_attr, ctx.compute().value_attr)

        ctx.value_attr = game_node

    def exitPlayers(self, ctx: GameTheoryLangParser.PlayersContext):
        players_node = self.ast.makeNode("Players", child=None, brother=None)

        plist = ctx.player()
        if len(plist) > 0:
            first = self.ast.makeLeaf(plist[0].getText())
            self.ast.addChild(players_node, first)
            for i in range(1, len(plist)):
                self.ast.addBrother(first if i == 1 else prev, self.ast.makeLeaf(plist[i].getText()))
                prev = first.brother if i == 1 else prev.brother

        ctx.value_attr = players_node

    def exitStrategies(self, ctx: GameTheoryLangParser.StrategiesContext):
        st_node = self.ast.makeNode("Strategies", child=None, brother=None)

        lines = ctx.strategyLine()
        if len(lines) > 0:
            self.ast.addChild(st_node, lines[0].value_attr)
            for i in range(1, len(lines)):
                self.ast.addBrother(lines[i-1].value_attr, lines[i].value_attr)

        ctx.value_attr = st_node

    def exitStrategyLine(self, ctx: GameTheoryLangParser.StrategyLineContext):
        player_leaf = self.ast.makeLeaf(ctx.player().getText())
        line_node = self.ast.makeNode("StratOf", child=player_leaf, brother=None)

        slist = ctx.startegy()
        if len(slist) > 0:
            first_s = self.ast.makeLeaf(slist[0].getText())
            self.ast.addBrother(player_leaf, first_s)
            prev = first_s
            for i in range(1, len(slist)):
                s_leaf = self.ast.makeLeaf(slist[i].getText())
                self.ast.addBrother(prev, s_leaf)
                prev = s_leaf

        ctx.value_attr = line_node

    def exitPayoff(self, ctx: GameTheoryLangParser.PayoffContext):
        pay_node = self.ast.makeNode("Payoff", child=None, brother=None)

        lines = ctx.payoffLine()
        if len(lines) > 0:
            self.ast.addChild(pay_node, lines[0].value_attr)
            for i in range(1, len(lines)):
                self.ast.addBrother(lines[i-1].value_attr, lines[i].value_attr)

        ctx.value_attr = pay_node

    def exitPayoffLine(self, ctx: GameTheoryLangParser.PayoffLineContext):
        # (s1,s2,...) -> (u1,u2,...)
        entry = self.ast.makeNode("PayoffEntry", child=None, brother=None)

        prof = self.ast.makeNode("Profile", child=None, brother=None)
        self.ast.addChild(entry, prof)

        slist = ctx.startegy()
        if len(slist) > 0:
            first = self.ast.makeLeaf(slist[0].getText())
            self.ast.addChild(prof, first)
            prev = first
            for i in range(1, len(slist)):
                leaf = self.ast.makeLeaf(slist[i].getText())
                self.ast.addBrother(prev, leaf)
                prev = leaf

        util = self.ast.makeNode("Utilities", child=None, brother=None)
        self.ast.addBrother(prof, util)

        nums = ctx.signedNumber()
        if len(nums) > 0:
            first_n = self.ast.makeLeaf(nums[0].getText())
            self.ast.addChild(util, first_n)
            prev = first_n
            for i in range(1, len(nums)):
                leaf = self.ast.makeLeaf(nums[i].getText())
                self.ast.addBrother(prev, leaf)
                prev = leaf

        ctx.value_attr = entry

    def exitCompute(self, ctx):
        ctype = ctx.getChild(2).getText()   # ShowMatrix | BestResponses | Nash
        leaf = self.ast.makeLeaf(ctype)
        node = self.ast.makeNode("Compute", child=leaf, brother=None)
        ctx.value_attr = node

