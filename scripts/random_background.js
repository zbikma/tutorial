
const keywords = ["nature", "city", "technology", "space", "mountains"];
// function to set the random background
function setRandomBackground() {
    const randomKeyword = keywords[Math.floor(math.random() * keywords.length)];
    // Unsplash API to get a random image based on the keyword
    const imageUrl = `https://source.unsplash.com/random/1920x1080?${randomKeyword}`;

    // Set the random image as the background
    document.body.style.backgroundImage = `url('${imageUrl}')`;
}
window.onload = setRandomBackground;