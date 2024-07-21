const repoOwner = 'gabrielmslima';
const repoName = 'wallpapers';
const folderPath = 'images';

async function fetchImages() {
  const url = `https://api.github.com/repos/${repoOwner}/${repoName}/contents/${folderPath}`;
  try {
    const response = await fetch(url);
    const data = await response.json();
    const imagesContainer = document.getElementById('wallpapers-container');

    data.forEach(file => {
      if (file.type === 'file' && (file.name.endsWith('.jpg') || file.name.endsWith('.png'))) {
        const img = document.createElement('img');
        img.src = file.download_url;
        img.alt = file.name;
        imagesContainer.appendChild(img);
      }
    });
  } catch (error) {
    console.error('Error fetching images:', error);
  }
}

fetchImages();