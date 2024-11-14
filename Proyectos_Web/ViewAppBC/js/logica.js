/*  
Inicializar variables
Calcular las medidas de la pantalla
/*  Ancho de la pantalla    */
var anchoP = window.innerWidth; 
/*  Alto de la pantalla */
var altoP = window.innerHeight;

/*  Reglajes    */
// Puntos
var pT = document.getElementById("cPuntos").value;
//  Sets
var sT = document.getElementById("cSets").value;
// Alargue
var aL = 1;
// Espejo
var eS = 0;
// Tiempos
var tA = document.getElementById("time1");
var tB = document.getElementById("time2");

/*  Marcador    */
//  Contador A
var conA = document.getElementById("A-counter");
//  Contador Set A
var conAS = document.getElementById("Aset-counter");
//  Contador B
var conB = document.getElementById("B-counter");
//  Contador Set B
var conBS = document.getElementById("Bset-counter");
//  Auxiliar
var aux = 0;

//  Funcion que se llama al cargar la pagina
window.onload = function() {
    document.body.style.setProperty('--Apantalla', anchoP + 'px');
    determinarOrientacionPantalla();
    
    // Verificar si es la primera ejecución
    if (localStorage.getItem("run") === null) {
        reT();
        localStorage.setItem("run", "false");
    } else {
        // Recuperar los valores de los contadores del almacenamiento local si están disponibles
        conA.innerText = localStorage.getItem("contadorA");
        conB.innerText = localStorage.getItem("contadorB");
        conAS.innerText = localStorage.getItem("setA");
        conBS.innerText = localStorage.getItem("setB");
        pT = localStorage.getItem("cPuntos");
        sT = localStorage.getItem("cSets");
        tA.innerText = localStorage.getItem("tiempoA");
        tB.innerText = localStorage.getItem("tiempoB");
        aliNum();
    }
};

// Función para determinar la orientación de la pantalla
function determinarOrientacionPantalla() {
    var orientacion = (anchoP > altoP) ? "horizontal" : "vertical";
    //console.log("Orientación de la pantalla: " + orientacion);

    // Recargar la página si hay un cambio en la orientación
    window.addEventListener("resize", function() {
        var newAnchoP = window.innerWidth;
        var newAltoP = window.innerHeight;
        if ((newAnchoP > newAltoP && orientacion === "vertical") ||
            (newAnchoP < newAltoP && orientacion === "horizontal")) {
            location.reload();
        }
    });
}


// Función para incrementar el contador de A al hacer clic en ABox-Counter
function masA() {
    if(parseInt(conAS.innerText) < sT && parseInt(conBS.innerText) < sT){
        aux = parseInt(conA.innerText) + 1;
        conA.innerText = String (aux);
        aliNum();
        reglas();
    }
}

// Función para incrementar el contador de B al hacer clic en BBox-Counter
function masB() {
    if(parseInt(conAS.innerText) < sT && parseInt(conBS.innerText) < sT){
    aux = parseInt(conB.innerText) + 1;
    conB.innerText = String (aux);
    aliNum();
    reglas();
    }
}

// Función para decrementar el valor del contador
function disA() {
    if (parseInt(conA.innerText) > 0) {
        aux = parseInt(conA.innerText) - 1;
        conA.innerText = String (aux);
        aliNum();
        reglas();
    }
}

function disB() {
    if (parseInt(conB.innerText) > 0) {
        aux = parseInt(conB.innerText) - 1;
        conB.innerText = String (aux);
        aliNum();
        reglas();
    }
}

function cambio() {
    aux = conA.innerText;
    conA.innerText = conB.innerText;
    conB.innerText = aux;
    aux = conAS.innerText;
    conAS.innerText = conBS.innerText;
    conBS.innerText = aux;
    aliNum();
    gC();
}

function timeA() {
    if(tA.innerText == "2 TIEMPOS"){
        tA.innerText = "1 TIEMPO";
    }else{
    if(tA.innerText == "1 TIEMPO"){
        tA.innerText = "SIN TIEMPOS";
        tA.style.textDecoration = "line-through";
        tA.style.backgroundColor = "#303030";
        }
    }
    gC();
}

function timeB() {
    if(tB.innerText == "2 TIEMPOS"){
        tB.innerText = "1 TIEMPO";
    }else{
    if(tB.innerText == "1 TIEMPO"){
        tB.innerText = "SIN TIEMPOS";
        tB.style.textDecoration = "line-through";
        tB.style.backgroundColor = "#303030";
        }
    }
    gC();
}

