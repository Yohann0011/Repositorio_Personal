// Función para inicializar los contadores A y B en 0 al cargar la página
window.onload = function() {
    // Determinar si la pantalla está en modo horizontal o vertical
    determinarOrientacionPantalla();
};

// Función para determinar la orientación de la pantalla
function determinarOrientacionPantalla() {
    var screenWidth = window.innerWidth;
    var screenHeight = window.innerHeight;
    var orientacion = (screenWidth > screenHeight) ? "horizontal" : "vertical";
    console.log("Orientación de la pantalla: " + orientacion);
    // Recargar la página si hay un cambio en la orientación
    window.addEventListener("resize", function() {
        var newScreenWidth = window.innerWidth;
        var newScreenHeight = window.innerHeight;
        if ((newScreenWidth > newScreenHeight && orientacion === "vertical") ||
            (newScreenWidth < newScreenHeight && orientacion === "horizontal")) {
            location.reload();
        }
    });
}

// Función para obtener los valores de los contadores del servidor y actualizar la interfaz
function actualizarContadores() {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "php/obtC.php", true);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var data = JSON.parse(xhr.responseText);
            if(data.espejo == 0 || data.espejo == 1){
            document.getElementById("A-counter").innerText = data.contadorA;
            document.getElementById("B-counter").innerText = data.contadorB;
            document.getElementById("Aset-counter").innerText = data.setA;
            document.getElementById("Bset-counter").innerText = data.setB;
            document.getElementById("time1").innerText = data.tiempoA;
            document.getElementById("time2").innerText = data.tiempoB;

            // Aplicar estilo de centrado
            if (data.contadorA > 9) {
                document.getElementById("A-counter").classList.add("over-nine");
            } else {
                document.getElementById("A-counter").classList.remove("over-nine");
            }

            if (data.contadorB > 9) {
                document.getElementById("B-counter").classList.add("over-nine");
            } else {
                document.getElementById("B-counter").classList.remove("over-nine");
            }

            }else{
            document.getElementById("A-counter").innerText = data.contadorB;
            document.getElementById("B-counter").innerText = data.contadorA;
            document.getElementById("Aset-counter").innerText = data.setB;
            document.getElementById("Bset-counter").innerText = data.setA;
            document.getElementById("time1").innerText = data.tiempoB;
            document.getElementById("time2").innerText = data.tiempoA;
            

            // Aplicar estilo de centrado
            if (data.contadorB > 9) {
                document.getElementById("A-counter").classList.add("over-nine");
            } else {
                document.getElementById("A-counter").classList.remove("over-nine");
            }

            if (data.contadorA > 9) {
                document.getElementById("B-counter").classList.add("over-nine");
            } else {
                document.getElementById("B-counter").classList.remove("over-nine");
            }

            }
        }
    };
    xhr.send();
}

// Actualizar los contadores cada segundo
setInterval(actualizarContadores, 100);

// Llamar a la función una vez para mostrar los valores al cargar la página
actualizarContadores();

// Calcular el ancho y alto de la pantalla
var anchoPantalla = window.innerWidth; // Obtén el ancho de la pantalla
var altoPantalla = window.innerHeight; // Obtén el alto de la pantalla
document.body.style.setProperty('--screenWidth', anchoPantalla + 'px'); // Establece el valor de la variable --screenWidth
document.body.style.setProperty('--screenHeight', altoPantalla + 'px'); // Establece el valor de la variable --screenHeight
