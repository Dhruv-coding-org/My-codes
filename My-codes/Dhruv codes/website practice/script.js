// Function to generate a random color
function getRandomColor() {
  const letters = '0123456789ABCDEF';
  let color = '#';
  for (let i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}

// Select all box elements
const boxes = document.querySelectorAll('.box');

boxes.forEach(box => {
  box.addEventListener('click', () => {
    // Change text
    box.textContent = "Color Changed";

    // Change to random color
    box.style.backgroundColor = getRandomColor();

    // Add animation class
    box.classList.add('animated');

    // Remove animation class after 300ms to allow re-animation on next click
    setTimeout(() => {
      box.classList.remove('animated');
    }, 300);
  });
});
