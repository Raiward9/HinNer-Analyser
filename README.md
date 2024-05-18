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
    <li>Deixar línies buides, aquestes es detectaran com a error de sintaxis ja que l'intèrpret no trobarà el EOF de l'expressió.</li>
    <li>Posar diverses expressions o definicions a la mateixa línia del textarea.</li>
</ul>
<h3>Tenir en compte</h3>
<ul>
    <li>Es poden colocar múltiples expressions o definicions alhora al textarea, però s'executaran de forma seqüencial.</li>
    <li>En cas que surti per pantalla un TypeError amb els tipus definits, implicarà que hi ha hagut algun conflicte de tipus en la inferència. Si per altra banda es
        un error on apareixen tipus temporals, implicarà que no s'ha definit correctament l'expressió.
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