// --- ส่วนที่ 1: การวนลูปแสดงภาพผลงาน ---
const totalTattoos = 24; 
const galleryContainer = document.getElementById('portfolio-gallery');

if (galleryContainer) {
    let htmlContent = '';
    for (let i = 1; i <= totalTattoos; i++) {
        let fileName = i.toString().padStart(3, '0');
        htmlContent += `
            <div class="portfolio-item">
                <img src="imgs/tattoo${fileName}.jpg" alt="work tattoo ${fileName}" loading="lazy">
            </div>
        `;
    }
    galleryContainer.innerHTML = htmlContent;
}

// --- ส่วนที่ 2: จัดการ Mobile Menu (Hamburger) ---
const mobileMenu = document.getElementById('mobile-menu');
const navLinks = document.querySelector('.nav-links');

mobileMenu.addEventListener('click', () => {
    navLinks.classList.toggle('active');
});

document.querySelectorAll('.nav-links a').forEach(link => {
    link.addEventListener('click', () => {
        navLinks.classList.remove('active');
    });
});