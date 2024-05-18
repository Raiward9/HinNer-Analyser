<h1>Analitzador HinNer</h1>
<h2>Llibreries usades</h2>
<ul>
    <li>antlr4</li>
    <li>pickle</li>
    <li>dataclasses</li>
    <li>streamlit</li>
    <li>graphviz</li>
    <li>pandas</li>
    <li>copy</li>
</ul>
<h2>Coses a evitar i tenir en compte abans d'executar el programa</h2>
<h3>Evitar</h3>
<ul>
    <li>Deixar línies buides, aquestes es detectaran com a errors de sintaxis ja que l'intèrpret no trobarà el EOF de l'expressió.</li>
    <li>Posar diverses expressions o definicions a la mateixa línia del textarea.</li>
</ul>
<h3>Tenir en compte</h3>
<ul>
    <li>Es poden colocar múltiples expressions o definicions alhora al textarea, però s'executaran de forma seqüencial.</li>
    <li>En cas que surti per pantalla un TypeError amb els tipus definits, implicarà que hi ha hagut algun conflicte de tipus en la inferència. Si per altra banda es
        un error on apareixen tipus temporals, implicarà que no s'ha definit correctament l'expressió.
    </li>
    <li>
        Els tipus definits han d'estar enterament escrits en majúscules.
    </li>
</ul>
<h2>Manual</h2>
<ol>
    <li>Afegir un statement (definició o expressió) per línia al textarea.</li>
    <li>Clicar el botó "fer".</li>
</ol>

<h2>Pecularitats del codi</h2>
<p>El mecanisme d'inferència s'ha realitzat adaptant el codi d'unificació d'equacions que podem trobar al següent blog:</p>
(https://eli.thegreenplace.net/2018/unification/) <br></br>
<p>En un començament, vaig intentar fer la inferència de tipus de la forma explicada a classe, és a dir, de forma bottom-up, no obstant, per tal de crear un intèrpret més potent he decidit optar per aquesta opció.</p>
<p>
Per altra banda, també cal destacar que el visitador al tractar amb definicions retorna None i modifica una taula de simbols encarregada de les definicions que després es rescata. D'aquesta forma es pot saber si la crida al visitador era una crida amb una definició o una expressió.
</p>

<h2>Tests</h2>
<p>Els tests es troben separats en 6 fitxers amb el nom testx, on la x és el número de tasca al que corresponen. Es tracten de tests manuals i d'integració, és a dir, que són
tests que s'han de provar manualment i proven la funcionalitat sencera de l'aplicació. <br></br> Els casos a provar dintre de cada fitxer estan separats per salts de línia.</p>

<h2>Documentació del codi</h2>

<h3>TreeVisitor</h3>
<p>El TreeVisitor és l'únic visitador del programa, el qual s'encarrega de crear un objecte del tipus algebraic Arbre que està composat per la classe Node i la classe Buit 
que com es pot intuir, serveixen per implementar un Arbre (que en aquest cas serà binari, és a dir, cada node tindrà com a molt 2 fills). Cada node de l'arbre tindrà un 
símbol, una llista amb els seus fills (que també seran de tipus Arbre) i el seu tipus (que també serà de tipus Arbre).</p>

<h3>Funcions fora del visitador</h3>
<ul>
    <li>
        generarArbre: la qual donada l'arbre i una taula amb alguns tipus, aplica un breadth first search sobre l'arbre creant a la vegada l'objecte Graph necessari per 
        visualitzar l'arbre en streamlit
    </li>
    <li>
        passarArbreDeTipusAString: donat un arbre de tipus i un taula amb alguns tipus, retorna l'string corresponent al tipus de l'arbre.
    </li>
    <li>
        unificar: funció que s'encarrega d'unificar 2 arbres de tipus i retorna els tipus inferits en un diccionari. 
    </li>
    <li>
        unificar_variable: funció que s'encarrega d'unificar 2 arbres de tipus quan com a mínim un d'ells és un tipus temporal i retorna els tipus inferits en un diccionari 
        (s'usa per la unificació). 
    </li>
    <li>
        esta_una_contenida_a_altre: funció que s'encarrega de comprovar si 1 arbre de tipus temporal està contingut a un altre arbre de tipus(s'usa per la unificació). 
    </li>
    <li>
        es_una_variable: comprova si un arbre de tipus correspon a una variable temporal, és a dir, si és un arbre d'1 nivell i el seu simbol es una t seguida per un número 
        (s'usa per la unificació).
    </li>
    <li>
        son_iguals: comprova si dos arbres de tipus són iguals (s'usa per la unificació).
    </li>
    <li>
        es_tipus_complex: comprova si un arbre de tipus correspon a un tipus complex, és a dir, si té més d'un nivell (s'usa per la unificació).
    </li>
    <li>
        inferirTipus: donat un arbre infereix els tipus dels seus nodes si és possible, si no, llença una excepció.
    </li>
    <li>
        createDataTable: crea un dataframe a partir d'un diccionari amb els tipus dels nodes.
    </li>
    <li>
        executaAnalitzador: donat un statement en forma de string, s'encarrega de tot el procès a partir de que s'ha clicat al botó "fer". Des de cridar al parser i al visitor
        fins a imprimir per pantalla totes les dades necessàries.
    </li>
</ul>
