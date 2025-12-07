
function myJS() {
    alert("js function called");
}

document.addEventListener("DOMContentLoaded", () => {

    // COLLAPSIBLE SECTIONS WITH SMOOTH SLIDE
    const sections = document.querySelectorAll(".collapsible-section");

    sections.forEach(section => {
        const btn = section.querySelector(".collapsible-btn");
        const content = section.querySelector(".collapsible-content");
        if (!content) return;

        // Collapse by default
        content.style.height = "0px";
        content.style.overflow = "hidden";

        btn.addEventListener("click", () => {
            const isOpen = section.classList.toggle("open");

            if (isOpen) {
                // Expand to fit content naturally
                const fullHeight = content.scrollHeight;
                content.style.height = fullHeight + "px";
            } else {
                content.style.height = "0px";
            }

            // If it's a main section, toggle all sub-sections
            const isMainSection = section.parentElement.classList.contains("collapsible-wrapper");
            if (isMainSection) {
                const subSections = content.querySelectorAll(".collapsible-section");
                subSections.forEach(sub => {
                    const subContent = sub.querySelector(".collapsible-content");
                    if (subContent) {
                        const openState = isOpen;
                        sub.classList.toggle("open", openState);
                        subContent.style.height = openState ? subContent.scrollHeight + "px" : "0px";
                    }
                });
            }
        });

        // Ensure that when content transitions end, set height to auto for flexibility
        content.addEventListener("transitionend", () => {
            if (section.classList.contains("open")) {
                content.style.height = "auto"; // allow further nested expansions without clipping
            }
        });
    });

    // TABLE OF CONTENTS
    const tocList = document.querySelector(".sidebar-inner .toc #toc-list"); // strictly inside sidebar

    if (tocList) {
        const headers = document.querySelectorAll(".collapsible-section > .collapsible-btn");
        headers.forEach(header => {
            const text = header.textContent.trim();
            const id = header.parentElement.id || text.toLowerCase().replace(/[^a-z0-9]+/g, "-");
            header.parentElement.id = id;

            const li = document.createElement("li");
            li.innerHTML = `<a href="#${id}">${text}</a>`;
            tocList.appendChild(li);
        });
    }

});



/* Créer effet de mouvement sur les layers de l'image de fond */
/*
document.addEventListener("scroll", () => {
    document.documentElement.style.setProperty("--scrollY", window.scrollY);
});*/

