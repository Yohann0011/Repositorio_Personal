<?php
// Obtener los valores de los contadores desde el archivo datos.txt
$filePath = 'datos.txt';

// Verificar si el archivo existe
if (file_exists($filePath)) {
    // Leer los datos desde el archivo
    $data = file_get_contents($filePath);

    // Convertir los datos en un array
    $datos = explode(',', $data);

    // Crear un array asociativo para devolver los datos en formato JSON
    $responseData = array(
        'contadorA' => intval($datos[0]),
        'contadorB' => intval($datos[1]),
        'setA' => intval($datos[2]),
        'setB' => intval($datos[3]),
        'cPuntos' => intval($datos[4]),
        'cSets' => intval($datos[5]),
        'tiempoA' => ($datos[6]),
        'tiempoB' => ($datos[7]),
        'espejo' => intval($datos[8])
    );

    // Devolver los datos en formato JSON
    echo json_encode($responseData);
} else {
    // Devolver un mensaje de error si el archivo no existe
    echo json_encode(array('error' => 'El archivo datos.txt no existe.'));
}
?>
