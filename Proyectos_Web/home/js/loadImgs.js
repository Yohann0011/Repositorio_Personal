document.addEventListener('DOMContentLoaded', function() {
    // Lista de IDs de imágenes a cargar
    const imageIds = [1, 2, 3, 4, 5, 6, 7, 8];

    // URL base del archivo PHP para cargar imágenes
    const baseUrl = 'http://blackchikens.byethost14.com/php/loadImg.php?id=';

    // Contenedor de imágenes
    const imagenesDiv = document.getElementById('imagenes');

    // Función para cargar una imagen
    function loadImage(imageId) {
        return new Promise((resolve, reject) => {
            const img = document.createElement('img');
            img.src = baseUrl + imageId;
            img.alt = `Imagen ${imageId}`;
            img.onload = function() {
                console.log(`Imagen ${imageId} cargada correctamente`);
                resolve(img);
            };
            img.onerror = function() {
                console.error(`Error al cargar la imagen ${imageId}`);
                reject();
            };
        });
    }

    // Cargar todas las imágenes
    Promise.all(imageIds.map(loadImage))
        .then(images => {
            // Insertar todas las imágenes en el contenedor
            images.forEach(img => imagenesDiv.appendChild(img));
        })
        .catch(() => {
            console.error('Error al cargar algunas imágenes');
        });
});


function initializeSlider() {
    const sliderImages = document.querySelectorAll('.carrusel-imagen');
    let currentIndex = 0;

    function showImage(index) {
        sliderImages.forEach((img, i) => {
            img.style.display = i === index ? 'block' : 'none';
        });
    }

    function nextImage() {
        currentIndex = (currentIndex + 1) % sliderImages.length;
        showImage(currentIndex);
    }

    setInterval(nextImage, 3000); // Cambia la imagen cada 3 segundos

    // Mostrar la primera imagen inicialmente
    showImage(currentIndex);
}