function reglas() {
    if(parseInt(conA.innerText) >= pT && (parseInt(conA.innerText) - parseInt(conB.innerText)) >= 2 && aL == 1 ){
        aux = parseInt(conAS.innerText) + 1;
        conAS.innerText = String (aux);
        re()
        if(parseInt(conAS.innerText) == sT || parseInt(conBS.innerText) == sT){
            cambio()
        }
        cambio()
    }else{
        if(parseInt(conA.innerText) == pT && aL == 0 ){
        aux = parseInt(conAS.innerText) + 1;
        conAS.innerText = String (aux);
        re()
        if(parseInt(conAS.innerText) == sT || parseInt(conBS.innerText) == sT){
            cambio()
        }
        cambio()
        }
    }
    if(parseInt(conB.innerText) >= pT && (parseInt(conB.innerText) - parseInt(conA.innerText)) >= 2 && aL == 1){
        aux = parseInt(conBS.innerText) + 1;
        conBS.innerText = String (aux);
        re()
        if(parseInt(conAS.innerText) == sT || parseInt(conBS.innerText) == sT){
            cambio()
        }
        cambio()
    }else{
        if(parseInt(conB.innerText) == pT && aL == 0 ){
            aux = parseInt(conBS.innerText) + 1;
            conBS.innerText = String (aux);
            re()
            if(parseInt(conAS.innerText) == sT || parseInt(conBS.innerText) == sT){
                cambio()
            }
            cambio()
        }
    }
    gC();
}
function retime(){
    tA.innerText = "2 TIEMPOS";
    tA.style.textDecoration = null;
    tA.style.backgroundColor = "darkblue";
    tB.innerText = "2 TIEMPOS";
    tB.style.textDecoration = null;
    tB.style.backgroundColor = "darkred";
}

/*SECCION REINICIAR*/
function re (){
    conA.innerText = "0";
    conB.innerText = "0";
    aliNum();
    retime();
    gC();
}

function reT (){
    conA.innerText = "0";
    conB.innerText = "0";
    conAS.innerText = "0";
    conBS.innerText = "0";
    aliNum();
    retime();
    gC();
}

/* SECCIÓN AJUSTES */
var config = document.getElementById("config");
var puntosElements = document.getElementsByClassName("puntos");
var boton = document.getElementById("gBut");
var vali = document.getElementById("vali");

function alargue(){
    vali.classList.toggle("animado")
    if(vali.innerText == "SI"){
        vali.classList.add("animado")
        vali.innerText = "NO";
        aL = 0;
    }else{
        vali.classList.add("animado")
        vali.innerText = "SI";
        aL = 1;
    }
}

function verAjus() {
    config.style.visibility = "visible"; // Restaura la visibilidad del elemento con ID "config"
    // Restaura la visibilidad y la transición de cada elemento con la clase "puntos"
    for (var i = 0; i < puntosElements.length; i++) {
        var letras = puntosElements[i].querySelectorAll("label span"); // Selecciona todas las letras dentro del elemento
        letras.forEach(function(letra, index) {
            // Restaura el retraso de transición de la letra
            letra.style.transitionDelay = index * 50 + "ms"; // Restaura el retraso de transición a múltiplos de 50ms
            letra.style.visibility = "visible"; // Restaura la visibilidad de la letra
        });
        puntosElements[i].style.visibility = "visible"; // Restaura la visibilidad del elemento con la clase "puntos"
    }
    boton.style.visibility = "visible"; // Restaura la visibilidad del botón con ID "gBut"
}
function oculAjus() {
    // Guarda los valores del limite de puntos
    pT = document.getElementById("cPuntos").value;
    sT = document.getElementById("cSets").value;
    gC()

    config.style.visibility = "hidden"; // Oculta el elemento con ID "config"

    // Oculta cada elemento con la clase "puntos" y quita el retraso de transición de las letras
    for (var i = 0; i < puntosElements.length; i++) {
        var letras = puntosElements[i].querySelectorAll("label span"); // Selecciona todas las letras dentro del elemento
        letras.forEach(function(letra) {
            letra.style.transitionDelay = "0ms"; // Quita el retraso de transición de la letra
            letra.style.visibility = "hidden"; // Oculta la letra
        });

        puntosElements[i].style.visibility = "hidden"; // Oculta el elemento con la clase "puntos"
    }

    boton.style.visibility = "hidden"; // Oculta el botón con ID "gBut"
}
/* SECCIÓN AJUSTES VISUALES*/
//  Funcion para alinear los valores en las cajas
function aliNum(){
    if (parseInt(conA.innerText) < 10){
        conA.classList.remove('over-nine');
        conA.classList.add('under-nine');
    }else{
        conA.classList.remove('under-nine');
        conA.classList.add('over-nine');
    }

    if (parseInt(conB.innerText) < 10){
        conB.classList.remove('over-nine');
        conB.classList.add('under-nine');
    }else{
        conB.classList.remove('under-nine');
        conB.classList.add('over-nine');
    }
}

function gC() {
    // Guardar los valores de los contadores en el almacenamiento local
    localStorage.setItem("contadorA", conA.innerText);
    localStorage.setItem("contadorB", conB.innerText);
    localStorage.setItem("setA", conAS.innerText);
    localStorage.setItem("setB", conBS.innerText);
    localStorage.setItem("cPuntos", pT);
    localStorage.setItem("cSets", sT);
    localStorage.setItem("tiempoA",tA.innerText);
    localStorage.setItem("tiempoB",tB.innerText);
    localStorage.setItem("espejo",eS);
}