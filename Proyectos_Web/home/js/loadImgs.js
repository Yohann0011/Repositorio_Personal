const sliderImages = document.querySelectorAll('.slider img');
let currentIndex = 0;

function showImage(index) {
    sliderImages.forEach((img, i) => {
        img.classList.remove('active');
        if (i === index) {
            img.classList.add('active');
        }
    });
}

function nextImage() {
    currentIndex = (currentIndex + 1) % sliderImages.length;
    showImage(currentIndex);
}

setInterval(nextImage, 3000); // Cambia la imagen cada 3 segundos

// Mostrar la primera imagen inicialmente
showImage(currentIndex);
