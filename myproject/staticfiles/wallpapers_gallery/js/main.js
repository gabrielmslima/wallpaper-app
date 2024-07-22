document.addEventListener('DOMContentLoaded', function () {
    const images = document.querySelectorAll('.gallery img');
    images.forEach(function (img) {
      img.addEventListener('click', function () {
        alert('Image clicked: ' + img.alt);
      });
    });
  });