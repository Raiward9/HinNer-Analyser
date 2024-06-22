// Gramàtica per expressions senzilles
grammar hm;
root : statement EOF
     ;

statement : expr                                       # exprStmt
          | definition                                 # definitionStmt
          ; 

definition : expr TWOPOINTS TWOPOINTS type
          ;

type : TYPE                                           # typeSimple
      | <assoc=right> type ARROW type                 # typeAssociative
      | LPAR type RPAR                                # typeParenthesis
      ;

expr : LPAR expr RPAR                                  # parenthesis                 
     | expr expr                                       # aplicationExpr
     | abstraction                                     # abstractionExpr
     | NUM                                             # number
     | IDENT                                           # ident
     ;

abstraction: SLASH IDENT ARROW expr                    # anonymousFunction
           | LPAR SUM RPAR                             # infixOperator
           ;

ARROW          : '->';
SLASH          : '\\';
TWOPOINTS      : ':';
SUM            : '+';
LPAR           : '(';
RPAR           : ')';
NUM            : [0-9]+ ;
TYPE           : [A-Z]+;
IDENT          : [a-zA-Z] ([a-zA-Z] | [0-9])*;
WS             : [ \t\n\r]+ -> skip ;