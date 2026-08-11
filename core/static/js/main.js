document.addEventListener("DOMContentLoaded", () => {

    // ==========================
    // Sticky Navbar
    // ==========================

    const navbar = document.querySelector(".navbar");

    window.addEventListener("scroll", () => {
        if (window.scrollY > 80) {
            navbar.classList.add("scrolled");
        } else {
            navbar.classList.remove("scrolled");
        }
    });

    // ==========================
    // Mobile Menu
    // ==========================

    const menuBtn = document.querySelector(".mobile-menu");
    const navMenu = document.querySelector(".nav-menu");

    if (menuBtn && navMenu) {

        menuBtn.addEventListener("click", () => {
            navMenu.classList.toggle("active");
            menuBtn.classList.toggle("active");
        });

    }

    // ==========================
    // Animated Counters
    // ==========================

    const counters = document.querySelectorAll(".stat-number");

    const animateCounter = (counter) => {

        const target = parseInt(counter.dataset.target);

        let current = 0;

        const increment = Math.ceil(target / 100);

        const timer = setInterval(() => {

            current += increment;

            if (current >= target) {

                current = target;

                clearInterval(timer);

            }

            counter.textContent = current;

        }, 20);

    };

    const observer = new IntersectionObserver((entries) => {

        entries.forEach(entry => {

            if (entry.isIntersecting) {

                animateCounter(entry.target);

                observer.unobserve(entry.target);

            }

        });

    }, { threshold: 0.5 });

    counters.forEach(counter => observer.observe(counter));

});

// ==========================
// Scroll Reveal
// ==========================

const reveals = document.querySelectorAll(".reveal");

const revealObserver = new IntersectionObserver((entries) => {

    entries.forEach(entry => {

        if (entry.isIntersecting) {
            entry.target.classList.add("active");
            revealObserver.unobserve(entry.target);
        }

    });

}, { threshold: 0.15 });

reveals.forEach(section => revealObserver.observe(section));

window.addEventListener("scroll", () => {
    const header = document.querySelector("header");
    header.classList.toggle("scrolled", window.scrollY > 50);
});

const counters = document.querySelectorAll(".stat-number");

const animateCounter = counter => {
    const target = +counter.dataset.target;
    let count = 0;
    const step = Math.ceil(target / 80);

    const timer = setInterval(() => {
        count += step;

        if (count >= target) {
            counter.textContent = target;
            clearInterval(timer);
        } else {
            counter.textContent = count;
        }
    }, 20);
};

const stats = document.querySelector(".stats-band");

if (stats) {
    const observer = new IntersectionObserver(entries => {
        if (entries[0].isIntersecting) {
            counters.forEach(animateCounter);
            observer.disconnect();
        }
    });

    observer.observe(stats);
}

const progress = document.querySelector(".progress-bar");

window.addEventListener("scroll", () => {
    const total = document.documentElement.scrollHeight - window.innerHeight;
    const percent = (window.scrollY / total) * 100;
    progress.style.width = percent + "%";
});

const backToTop = document.getElementById("backToTop");

window.addEventListener("scroll", () => {
    backToTop.classList.toggle("show", window.scrollY > 300);
});

backToTop.addEventListener("click", () => {
    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
});

const testimonials = document.querySelectorAll(".testimonial");
let current = 0;

if (testimonials.length) {
    setInterval(() => {
        testimonials[current].classList.remove("active");
        current = (current + 1) % testimonials.length;
        testimonials[current].classList.add("active");
    }, 5000);
}