document.addEventListener('DOMContentLoaded', () => {
    initTheme();
    initNavbar();
    initSmoothScroll();
    initCharCounter();
    initPredictForm();
    initExampleButtons();
    initAutoFocus();
});

/* ===== Dark Mode ===== */
function initTheme() {
    const toggle = document.getElementById('themeToggle');
    const icon = document.getElementById('themeIcon');
    const saved = localStorage.getItem('theme') || 'light';

    document.documentElement.setAttribute('data-theme', saved);
    updateThemeIcon(icon, saved);

    toggle?.addEventListener('click', () => {
        const current = document.documentElement.getAttribute('data-theme');
        const next = current === 'dark' ? 'light' : 'dark';
        document.documentElement.setAttribute('data-theme', next);
        localStorage.setItem('theme', next);
        updateThemeIcon(icon, next);
    });
}

function updateThemeIcon(icon, theme) {
    if (!icon) return;
    icon.className = theme === 'dark' ? 'fas fa-sun' : 'fas fa-moon';
}

/* ===== Navbar Scroll Effect ===== */
function initNavbar() {
    const nav = document.getElementById('mainNav');
    if (!nav) return;

    window.addEventListener('scroll', () => {
        nav.classList.toggle('scrolled', window.scrollY > 50);
    });
}

/* ===== Smooth Scrolling ===== */
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', (e) => {
            const targetId = anchor.getAttribute('href');
            if (targetId === '#') return;

            const target = document.querySelector(targetId);
            if (target) {
                e.preventDefault();
                const offset = 80;
                const top = target.getBoundingClientRect().top + window.scrollY - offset;
                window.scrollTo({ top, behavior: 'smooth' });
            }
        });
    });
}

/* ===== Character Counter ===== */
function initCharCounter() {
    const textarea = document.getElementById('emailText');
    const counter = document.getElementById('charCount');
    if (!textarea || !counter) return;

    const update = () => {
        counter.textContent = textarea.value.length;
    };

    textarea.addEventListener('input', update);
    update();
}

/* ===== Prediction Form Loading ===== */
function initPredictForm() {
    const form = document.getElementById('predictForm');
    const btn = document.getElementById('predictBtn');
    const spinner = document.getElementById('loadingSpinner');

    form?.addEventListener('submit', (e) => {
        const text = document.getElementById('emailText')?.value.trim();
        if (!text) {
            e.preventDefault();
            showToast('Please enter an email.', 'error');
            return;
        }

        btn?.classList.add('d-none');
        spinner?.classList.remove('d-none');
    });
}

/* ===== Example Emails ===== */
const EXAMPLE_SPAM = `URGENT! You have won a 1 week FREE membership in our £100,000 Prize Jackpot! Txt the word: CLAIM to No: 81010 T&C www.dbuk.net LCCLTD POBOX 4403LDNW1A7RW18`;

const EXAMPLE_HAM = `Hey! Are we still meeting for lunch tomorrow at 12:30? Let me know if the time works for you. I'll be near the downtown office.`;

function initExampleButtons() {
    const textarea = document.getElementById('emailText');
    const spamBtn = document.getElementById('exampleSpam');
    const hamBtn = document.getElementById('exampleHam');

    spamBtn?.addEventListener('click', () => {
        if (textarea) {
            textarea.value = EXAMPLE_SPAM;
            textarea.dispatchEvent(new Event('input'));
            showToast('Example spam email loaded!', 'info');
        }
    });

    hamBtn?.addEventListener('click', () => {
        if (textarea) {
            textarea.value = EXAMPLE_HAM;
            textarea.dispatchEvent(new Event('input'));
            showToast('Example ham email loaded!', 'info');
        }
    });
}

/* ===== Auto Focus ===== */
function initAutoFocus() {
    const textarea = document.getElementById('emailText');
    if (textarea && window.location.hash === '#predict') {
        setTimeout(() => textarea.focus(), 300);
    }
}

/* ===== Toast Notifications ===== */
function showToast(message, type = 'info') {
    const existing = document.querySelector('.custom-toast');
    existing?.remove();

    const toast = document.createElement('div');
    toast.className = `custom-toast ${type}`;
    toast.textContent = message;
    document.body.appendChild(toast);

    setTimeout(() => toast.remove(), 3000);
}
