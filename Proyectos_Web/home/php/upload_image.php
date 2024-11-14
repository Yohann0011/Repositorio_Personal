<?php
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: POST');
header('Access-Control-Allow-Headers: Content-Type');

// Conexión a la base de datos
$host = 'sql308.byethost14.com';
$dbname = 'b14_36751384_imagenes_Carrusel';
$user = 'b14_36751384';
$password = 'Yelsaco1';

// Conectar a la base de datos
$conn = new mysqli($host, $user, $password, $dbname);

// Verificar conexión
if ($conn->connect_error) {
    echo 'Conexión fallida: ' . $conn->connect_error;
    exit;
}

// Verificar si el archivo fue subido
if (isset($_FILES['file'])) {
    $file = $_FILES['file']['tmp_name'];
    $image = addslashes(file_get_contents($file));
    $name = $_FILES['file']['name'];

    // Insertar la imagen en la base de datos
    $sql = "INSERT INTO imagenes (name, image) VALUES ('$name', '$image')";
    if ($conn->query($sql) === TRUE) {
        echo 'Imagen subida correctamente';
    } else {
        echo 'Error al subir la imagen: ' . $conn->error;
    }
} else {
    echo 'No se recibió ninguna imagen';
}

$conn->close();
?>
