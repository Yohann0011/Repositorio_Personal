document.addEventListener('DOMContentLoaded', function() {
    const radios = document.querySelectorAll('.radio');

    radios.forEach(function(radio) {
        radio.addEventListener('change', function() {
            
            // Desmarcar input
            radios.forEach(function(r) {
                r.checked = false;
            });
            // Marcar input
            this.checked = true;
        });
    });
});
