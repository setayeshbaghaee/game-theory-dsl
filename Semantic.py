class SemanticError(Exception):
    pass


class SemanticAnalyzer:
    def __init__(self, ast_root):
        self.root = ast_root

        self.game_name = None
        self.players = []
        self.strategies = {}  
        self.payoffs = []     
        self.compute = None


    def _children(self, node):
        res = []
        c = node.child
        while c is not None:
            res.append(c)
            c = c.brother
        return res

    def _find_child_by_value(self, node, value):
        c = node.child
        while c is not None:
            if c.value == value:
                return c
            c = c.brother
        return None


    def extract(self):
        if self.root is None or self.root.value != "Program":
            raise SemanticError("Internal Error: AST root is not Program")

        game_node = self.root.child
        if game_node is None or game_node.value != "Game":
            raise SemanticError("Internal Error: Program has no Game node")

        parts = self._children(game_node)
        if len(parts) < 5:
            raise SemanticError("Internal Error: Game node is missing sections")

        self.game_name = str(parts[0].value)

        players_node = self._find_child_by_value(game_node, "Players")
        strategies_node = self._find_child_by_value(game_node, "Strategies")
        payoff_node = self._find_child_by_value(game_node, "Payoff")
        compute_node = self._find_child_by_value(game_node, "Compute")

        if players_node is None or strategies_node is None or payoff_node is None or compute_node is None:
            raise SemanticError("Internal Error: Missing one of Players/Strategies/Payoff/Compute")

    
        for p in self._children(players_node):
            self.players.append(str(p.value))

        for strat_of in self._children(strategies_node):
            if strat_of.value != "StratOf":
                continue
            items = self._children(strat_of)
            if len(items) < 2:
                continue
            pl = str(items[0].value)
            sset = set(str(x.value) for x in items[1:])
            self.strategies[pl] = sset

        for entry in self._children(payoff_node):
            if entry.value != "PayoffEntry":
                continue

            prof_node = self._find_child_by_value(entry, "Profile")
            util_node = self._find_child_by_value(entry, "Utilities")
            if prof_node is None or util_node is None:
                continue

            profile = [str(x.value) for x in self._children(prof_node)]
            utilities = [int(str(x.value)) for x in self._children(util_node)]
            self.payoffs.append((profile, utilities))

        comp_parts = self._children(compute_node)
        if len(comp_parts) >= 1:
            self.compute = str(comp_parts[0].value)


    def check_players_min_2(self):
        if len(self.players) < 2:
            raise SemanticError("Semantic Error:\nPlayers must be at least 2")

    def check_duplicate_players(self):
        if len(set(self.players)) != len(self.players):
            raise SemanticError("Semantic Error:\nDuplicate player name detected")

    def check_every_player_has_strategies(self):
        for p in self.players:
            if p not in self.strategies or len(self.strategies[p]) == 0:
                raise SemanticError(f"Semantic Error:\nPlayer '{p}' has no strategies defined")

    def check_payoff_dimensions(self):
        n = len(self.players)
        for (profile, utilities) in self.payoffs:
            if len(profile) != n:
                raise SemanticError(
                    f"Semantic Error:\nPayoff profile must contain exactly {n} strategies for players: {', '.join(self.players)}\n"
                    f"Found profile: ({', '.join(profile)})"
                )
            if len(utilities) != n:
                raise SemanticError(
                    f"Semantic Error:\nPayoff must contain exactly {n} values for players: {', '.join(self.players)}\n"
                    f"Found: ({', '.join(map(str, utilities))})"
                )

    def check_undefined_strategy_usage(self):
        for (profile, utilities) in self.payoffs:
            for i, s in enumerate(profile):
                p = self.players[i]
                allowed = self.strategies.get(p, set())
                if s not in allowed:
                    allowed_str = ", ".join(sorted(list(allowed)))
                    raise SemanticError(
                        f"Semantic Error:\nUndefined strategy '{s}' used for player '{p}' in payoff definition.\n"
                        f"Allowed strategies for {p} are: {{{allowed_str}}}"
                    )

    def check_missing_payoffs_if_needed(self):
        if self.compute not in ("Nash", "BestResponses"):
            return

        expected = 1
        for p in self.players:
            expected *= len(self.strategies.get(p, []))

        found = len(self.payoffs)
        if found != expected:
            raise SemanticError(
                f"Semantic Error:\nMissing payoff entries. Expected {expected}, found {found}."
            )


    def run(self):
        self.extract()
        self.check_players_min_2()
        self.check_duplicate_players()
        self.check_every_player_has_strategies()
        self.check_payoff_dimensions()
        self.check_undefined_strategy_usage()
        self.check_missing_payoffs_if_needed()

        return True
