// Liste des sons d'orage
const thunderSounds = [
    "{{ url_for('static', filename='loud-thunder-192165.mp3') }}",
    "{{ url_for('static', filename='thunder.mp3') }}",
    "{{ url_for('static', filename='rain-and-thunder-sfx-12820.mp3') }}"
];

// Fonction pour jouer un son d'orage aléatoire
function playThunderSound() {
    const randomSound = thunderSounds[Math.floor(Math.random() * thunderSounds.length)];
    const thunderSound = new Audio(randomSound);

    // Générer un délai aléatoire entre 20 et 60 secondes (20000 à 60000 millisecondes)
    const randomDelay = Math.random() * (60000 - 20000) + 20000;

    // Jouer le son après le délai
    setTimeout(function() {
        thunderSound.play();
        // Après avoir joué le son, rejoue de manière aléatoire
        playThunderSound();
    }, randomDelay);
}

// Lancer la première lecture du son quand la page est complètement chargée
window.addEventListener('load', function() {
    playThunderSound();
});
