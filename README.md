## GameTheoryLang 
I designed GameTheoryLang as a Domain-Specific Language (DSL) for modeling and analyzing multi-player strategic-form games.

The language allows users to formally define players, strategies, payoff functions, and compute core game-theoretic concepts such as:

ShowMatrix

BestResponses

Pure Nash Equilibrium

The project implements a full compiler-like pipeline:

ANTLR Grammar → Parsing → AST Construction → Semantic Analysis → C Code Generation → Execution

## Motivation

GameTheoryLang was designed to explore:

DSL design for mathematical modeling

Compiler construction concepts

Formal grammar design using ANTLR

Semantic validation and static analysis

Algorithmic computation of Nash equilibria

Code generation to a low-level language (C)

## Language Capabilities

With GameTheoryLang, you can:

Define a game (name + players)

Define strategy sets for each player

Specify payoff values for each strategy profile

Choose a computation using compute

Supported computations:

ShowMatrix

BestResponses

Nash (Pure strategy Nash equilibrium)

## Language Syntax

game GameName {
  players: P1, P2, ..., Pn

  strategies:
    P1: S1, S2, ...
    P2: S1, S2, ...
    ...
    Pn: S1, S2, ...

  payoff:
    (S_P1, S_P2, ..., S_Pn) -> (u1, u2, ..., u_n)

  compute: ShowMatrix | BestResponses | Nash
}

## Compiler Architecture

The project follows a structured compilation pipeline:

GameTheoryLang.g4     → ANTLR grammar definition
CustomListener.py     → Parse tree traversal & AST construction
Ast.py                → Abstract Syntax Tree representation
Semantic.py           → Semantic validation & constraint checking
code_generator.py     → C code generation
generated_game.c      → Generated C program
main.py               → Pipeline entry point


Each stage is clearly separated to maintain clean architecture and extensibility.

## Semantic Validation

The language performs strict semantic checks, including:

Duplicate player or strategy names

Undefined strategy usage

Payoff dimension mismatch

Incomplete payoff table (required for Nash / BestResponses)

Incorrect payoff tuple size

Example error:

Semantic Error:
Payoff must contain exactly 3 values for players: A, B, C
Found: (1, 2)


This ensures correctness before code generation.

## Game-Theoretic Computations
1️⃣ ShowMatrix

Displays all strategy profiles and corresponding payoff tuples.

2️⃣ BestResponses

For each player and fixed opponent strategies:

given (<strategies of other players>) -> {best responses}


If payoffs tie, all maximizing strategies are returned.

3️⃣ Pure Nash Equilibrium

A strategy profile
S = (s1, s2, …, sn)

is a Nash equilibrium if no player can improve payoff via unilateral deviation:

ui(si, s−i) ≥ ui(s'i, s−i)


If none exist:

Nash Equilibrium:
None found (No pure strategy equilibrium)

## Design Challenges

Handling arbitrary N-player payoff combinations

Ensuring complete payoff table validation before Nash computation

Designing a clean AST structure independent of ANTLR parse tree

Avoiding exponential blowup in best-response computation

## How to Run

Put a valid DSL program inside input.txt.

Run:

python main.py


Make sure:

ANTLR-generated sources exist under gen/

C compiler is available if code generation is executed

The output includes:

AST display (if enabled)

Computation results

Or semantic errors

## Example: Prisoner’s Dilemma
game PrisonersDilemma {
  players: A, B

  strategies:
    A: Cooperate, Defect
    B: Cooperate, Defect

  payoff:
    (Cooperate, Cooperate) -> (-1, -1)
    (Cooperate, Defect)    -> (-3, 0)
    (Defect, Cooperate)    -> (0, -3)
    (Defect, Defect)       -> (-2, -2)

  compute: Nash
}


Output:

Game: PrisonersDilemma
Nash Equilibrium:
  (Defect, Defect)
  
Additional examples are available in the `examples/` directory.

## What This Project Demonstrates

DSL design for formal modeling

ANTLR grammar implementation

AST construction via custom listener

Static semantic analysis

Implementation of best-response and Nash equilibrium algorithms

Code generation to C

Structured compiler pipeline design

## Future Improvements

Support for mixed-strategy Nash equilibrium

Matrix-style visualization for 2-player games

Performance optimization for larger N-player games

Enhanced CLI interface

Additional static analysis rules

## Author

Setayesh Baghaee
Computer Engineering Student
