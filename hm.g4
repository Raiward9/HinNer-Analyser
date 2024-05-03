// Gramàtica per expressions senzilles
grammar hm;
root : expr EOF 
     ;

expr : LPAR expr RPAR                                  # parentesis                 
     | expr expr                                       # aplicacioExpr
     | abstraccio                                      # abstraccioExpr
     | NUM                                             # numero
     | IDENT                                           # ident
     ;

abstraccio: SLASH IDENT ARROW expr      # funcioAnonima
          | LPAR SUMA RPAR              # operadorInfix
          ;

ARROW          : '->';
SLASH          : '\\';
SUMA           : '+';
LPAR           : '(';
RPAR           : ')';
NUM            : [0-9]+ ;
IDENT          : ([A-Z] | [a-z]) (([A-Z] | [a-z]) | [0-9])*;
WS             : [ \t\n\r]+ -> skip ;