// Gramàtica per expressions senzilles
grammar hm;
root : expr            
     ;

expr : LPAR expr RPAR                                  # parentesis                 
     | (LPAR funcio RPAR | operadorInfix)  (expr)*     # aplicacio
     | funcio                                          # funcioExpr 
     | operadorInfix                                   # operadorExpr
     | NUM                                             # numero
     | IDENT                                           # ident
     ;

funcio: SLASH IDENT ARROW expr
     ; 

operadorInfix: LPAR SUMA RPAR
     ; 

ARROW          : '->';
SLASH          : '\\';
SUMA           : '+';
LPAR           : '(';
RPAR           : ')';
NUM            : [0-9]+ ;
IDENT          : ([A-Z] | [a-z]) (([A-Z] | [a-z]) | [0-9])*;
WS             : [ \t\n\r]+ -> skip ;