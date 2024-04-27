// Gramàtica per expressions senzilles
grammar hm;
root : (expr)*             // letiqueta ja és root
     ;

statement : 
          | expr 
          ;

expr : LPAR OPERADOR RPAR (IDENT|NUM)+       # operadors
     | LPAR expr RPAR                        # parentesis
     | SLASH IDENT ARROW expr                # funcio
     | NUM                                   # numero
     | IDENT                                 # ident
     ;


ARROW          : '->';
SLASH          : '\\';
OPERADOR       : '+';
LPAR           : '(';
RPAR           : ')';
NUM            : [0-9]+ ;
IDENT          : ([A-Z] | [a-z]) (([A-Z] | [a-z]) | [0-9])*;
WS             : [ \t\n\r]+ -> skip ;