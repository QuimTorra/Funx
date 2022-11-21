grammar Funx;

root : expr EOF ;

expr : expr ('*' | '/' | '%') expr # Bin 
     | expr ('+' | '-') expr # Bin 
     | expr ('=' | '!=' | '<' | '>' | '<=' | '>=') expr # Rel
     | TRUE # Rel
     | FALSE # Rel
     | INT # Val
     ;

TRUE : 'True';
FALSE : 'False';
INT : [0-9]+ ;
WS  : [ \n]+ -> skip ; 
