document.getElementById('max1').addEventListener('click', function() {
    var input = document.getElementById('bol1');
    input.value = parseInt(input.value) + 1;
  });
  
  document.getElementById('min1').addEventListener('click', function() {
    var input = document.getElementById('bol1');
    if (parseInt(input.value) > 1) {
      input.value = parseInt(input.value) - 1;
    }
  });
  
  document.getElementById('max2').addEventListener('click', function() {
    var input = document.getElementById('bol2');
    input.value = parseInt(input.value) + 1;
  });
  
  document.getElementById('min2').addEventListener('click', function() {
    var input = document.getElementById('bol2');
    if (parseInt(input.value) > 1) {
      input.value = parseInt(input.value) - 1;
    }
  });
  
  function guardarYComprar() {
    localStorage.setItem('bol1', document.getElementById('bol1').value);
    localStorage.setItem('bol2', document.getElementById('bol2').value);
    window.location.href = 'compra.html';
  }