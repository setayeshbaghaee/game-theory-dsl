from antlr4 import *
import argparse
import sys
import subprocess

from gen.GameTheoryLangLexer import GameTheoryLangLexer
from gen.GameTheoryLangParser import GameTheoryLangParser

from CustomListener import MyASTListener
from Semantic import SemanticAnalyzer

from code_generator import generate_c


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-n", "--file", default="input.txt")
    ap.add_argument("--gen", action="store_true", help="generate python code to generated_game.py")
    args = ap.parse_args()

    stream = FileStream(args.file, encoding="utf-8")
    lexer = GameTheoryLangLexer(stream)
    tokens = CommonTokenStream(lexer)
    parser = GameTheoryLangParser(tokens)

    tree = parser.program()

    listener = MyASTListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    print("\n====== AST ======")
    listener.print_tree(listener.ast.root)

    print("\n====== Semantic ======")
    sem = SemanticAnalyzer(listener.ast.root)
    sem.run()
    print("Semantic OK ✅")

   
    out_c = generate_c(
        game_name=sem.game_name,
        players=sem.players,
        strategies=sem.strategies,
        payoffs=sem.payoffs,
        compute=sem.compute,
        out_path="generated_game.c"
    )
    print("\nGenerated:", out_c)
    try:
        subprocess.run(["gcc", "generated_game.c", "-o", "generated_game.exe"], check=True)
        print("\n====== Running Generated C Program ======")
        subprocess.run(["generated_game.exe"], check=True)
    except Exception as e:
        print("\n(Note) gcc not available or compile failed. You can compile generated_game.c manually.")



if __name__ == "__main__":
    main()
