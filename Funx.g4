grammar Funx;

root: stmt EOF | EOF;

stmt:
	CL											# CLI
	| VAR '<-' expr								# Assig
	| FN args '{' stmt '}'						# Func
	| IF expr '{' stmt '}'						# If
	| IF expr '{' stmt '}' ELSE '{' stmt '}'	# IfElse
	| WHILE expr '{' stmt '}'					# While
	| stmt stmt									# RecStmt
	| expr										# Exprs;

expr:
	'(' expr ')'										# Bin
	| <assoc = right> expr '^' expr						# Bin
	| expr ('*' | '/' | '%') expr						# Bin
	| expr ('+' | '-') expr								# Bin
	| expr ('=' | '!=' | '<' | '>' | '<=' | '>=') expr	# Rel
	| TRUE												# Rel
	| FALSE												# Rel
	| FN expr*											# IdentFN
	| VAR												# IdentVAR
	| INT												# Val;

args: VAR* # Arg;

TRUE: 'True';
FALSE: 'False';
IF: 'if';
ELSE: 'else';
WHILE: 'while';
FN: ([A-Z]) ([a-zA-Z] | [0-9] | '_')*;
VAR: ([a-z]) ([a-zA-Z] | [0-9] | '_')*;
// IDENT: ([a-zA-Z] | [0-9] | '_')*;
CL: (':') ([A-Za-z0-9])*;
INT: [0-9]+;
WS: [ \n\r\t]+ -> skip;
