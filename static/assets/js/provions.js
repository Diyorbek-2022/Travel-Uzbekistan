window.addEventListener('scroll', function() {
    const hero = document.getElementById('hero');
    const img = hero.querySelector('img');
    const scrollPosition = window.scrollY;

    // Adjust the scale and filter based on scroll position
    const scaleValue = 1 + scrollPosition / 1000; // Adjust the zoom level
    const darkenValue = Math.min(1, scrollPosition / 500); // Darken effect

    img.style.transform = `scale(${scaleValue})`;
    img.style.filter = `brightness(${1 - darkenValue})`; // Darkening the image
});