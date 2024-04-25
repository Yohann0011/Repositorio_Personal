function medidas(){
// Obtener medidas de la pantalla
var anchoPantalla = window.innerWidth;
var altoPantalla = window.innerHeight;
var a = document.querySelector('.mitad').height;
document.documentElement.style.setProperty('--alto', altoPantalla + 'px');
document.documentElement.style.setProperty('--ancho', anchoPantalla + 'px');
document.documentElement.style.setProperty('--a', a + 'px');


}

// Función para cargar el contenido del archivo
function cargarContenido() {
    fetch('lectura.txt')
    .then(response => response.text())
    .then(texto => {
        // Separar el texto en un array de palabras
        var palabras = texto.split(/\s+/);
        var indice = 0;
        // Función para cambiar la palabra cada 5ms
        setInterval(function() {
            var palabra = palabras[indice % palabras.length];
            var indiceMitad = Math.floor(palabra.length / 2);
            var inicio = palabra.substring(0, indiceMitad);
            var mitad = palabra.charAt(indiceMitad);
            var fin = palabra.substring(indiceMitad + 1);

            document.getElementById("p1").innerHTML = inicio;
            document.getElementById("p2").innerText = mitad;
            document.getElementById("p3").innerText = fin;

            var m2 = document.querySelector('.mitad').offsetWidth;
            // Aplicar el ancho de .mitad como una variable CSS
            document.documentElement.style.setProperty('--m2', m2 + 'px');

            indice++;
        }, 300);
    });
}

// Llamar a la función para cargar el contenido del archivo
cargarContenido();
medidas();

