/* ───────────────────────────────────────────────────────────────────────────
   Friends-only gate (soft password).
   NOTE: this is light social gating, not real security — the page content is
   still inside the downloaded HTML. It keeps out random/casual visitors, which
   is the "just for friends" goal. Don't reuse this password for anything important.
   To change the password: base64-encode the new word and replace the token below
   (e.g. in a browser console: btoa('newword')).
   ─────────────────────────────────────────────────────────────────────────── */
(function () {
  var KEY = 'claire_friends_unlocked';
  if (localStorage.getItem(KEY) === 'yes') return;          // already let in

  var PW = atob('cHVwcHk=');                                // the password
  // hide the page until they're in (runs in <head>, before first paint)
  document.documentElement.style.visibility = 'hidden';

  function build() {
    var css = document.createElement('style');
    css.textContent =
      '#friend-gate{position:fixed;inset:0;z-index:99999;display:flex;align-items:center;' +
      'justify-content:center;background:linear-gradient(160deg,#f4f9ff,#cfe8ff);' +
      "font-family:'Nunito',system-ui,sans-serif}" +
      '#friend-gate .box{background:#fff;border-radius:22px;box-shadow:0 10px 30px rgba(43,108,176,.18);' +
      'padding:30px 26px;max-width:340px;width:88%;text-align:center}' +
      "#friend-gate h2{font-family:'Fredoka','Nunito',sans-serif;color:#1f5290;margin:0 0 6px;font-size:1.5rem}" +
      '#friend-gate p{color:#4a6585;font-weight:600;margin:0 0 16px}' +
      '#friend-gate input{width:100%;box-sizing:border-box;padding:12px 14px;border:2px solid #cfe8ff;' +
      'border-radius:12px;font-size:1rem;font-family:inherit;text-align:center}' +
      "#friend-gate button{width:100%;margin-top:10px;padding:12px;border:0;border-radius:12px;" +
      "background:#2b6cb0;color:#fff;font-weight:800;font-family:'Fredoka','Nunito',sans-serif;" +
      'font-size:1rem;cursor:pointer}' +
      '#friend-gate button:hover{background:#1f5290}' +
      '#friend-gate .err{color:#c0466b;font-weight:700;font-size:.85rem;min-height:1.1em;margin-top:8px}';
    document.documentElement.appendChild(css);

    var g = document.createElement('div');
    g.id = 'friend-gate';
    g.innerHTML =
      '<div class="box">' +
      '<h2>Friends only 🐾</h2>' +
      "<p>This bit's just for people I actually know. Password?</p>" +
      '<input id="fg-in" type="password" autocomplete="off" placeholder="password" aria-label="password">' +
      '<button id="fg-go">Let me in</button>' +
      '<div class="err" id="fg-err"></div>' +
      '</div>';
    document.body.appendChild(g);
    document.body.style.overflow = 'hidden';
    document.documentElement.style.visibility = 'visible';  // reveal (overlay covers content)

    var inp = g.querySelector('#fg-in');
    var err = g.querySelector('#fg-err');
    function tryit() {
      if (inp.value.trim().toLowerCase() === PW) {
        localStorage.setItem(KEY, 'yes');
        g.remove();
        document.body.style.overflow = '';
      } else {
        err.textContent = 'Nope. Try again.';
        inp.value = '';
        inp.focus();
      }
    }
    g.querySelector('#fg-go').onclick = tryit;
    inp.addEventListener('keydown', function (e) { if (e.key === 'Enter') tryit(); });
    inp.focus();
  }

  if (document.readyState !== 'loading') build();
  else document.addEventListener('DOMContentLoaded', build);
})();
