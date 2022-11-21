grammar Funx;

root: expr EOF | stmt EOF | EOF;

stmt: IDENT '<-' expr # Assig;

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
IDENT: [A-Z|a-z]+;
INT: [0-9]+;
WS: [ \n]+ -> skip;
