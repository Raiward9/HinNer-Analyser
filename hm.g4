// Gramàtica per expressions senzilles
grammar hm;
root : (statement)*             // letiqueta ja és root
     ;

statement : expr                            # expressioStmt
          | funcio                          # funcioStmt
          ;

expr : LPAR OPERADOR RPAR (IDENT|NUM)+       # operador
     | LPAR expr RPAR                        # parentesis 
     | LPAR funcio RPAR (IDENT|NUM)*         # funcioParametres
     | NUM                                   # numero
     | IDENT                                 # ident
     ;

funcio : SLASH IDENT ARROW expr
        ;                

ARROW          : '->';
SLASH          : '\\';
OPERADOR       : ('+'|'*'|'-'|'/');
LPAR           : '(';
RPAR           : ')';
NUM            : [0-9]+ ;
IDENT          : ([A-Z] | [a-z]) (([A-Z] | [a-z]) | [0-9])*;
WS             : [ \t\n\r]+ -> skip ;