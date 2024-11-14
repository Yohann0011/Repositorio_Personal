window.onload = function() {
    determinarOrientacionPantalla();
};

// Orientación de la pantalla
function determinarOrientacionPantalla() {
    var anchoPantalla = window.innerWidth;
    var altoPantalla = window.innerHeight;
    var orientacion = (anchoPantalla > altoPantalla) ? "horizontal" : "vertical";
    console.log("Orientación de la pantalla: " + orientacion);
    // Recargar la página si hay un cambio en la orientación
    window.addEventListener("resize", function() {
        var anchoPantalla = window.innerWidth;
        var altoPantalla = window.innerHeight;
        if ((anchoPantalla > altoPantalla && orientacion === "vertical") ||
            (anchoPantalla < altoPantalla && orientacion === "horizontal")) {
            location.reload();
        }
    });
}

// Calcular el ancho y alto de la pantalla
var anchoPantalla = window.innerWidth;
var altoPantalla = window.innerHeight;
document.body.style.setProperty('--anchoPantalla', anchoPantalla + 'px');
document.body.style.setProperty('--altoPantalla', altoPantalla + 'px');