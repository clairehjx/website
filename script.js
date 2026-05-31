/* ============================================================
   Claire's Website — a tiny bit of JavaScript to bring it alive
   ============================================================ */

// 1) Show the current year in the footer (so it's never out of date).
document.getElementById('year').textContent = new Date().getFullYear();

// 2) Gently fade sections in as you scroll down the page.
//    This uses an IntersectionObserver — it "watches" each element and
//    tells us the moment it scrolls into view, so we can add a class.
const revealItems = document.querySelectorAll('.reveal');

if ('IntersectionObserver' in window) {
  const watcher = new IntersectionObserver((entries) => {
    for (const entry of entries) {
      if (entry.isIntersecting) {
        entry.target.classList.add('show');
        watcher.unobserve(entry.target);   // only animate once
      }
    }
  }, { threshold: 0.15 });

  revealItems.forEach((el) => watcher.observe(el));
} else {
  // If the browser is very old, just show everything.
  revealItems.forEach((el) => el.classList.add('show'));
}
