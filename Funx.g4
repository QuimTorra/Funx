grammar Funx;

root: expr EOF;

expr:
	<assoc = right> expr '^' expr						# Bin
	| expr ('*' | '/' | '%') expr						# Bin
	| expr ('+' | '-') expr								# Bin
	| expr ('=' | '!=' | '<' | '>' | '<=' | '>=') expr	# Rel
	| TRUE												# Rel
	| FALSE												# Rel
	| IDENT												# Ident
	| INT												# Val;

TRUE: 'True';
FALSE: 'False';
IDENT: [A-z]+;
INT: [0-9]+;
WS: [ \n]+ -> skip;
