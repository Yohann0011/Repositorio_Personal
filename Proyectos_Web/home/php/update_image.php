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
    echo json_encode(['error' => 'Conexión fallida: ' . $conn->connect_error]);
    exit;
}

// Verificar si el archivo fue subido y si se proporcionó un ID
if (isset($_FILES['file']) && isset($_POST['id'])) {
    $file = $_FILES['file'];
    $id = intval($_POST['id']);

    // Validar el archivo subido
    $allowedMimeTypes = ['image/jpeg', 'image/png', 'image/gif'];
    $fileMimeType = mime_content_type($file['tmp_name']);
    
    if (!in_array($fileMimeType, $allowedMimeTypes)) {
        echo json_encode(['error' => 'Tipo de archivo no permitido']);
        exit;
    }

    // Leer el contenido del archivo
    $image = file_get_contents($file['tmp_name']);

    // Preparar la sentencia SQL
    $stmt = $conn->prepare("UPDATE imagenes SET image = ? WHERE id = ?");
    if ($stmt) {
        $null = NULL; // Enviar NULL como parámetro de tipo LONG BLOB
        $stmt->bind_param("bi", $null, $id); // "bi" = BLOB y entero

        // Enviar el contenido del archivo como parámetro
        $stmt->send_long_data(0, $image);

        if ($stmt->execute()) {
            echo json_encode(['success' => 'Imagen actualizada correctamente']);
        } else {
            echo json_encode(['error' => 'Error al actualizar la imagen: ' . $stmt->error]);
        }

        $stmt->close();
    } else {
        echo json_encode(['error' => 'Error al preparar la consulta: ' . $conn->error]);
    }
} else {
    echo json_encode(['error' => 'No se recibió ninguna imagen o ID']);
}

$conn->close();
?>
