  // Toggle dark mode
    const toggleButton = document.getElementById('toggle-mode');
    toggleButton.addEventListener('click', function() {
      document.body.classList.toggle('dark');
      this.textContent = document.body.classList.contains('dark') ? '☀️ Light Mode' : '🌗 Dark Mode';
    });

    // Check if image loaded successfully
    const profileImg = document.querySelector('.Profile-img');
    if (profileImg.complete && profileImg.naturalHeight !== 0) {
      profileImg.parentElement.classList.remove('no-image');
    }