const youtubeImage = document.querySelector('.youtube-image'); // Replace '.youtube-image' with the actual selector for your YouTube image

youtubeImage.addEventListener('mouseover', () => {
    youtubeImage.style.boxShadow = '0 0 20px rgba(255, 0, 0, 0.7)'; // Adjust the shadow properties as desired
    youtubeImage.style.transition = 'box-shadow 0.3s ease-in-out'; // Add a smooth transition
});

youtubeImage.addEventListener('mouseout', () => {
    youtubeImage.style.boxShadow = 'none'; // Remove the shadow when the mouse leaves
});