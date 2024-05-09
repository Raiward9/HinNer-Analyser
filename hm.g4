// Gramàtica per expressions senzilles
grammar hm;
root : statement EOF 
     ;

statement : expr                        # exprStmt
          | definicio                   # definicioStmt
          ; 

definicio : expr DOSPUNTS DOSPUNTS tipus
          ;

tipus : IDENT                                          # tipusSimple
      | <assoc=right> tipus ARROW tipus                # tipusAssociatiu
      | LPAR tipus RPAR                                # tipusParentesis
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
// TIPUS          : ('A'..'Z')+;
IDENT          : ('a'..'z' | 'A'..'Z') ('a'..'z' | 'A'..'Z' | '0'..'9')*;
WS             : [ \t\n\r]+ -> skip ;