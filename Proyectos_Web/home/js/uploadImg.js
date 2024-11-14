document.addEventListener('DOMContentLoaded', () => {
    const uploadForm = document.getElementById('uploadForm');
    uploadForm.addEventListener('submit', function(event) {
        event.preventDefault();

        const fileInput = document.getElementById('fileInput');
        const file = fileInput.files[0];

        if (file) {
            const formData = new FormData();
            formData.append('file', file);

            fetch('php/upload_image.php', {
                method: 'POST',
                body: formData
            })
            .then(response => response.text())
            .then(result => {
                document.getElementById('response').textContent = result;
                fileInput.value = ''; // Clear the input
            })
            .catch(error => {
                console.error('Error:', error);
            });
        } else {
            document.getElementById('response').textContent = 'Por favor, selecciona una imagen para subir.';
        }
    });
});
