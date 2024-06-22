from hmParser import hmParser
from hmVisitor import hmVisitor
import copy
from node import Node, Tree, Empty

# Visitador principal del programa 
class TreeVisitor(hmVisitor):
    def __init__(self, symbolsTable):
        self.symbolsTable = [copy.deepcopy(symbolsTable)]
        self.definitionsSymbolsTable = symbolsTable
        self.freeSymbol = 0

    def getFreeSymbol(self):
        currentLetter = f"t{self.freeSymbol}"
        self.freeSymbol += 1
        return currentLetter
    
    def searchInSymbolsTable(self, symbol: str) -> Node:
        for symbolsTable in self.symbolsTable:
                if symbol in symbolsTable:
                    return Node(symbol, [], symbolsTable[symbol])
        
        type = self.getFreeSymbol()
        self.symbolsTable[0][symbol] = Node(type, [], Empty)
        return Node(symbol, [], Node(type, [], Empty)) 

    def visitRoot(self, ctx:hmParser.RootContext):
        [statement, eof] = list(ctx.getChildren())
        resStatement = self.visit(statement)
        return resStatement
    
    def visitExprStmt(self, ctx: hmParser.ExprStmtContext):
        [expr] = list(ctx.getChildren())
        return self.visit(expr)
    
    def visitDefinitionStmt(self, ctx: hmParser.DefinitionStmtContext):
        [definition] = list(ctx.getChildren())
        return self.visit(definition)
    
    def visitDefinition(self, ctx: hmParser.DefinitionContext):
        [expr, _, _, type] = list(ctx.getChildren())
        treeType = self.visit(type)
        nameExpr = str(expr.getText())
        self.symbolsTable[-1][nameExpr] = treeType
        self.definitionsSymbolsTable[nameExpr] = treeType
        return None
    
    def visitTypeSimple(self, ctx: hmParser.TypeSimpleContext):
        [type] = list(ctx.getChildren())
        type = str(ctx.getText())
        return Node(type, [], Empty)
    
    def visitTypeAssociative(self, ctx: hmParser.TypeAssociativeContext):
        [type1, arrow, type2] = list(ctx.getChildren())
        treeType1 = self.visit(type1)
        treeType2 = self.visit(type2)
        return Node('->', [treeType1, treeType2],  Empty)
    
    def visitTypeParenthesis(self, ctx: hmParser.TypeParenthesisContext):
        [lpar, type, rpar] = list(ctx.getChildren())
        return self.visit(type)

    def visitParenthesis(self, ctx: hmParser.ParenthesisContext):
        [_, expr, _] = list(ctx.getChildren())
        return self.visit(expr)
    
    def visitAplicationExpr(self, ctx: hmParser.AplicationExprContext):
        [expr1, expr2] = list(ctx.getChildren())
        symbol = self.getFreeSymbol()

        treeExpr1 = self.visit(expr1)
        treeExpr2 = self.visit(expr2)

        return Node('@', [treeExpr1, treeExpr2], Node(symbol, [], Empty))

    def visitAbstractionExpr(self, ctx: hmParser.AbstractionExprContext):
        [expr] = list(ctx.getChildren())
        return self.visit(expr)
    
    def visitNumber(self, ctx: hmParser.NumberContext):
        number = str(ctx.getText())
        return self.searchInSymbolsTable(number)
    
    def visitIdent(self, ctx: hmParser.IdentContext):
        identifier = str(ctx.getText())
        return self.searchInSymbolsTable(identifier)
    
    def visitAnonymousFunction(self, ctx: hmParser.AnonymousFunctionContext):
        [_, ident, _, expr] = list(ctx.getChildren())
        self.symbolsTable.insert(0, {})

        symbol = self.getFreeSymbol()
        
        symbolIdent = self.getFreeSymbol()
        self.symbolsTable[0][str(ident)] = Node(symbolIdent, [], Empty)
        
        treeIdent = Node(str(ident), [], Node(symbolIdent, [], Empty))
        treeExpr = self.visit(expr)

        self.symbolsTable.pop(0)
            
        return Node('λ', [treeIdent, treeExpr], Node(symbol, [], Empty)) 

    def visitInfixOperator(self, ctx: hmParser.InfixOperatorContext):
        operator = str(ctx.getText())
        return self.searchInSymbolsTable(operator)
    