// Gramàtica per expressions senzilles
grammar hm;
root : statement EOF 
     ;

statement : expr                        # exprStmt
          | definicio                   # definicioStmt
          ; 

definicio : expr DOSPUNTS DOSPUNTS tipus
          ;

tipus : TIPUS (ARROW TIPUS)* 
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
DOSPUNTS       : ':';
SUMA           : '+';
LPAR           : '(';
RPAR           : ')';
NUM            : [0-9]+ ;
TIPUS          : [A-Z]+ ;
IDENT          : [a-zA-Z] ([a-zA-Z]  | [0-9])* [a-z] ;
WS             : [ \t\n\r]+ -> skip ;