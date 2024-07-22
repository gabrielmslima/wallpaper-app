document.addEventListener('DOMContentLoaded', function () {
    const images = document.querySelectorAll('.gallery img');
    images.forEach(function (img) {
        img.addEventListener('click', function () {
            window.open(img.src, '_blank');
        });
    });
});