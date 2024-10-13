// Fonction pour jouer le son d'orage après un délai aléatoire
function playThunderSound() {
  const thunderSound = document.getElementById('thunder-sound');

  // Réduire le volume à 50%
  thunderSound.volume = 0.5;

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
