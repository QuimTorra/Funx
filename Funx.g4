grammar Funx;

root: stmt EOF | EOF;

stmt:
	IDENT '<-' expr								# Assig
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
	| IDENT												# Ident
	| INT												# Val;

TRUE: 'True';
FALSE: 'False';
IF: 'if';
ELSE: 'else';
WHILE: 'while';
IDENT: [A-Z|a-z]+;
INT: [0-9]+;
WS: [ \n\r]+ -> skip;
