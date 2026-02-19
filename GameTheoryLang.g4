grammar GameTheoryLang;

program : game* EOF;

game : 'game' gamename '{' players strategies payoff compute '}';
gamename : IDENTIFIER;

players : 'players' ':' player (',' player)*;
player : IDENTIFIER;

strategies : 'strategies' ':' strategyLine+;
strategyLine : player ':' startegy (',' startegy)*;
startegy : IDENTIFIER;

payoff : 'payoff' ':' payoffLine+;
payoffLine
  : LPAREN startegy (',' startegy)* RPAREN
    '->'
    LPAREN signedNumber (',' signedNumber)* RPAREN
  ;

compute : 'compute' ':' ('ShowMatrix' | 'BestResponses' | 'Nash');

LPAREN : '(';
RPAREN : ')';
IDENTIFIER : [a-zA-Z_] [a-zA-Z0-9_]*;
signedNumber : '-'? NUMBER;
NUMBER : [0-9]+;
WS : [ \t\r\n]+ -> skip;
LINE_COMMENT : '//' ~[\r\n]* -> skip;
BLOCK_COMMENT : '/*' .*? '*/' -> skip;