from node import Node, Tree, Empty

# retorna True si l'arbre es de tipus temporal (1 nivell i 
#el seu tipus ha de ser de la forma tx, on x es un numero)
def is_a_variable(root: Node) -> bool:
    if len(root.symbol) >= 2:
        return root.symbol[0] == "t" and root.symbol[1:].isnumeric()
    else:
        return False 

# retorna True si els arbres x i y son iguals, False si no    
def are_equal(x: Node, y: Node) -> bool:
    if len(x.children) != len(y.children):
        return False
    elif x.children == []:
        return x.symbol == y.symbol
    else:
        return x.symbol == y.symbol and are_equal(x.children[0], y.children[0]) and are_equal(x.children[1], y.children[1])

# retorna True si l'arbre root es de tipus complex (té més de 1 nivell)
# False si no
def is_complex_type(root: Node) -> bool:
    return root.symbol == "->"

# unifica 2 arbres de tipus, fa us d'un diccionari (subst) amb tipus sabuts
def unify(x: Node, y: Node, subst: dict) -> dict:
    if subst is None:
        return None
    elif are_equal(x,y):
        return subst
    elif is_a_variable(x):
        return unify_variable(x, y, subst)
    elif is_a_variable(y):
        return unify_variable(y, x, subst)
    elif is_complex_type(x) and is_complex_type(y):
        for childInd in range(2):
            subst = unify(x.children[childInd], y.children[childInd], subst)
        
        return subst
    else:
        raise TypeError(f"{typeTreeToString(x, subst)} vs {typeTreeToString(y, subst)}")

# unifica un arbre de tipus temporal amb un altre arbre, fa us d'un diccionari (subst)
# amb tipus ja sabuts
def unify_variable(v: Node, x: Node, subst: dict) -> dict:
    assert(is_a_variable(v))
    if v.symbol in subst:
        return unify(subst[v.symbol], x, subst)
    elif is_a_variable(x) and x.symbol in subst:
        return unify(v, subst[x.symbol], subst)
    elif is_one_contained_in_the_other(v, x, subst):
        raise TypeError(f"{typeTreeToString(v, {})} vs {typeTreeToString(x, {})}")
    else:
        return {**subst, v.symbol: x}

def is_one_contained_in_the_other(v: Node, term: Node, subst: dict) -> bool:
    assert(is_a_variable(v))
    if are_equal(v, term):
        return True
    elif is_a_variable(term) and term.symbol in subst:
        return is_one_contained_in_the_other(v, subst[term.symbol], subst)
    elif is_complex_type(term):
        return any(is_one_contained_in_the_other(v, child, subst) for child in term.children)
    else:
        return False

# infereix el tipus dels nodes d'un abre. Fa us d'un diccionari amb tipus ja 
#inferits o sabuts i retorna un diccionari amb els tipus inferits
def inferType(root: Node, inferedSymbolsTable: dict) -> dict:
    children = root.children
    if children != []:
        match root:
            case Node('@', [child1, child2], _):
                realTypeChild1 = child1.type
                inferedTypeChild1 = Node("->", [child2.type, root.type], Empty)

                inferedSymbolsTable = unify(realTypeChild1, inferedTypeChild1, inferedSymbolsTable)

                inferedSymbolsTable = inferType(child1, inferedSymbolsTable)
                inferedSymbolsTable = inferType(child2, inferedSymbolsTable)

            case Node('λ', [child1, child2], _):
                realTypeRoot = root.type
                inferedTypeRoot = Node("->", [child1.type, child2.type], Empty)

                inferedSymbolsTable = unify(realTypeRoot, inferedTypeRoot, inferedSymbolsTable)

                inferedSymbolsTable = inferType(child1, inferedSymbolsTable)
                inferedSymbolsTable = inferType(child2, inferedSymbolsTable)

    return inferedSymbolsTable

# passa un arbre de type a string, fa us d'un diccionari (symbolsTable)
# amb type sabuts
def typeTreeToString(root: Node, symbolsTable: dict) -> str:
    match root:
        case Node('->', [child1, child2], _):
            return f"({typeTreeToString(child1, symbolsTable)} -> {typeTreeToString(child2, symbolsTable)})"
        case Node(x, [], _):
            if x in symbolsTable:
                return typeTreeToString(symbolsTable[x], symbolsTable)
            
            return x