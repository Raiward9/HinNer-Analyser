<h1>Analitzador HinNer</h1>
<h2>Libraries used</h2>
<ul>
    <li>antlr4</li>
    <li>pickle</li>
    <li>dataclasses</li>
    <li>streamlit</li>
    <li>graphviz</li>
    <li>pandas</li>
    <li>copy</li>
</ul>

<h2>Manual</h2>
<p>Avisos abans d'executar el programa: Compte amb posar linies buides, ja que ho detectarà com a error de sintaxis (ja que no trobarà el EOF de l'expressió).
També cal destacar que es poden colocar multiples statements alhora al textarea, però s'executaran seqüencialment.
</p>
<ol>
    <li>Afegir un statement (definicio o expressio) per linia al textarea. Molt de compte amb deixar linies buides.</li>
    <li>Clicar el botó "fer"</li>
</ol>

<h2>Pecularitats de l'intèrpret</h2>
<p>El mecanisme d'inferència s'ha realitzat adaptant el codi d'unificació d'equacions que podem trobar al següent blog:</p>.
[Link text](https://eli.thegreenplace.net/2018/unification/).
En un començament, vaig intentar fer la inferència de tipus de la forma explicada a classe, és a dir, de forma bottom-up, no obstant, per tal de crear un intèrpret més potent, he decidit optar per aquesta opció.