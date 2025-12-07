
function myJS() {
    alert("js function called");
}

document.addEventListener("DOMContentLoaded", () => {

    const sections = document.querySelectorAll(".collapsible-section");

    sections.forEach(section => {
        const btn = section.querySelector(".collapsible-btn");
        const content = section.querySelector(".collapsible-content");

        if (!content) return;

        // Start collapsed
        content.style.maxHeight = "0px";
        content.style.overflow = "hidden";
        content.style.transition = "max-height 0.4s ease";

        btn.addEventListener("click", () => {
            const isOpen = section.classList.toggle("open");

            if (isOpen) {
                content.style.maxHeight = content.scrollHeight + "px";
            } else {
                content.style.maxHeight = "0px";
            }
        });
    });

});



/* Créer effet de mouvement sur les layers de l'image de fond */
/*
document.addEventListener("scroll", () => {
    document.documentElement.style.setProperty("--scrollY", window.scrollY);
});*/

