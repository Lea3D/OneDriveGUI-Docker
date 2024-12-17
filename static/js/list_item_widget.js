document.addEventListener("DOMContentLoaded", () => {
    const progressBar = document.querySelector(".progress");
    const updateButton = document.querySelector(".tool-button");

    updateButton.addEventListener("click", () => {
        const newWidth = Math.min(100, Math.random() * 100).toFixed(2);
        progressBar.style.width = `${newWidth}%`;
        console.log(`Progress updated to: ${newWidth}%`);
    });
});
