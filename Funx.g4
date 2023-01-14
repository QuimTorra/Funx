grammar Funx;

root: stmt EOF | EOF;

stmt:
	FN args '{' stmt? '}'						# Func
	| VAR '<-' expr								# Assig
	| IF expr '{' stmt? '}'						# If
	| IF expr '{' stmt? '}' ELSE '{' stmt? '}'	# IfElse
	| WHILE expr '{' stmt? '}'					# While
    | FOR VAR 'in' expr '{' stmt? '}'           # For
    | OUTPUT expr                               # Output
    | INPUT VAR                                 # Input
	| stmt stmt									# RecStmt
	| expr										# Exprs;

expr:
	'(' expr ')'										# Bin
	| <assoc = right> expr '^' expr						# Bin
    | expr '[' expr ']'                                 # ListIndx
    | expr '[' expr? ':' expr? ']'                      # ListSlice
    | '[' (expr (',' expr)*)? ']'                       # List
    | '[' expr? '..' expr ']'                           # ListRange
	| expr ('*' | '/' | '%') expr						# Bin
	| expr ('+' | '-') expr								# Bin
	| expr ('=' | '!=' | '<' | '>' | '<=' | '>=' | 'and' | 'or' | 'xor') expr	# Rel
    | ('not') expr                                      # Rel
	| TRUE												# Rel
	| FALSE												# Rel
	| FN expr*											# IdentFN
	| VAR												# IdentVAR
	| INT												# Val;

args: VAR* # Arg;

INPUT: 'input';
OUTPUT: 'print';
TRUE: 'True';
FALSE: 'False';
IF: 'if';
ELSE: 'else';
WHILE: 'while';
FOR: 'for';
// IDENT: ([a-zA-Z])([a-zA-Z] | [0-9] | '_')*;
FN: ([A-Z]) ([a-zA-Z] | [0-9] | '_')*;
VAR: ([a-z]) ([a-zA-Z] | [0-9] | '_')*;
// CL: (':') ([A-Za-z0-9])*;
INT: ('-')?[0-9]+;
CS: '#' ~[\n]* [\n] -> skip;
WS: [ \n\r\t]+ -> skip;
