<?php
// Obtener los valores de los contadores desde la solicitud POST
$contadorA = isset($_POST['contadorA']) ? intval($_POST['contadorA']) : 0;
$contadorB = isset($_POST['contadorB']) ? intval($_POST['contadorB']) : 0;
$setA = isset($_POST['setA']) ? intval($_POST['setA']) : 0;
$setB = isset($_POST['setB']) ? intval($_POST['setB']) : 0;
$cPuntos = isset($_POST['cPuntos']) ? intval($_POST['cPuntos']) : 0;
$cSets = isset($_POST['cSets']) ? intval($_POST['cSets']) : 0;
$tiempoA = isset($_POST['tiempoA']) ? $_POST['tiempoA'] : "";
$tiempoB = isset($_POST['tiempoB']) ? $_POST['tiempoB'] : "";
$espejo = isset($_POST['espejo']) ? intval($_POST['espejo']) : 0;

$filePath = 'datos.txt';

// Construir la cadena de datos
$data = "$contadorA,$contadorB,$setA,$setB,$cPuntos,$cSets,$tiempoA,$tiempoB,$espejo";

// Guardar los datos en el archivo, sobrescribiendo el contenido existente
if (file_put_contents($filePath, $data) !== false) {
    echo "Datos guardados correctamente.";
} else {
    echo "Error al guardar los datos en el archivo.";
}
?>
