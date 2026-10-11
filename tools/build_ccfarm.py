"""Generates the ccfarm pages of Claire's website from one shared template."""
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

PAGES = [
    ("ccfarm.html", "Overview"),
    ("ccfarm-world.html", "The game"),
    ("ccfarm-workshop.html", "The workshop"),
    ("ccfarm-workflow.html", "How it's built"),
    ("ccfarm-updates.html", "Updates"),
]


def shot(src, alt, cap, cls=""):
    return (f'<figure class="shot {cls} reveal"><img src="img/ccfarm/{src}" alt="{alt}" loading="lazy" '
            f'onerror="this.closest(\'figure\').remove()"><figcaption>{cap}</figcaption></figure>')


def clip(src, cap, cls="", poster=""):
    p = f' poster="img/ccfarm/{poster}"' if poster else ""
    return (f'<figure class="clip {cls} reveal"><video src="img/ccfarm/{src}"{p} autoplay muted loop playsinline '
            f'preload="metadata" onerror="this.closest(\'figure\').remove()"></video><figcaption>{cap}</figcaption></figure>')


def step(n, title, file, what, extra="", why=""):
    w = f'<div class="why">{why}</div>' if why else ""
    return f'''<div class="wf-step reveal"><span class="num">{n}</span><div class="wf-card">
            <h3>{title}</h3>
            <span class="wf-file">{file}</span>
            <p class="wf-what">{what}</p>
            {extra}
            {w}
          </div></div>'''


def page(fname, title, desc, eyebrow, h1, tagline, body, prev=None, nxt=None):
    tabs = "\n".join(
        f'        <a href="{f}"{" aria-current=\"page\"" if f == fname else ""}>{label}</a>' for f, label in PAGES)
    nav = ""
    if prev or nxt:
        a = f'<a class="btn btn-ghost" href="{prev[0]}">← {prev[1]}</a>' if prev else "<span></span>"
        b = f'<a class="btn btn-primary" href="{nxt[0]}">{nxt[1]} →</a>' if nxt else ""
        nav = f'<div class="next-page">{a}{b}</div>'
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <!-- Friends-only soft password gate (runs before paint) -->
  <script src="gate.js"></script>
  <title>{title} · Claire</title>
  <meta name="description" content="{desc}">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&family=Nunito:wght@600;700;800&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="ccfarm.css">
  <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Ccircle cx='16' cy='16' r='13' fill='%234a90d9'/%3E%3Ccircle cx='11' cy='12' r='4' fill='%23cfe8ff'/%3E%3C/svg%3E">
</head>
<body>

  <!-- ============ NAV ============ -->
  <nav class="nav">
    <div class="wrap">
      <a class="brand" href="index.html#top"><span class="dot"></span>Claire</a>
      <div class="nav-links">
        <a href="index.html#ccfarm">← Back to my site</a>
      </div>
    </div>
  </nav>

  <!-- ============ HERO ============ -->
  <header class="hero wf-hero" id="top">
    <span class="blob b1"></span>
    <span class="blob b3"></span>
    <div class="wrap">
      <span class="eyebrow">{eyebrow}</span>
      <h1>{h1}</h1>
      <p class="tagline">{tagline}</p>
      <div class="cc-tabs">
{tabs}
      </div>
    </div>
  </header>

  <main>
    <section>
      <div class="wrap">
{body}
        {nav}
      </div>
    </section>
  </main>

  <!-- ============ FOOTER ============ -->
  <footer class="footer">
    <div class="wrap">
      <p>Made by <strong>Claire</strong> — too much blue watercolour and one perpetually cheerful AI.</p>
      <p><a href="https://github.com/clairehjx" target="_blank" rel="noopener">github.com/clairehjx</a></p>
      <p class="small">© <span id="year"></span> Claire · still building, still learning.</p>
    </div>
  </footer>

  <script src="script.js"></script>
</body>
</html>
'''
    open(os.path.join(OUT, fname), "w").write(html)


# ---------------------------------------------------------------- Overview
page("ccfarm.html", "ccfarm",
     "ccfarm: The Secret of Shaymin's Glade. Claire's biggest project, a 3D Pokémon farm game in Godot with Claude-powered shopkeepers.",
     "My biggest project", "ccfarm:<br>The Secret of Shaymin's Glade",
     "A cozy 3D farm game my sister and I play together on our phones. Pokémon do the farm work, the shopkeepers talk back (thanks, Claude), and somewhere in the forest there's a glade the whole town forgot about. I'm the designer. It's taken over my life a bit.",
     f'''
        {clip("gameplay-landscape.mp4", "Sideways mode on a phone: walking down the main street to the furniture workshop.", poster="landscape-farm.png")}
        {clip("gameplay.mp4", "The original portrait view: walk, harvest, get followed by Umbreon.", "phone")}

        <div class="cc-stats reveal">
          <div class="cc-stat"><b>2</b><span>players on one shared farm</span></div>
          <div class="cc-stat"><b>3</b><span>shopkeepers you can actually talk to</span></div>
          <div class="cc-stat"><b>4</b><span>rooms per house (I asked for more space)</span></div>
          <div class="cc-stat"><b>3</b><span>holidays, each a chapter of the story</span></div>
        </div>

        <div class="card legend reveal">
          <h3>The pitch, in one breath</h3>
          <p>You and your friends share one farm at the edge of a forest. You plant crops, look after Miltank, Wooloo and Combee, turn it all into food and furniture, decorate your house, and chat with the villagers in town, who are powered by Claude, so you can type literally anything at them. Meanwhile the Pokémon keep wandering off towards the same bit of forest. That's not a bug. That's the story.</p>
          <div class="chips">
            <span class="chip">Godot 4</span><span class="chip">3D</span><span class="chip">Multiplayer</span><span class="chip">Claude NPCs</span><span class="chip">Blender</span><span class="chip">Android</span>
          </div>
        </div>

        <div class="section-head reveal">
          <span class="kicker">Pick a page</span>
          <h2>There's a lot. Sorry.</h2>
        </div>
        <div class="cc-pages">
          <a class="cc-page reveal" href="ccfarm-world.html"><img src="img/ccfarm/farm-overview.png" alt="" loading="lazy"><div><h3>The game</h3><p>The farm, the Pokémon, the houses, the holidays and the glade.</p></div></a>
          <a class="cc-page reveal" href="ccfarm-workshop.html"><img src="img/ccfarm/workshop-inside.png" alt="" loading="lazy" onerror="this.src='img/ccfarm/room-decorate.png'"><div><h3>The workshop</h3><p>Describe a piece of furniture and the game builds it. In 3D. For real.</p></div></a>
          <a class="cc-page reveal" href="ccfarm-workflow.html"><img src="img/ccfarm/shopkeeper-chat.png" alt="" loading="lazy" style="object-position:top"><div><h3>How it's built</h3><p>ChatGPT, Claude Code, Godot, Blender, an iMac and a box in the cupboard.</p></div></a>
          <a class="cc-page reveal" href="ccfarm-updates.html"><img src="img/ccfarm/christmas.png" alt="" loading="lazy"><div><h3>Updates</h3><p>What's changed, roughly by the day, because it changes daily.</p></div></a>
        </div>

        <div class="card wf-note reveal">
          <h3>Where's the code?</h3>
          <p>Closed source for now, because it's nowhere near done and I'd rather not have strangers judging my half-built barn. Once it's finished, I plan to open source it on <a href="https://github.com/clairehjx" target="_blank" rel="noopener">my GitHub</a>.</p>
        </div>''',
     nxt=("ccfarm-world.html", "The game"))

# ---------------------------------------------------------------- The game
page("ccfarm-world.html", "ccfarm: the game",
     "What you do in ccfarm: the shared farm, the Pokémon, houses and decorating, the holidays and the story of Shaymin's Glade.",
     "ccfarm · the game", "What you actually<br>do all day",
     "No winning, no losing. Just very organised busywork, a lot of decorating, and a mystery the Pokémon refuse to explain because Pokémon don't talk. Rules are rules.",
     f'''
        {shot("farm-overview.png", "The farm: crop plots, the windmill, the pond and a few Pokémon", "The farm. Yes, the world curves like a rolling log. On purpose.")}

        <div class="card legend reveal">
          <h3>A normal day on the farm</h3>
          <ul class="play-loop">
            <li>Pick who's playing (Claire or Chloe) and land on the shared farm.</li>
            <li>Plant crops. They grow in about 5 minutes, because nobody has time for real farming.</li>
            <li>Collect milk, wool, honey and eggs from the farm Pokémon.</li>
            <li>Turn it all into food and drinks at the work bench. Your partner Pokémon helps with the chores.</li>
            <li>Sell it, then spend it in town: the ramen shop, the tea shop and the furniture workshop.</li>
            <li>Decorate. Then decorate some more.</li>
            <li>Notice the Pokémon acting strange near the forest. Follow them. No spoilers.</li>
          </ul>
        </div>

        <div class="wf-steps">
          {step(1, "One farm, two phones", "Claire · Chloe · a shared world",
                "We each get our own wallet, our own bag and our own house, but the farm is shared. If Chloe harvests the wheat, it's gone on my screen too (rude, but correct). Bedtime only skips to morning when everyone's actually in bed.",
                shot("landscape-farm.png", "The sideways phone layout", "Sideways mode: the farm fills the whole screen and the buttons float over it."))}

          {step(2, "Pokémon doing the actual work", "Miltank · Wooloo · Combee · Torchic · Gogoat · Oinkologne",
                "Every farm Pokémon makes something, idles, gets fed, repeats. Each one has its own morning greeting and a signature antic. My partner Umbreon follows me round, fetches things and runs workshop chores. Chloe's is Sylveon. Its rings glow brighter at night now, because I asked.",
                shot("pokemon-farm.png", "Claire and Umbreon in the pasture with Miltank, Wooloo and Gogoat", "Me, Umbreon, and the staff. Nobody is working.")
                + shot("backyard-pokemon.png", "A Pokémon roaming a backyard", "Mimikyu and an Eevee live in our backyards. Mimikyu was rebuilt from MY drawing."))}

          {step(3, "Shopkeepers that actually talk", "Claude · panda (ramen) · turtle (tea) · bear (workshop)",
                "The shopkeepers are animal villagers. Type anything to them and Claude writes their reply, in character, with a mood attached, so they pull a face and do a little gesture to match. The ramen and tea stalls are proper shopfronts on the main street now, with the owners behind the counters.",
                shot("shopfronts.png", "The ramen and tea shopfronts on the main street", "The shopfronts. Ramen on one side, tea on the other, my wallet in the middle.")
                + shot("shopkeeper-chat.png", "Chatting with a shopkeeper on the phone", "Top half: the game. Bottom half: me being nosy.", "phone"),
                "<b>Rule:</b> only humans and villagers talk. Pokémon get thought bubbles at most. I will not be moved on this.")}

          {step(4, "Houses (with FOUR rooms now)", "decorate mode · lanterns · the mirror",
                "Everyone has a house to decorate. It started as one room, then I asked for more space, so now there's a side room, a mirrored west room and a north room behind the back wall. In decorate mode the walls drop to half height so you can carry furniture from room to room. You can sit on the chairs and lie on the beds, and Umbreon comes inside and curls up in its pet bed. Each room has a lantern that lights up at night. The mirror changes your outfit, hair style and colours.",
                shot("house-rooms-night.png", "Inside a house at night with lanterns lit", "Night mode. Cosy, as instructed.")
                + '<div class="shot-row">'
                + shot("room-decorate.png", "Decorating a bedroom", "My room. Tasteful.")
                + shot("avatar-wardrobe.png", "Avatar wardrobe and outfits", "The wardrobe lineup.")
                + "</div>")}

          {step(5, "Real holidays, real story", "Halloween · Christmas · Chinese New Year",
                "Seasons follow the real calendar. At Christmas the snow ramps in over three days, every shop gets lights, and Papa leaves a gift in each person's stocking. At Chinese New Year, Gracidea flowers bloom by the old glade path, and you can finally cook the Special Ramen from the old family recipe. Who it's for, I'm not saying. Play it.",
                '<div class="shot-row">'
                + shot("christmas.png", "The farm at Christmas dusk", "Christmas at dusk. Yes, the sky is pink. It's a choice.")
                + shot("shops-christmas.png", "The shopfronts with Christmas lights", "The shops, festively lit.")
                + shot("christmas-indoors.png", "The Christmas tree indoors", "The tree and the stocking.")
                + shot("chinese-new-year.png", "Gracidea flowers by the old glade path at Chinese New Year", "Chinese New Year: Gracidea by the old path. Suspicious.")
                + shot("glade.png", "A forest clearing", "The forest. The glade is somewhere past here.")
                + "</div>",
                "<b>Why real dates:</b> Christmas in the game is Christmas in real life. Much less confusing than a pretend calendar.")}
        </div>''',
     prev=("ccfarm.html", "Overview"), nxt=("ccfarm-workshop.html", "The workshop"))

# ---------------------------------------------------------------- The workshop
page("ccfarm-workshop.html", "ccfarm: the workshop",
     "How ccfarm's furniture workshop works: describe a piece to the shop owner, Claude designs it, Blender builds it, and it goes in the catalogue.",
     "ccfarm · the workshop", "Describe it.<br>They'll build it.",
     "My favourite new bit. Tell the workshop owner what furniture you want, in normal words, and a few seconds later there's an actual 3D piece of it spinning on a turntable. It still feels slightly illegal.",
     f'''
        {shot("furniture-workshop.png", "The furniture workshop on the main street", "The workshop, at the end of the main street. The craftsman is waving. Wave back.")}

        <div class="card legend reveal">
          <h3>What happens when you ask for a "cloud-shaped sofa"</h3>
          <p>The bear who used to run the upgrade stall now has a whole workshop, with two craftsmen hammering and sawing at the back (they look up and wave when you walk past, which is very polite of them).</p>
        </div>

        <div class="wf-steps">
          {step(1, "You ask the owner", "chat · Claude",
                "You just describe it in the chat. He's a villager, so Claude is doing his talking, and it decides your request counts as a commission.",
                shot("commission-chat.png", "The workshop owner's chat with a commissioned piece on a turntable", "The piece on its turntable, with a price. Drag to spin it.", "phone"))}

          {step(2, "Claude turns words into a recipe", "furniture designer prompt",
                "A second Claude, the furniture designer, writes a recipe for the piece: which boxes, cylinders and spheres go where, how big, which colours. Basically LEGO instructions.")}

          {step(3, "Blender builds it on the iMac", "Farm Host → iMac workshop → Blender",
                "The Farm Host on our NAS passes the recipe to the iMac, where Blender builds a real 3D model from it. If the iMac is off, the owner says his craftsmen are busy and only sells what's in stock. Very realistic, honestly.")}

          {step(4, "Buy it (or don't)", "Buy · No thanks",
                "You get the price and a Buy button. If you buy it, it goes into your bag, and it joins the workshop catalogue so other people can buy one too. Custom pieces are half price now, because I said the first prices were daylight robbery.",
                shot("commissioned-pieces.png", "A lineup of commissioned furniture pieces", "Some things we've commissioned. No regrets."))}

          {step(5, "The catalogue", "on the table inside the workshop",
                "Inside the workshop there's a catalogue on the table: one piece at a time on a turntable, Previous, Next, Buy. The roof goes see-through while you're inside so you can actually see.",
                shot("workshop-inside.png", "Inside the workshop with the catalogue and the craftsmen", "Inside. The craftsmen never stop. Union is looking into it."))}
        </div>

        <div class="card wf-note reveal">
          <h3>Maker Studio (the grown-up version)</h3>
          <p>There's also a separate app on the iMac called <strong>Maker Studio</strong> with the same trick for bigger jobs: a <strong>Furniture Maker</strong> and a <strong>creature maker</strong>. You describe it, Claude designs it, Blender builds it, it shows up on a turntable, and you press Save. That's where Mittens and Star came from.</p>
          {shot("maker-studio.png", "Maker Studio's Furniture Maker", "Maker Studio.")}
        </div>''',
     prev=("ccfarm-world.html", "The game"), nxt=("ccfarm-workflow.html", "How it's built"))

# ---------------------------------------------------------------- How it's built
page("ccfarm-workflow.html", "How ccfarm works",
     "Behind the scenes of ccfarm: brainstorming in ChatGPT, building with Claude Code, and how Godot, Blender, the iMac, the NAS and the phones fit together.",
     "ccfarm · how it's built", "How ccfarm<br>works",
     "I design it, my dad builds it with a LOT of help from Claude, and I file complaints. It's a system.",
     f'''
        <div class="card wf-note reveal" style="margin-top:0;margin-bottom:28px;">
          <h3>How it started: ChatGPT first, then Claude Code</h3>
          <p>Before there was a single line of code, I spent ages in <strong>ChatGPT</strong> just brainstorming: what the farm is, which Pokémon live on it, who the shopkeepers are, and the whole story about Shaymin's Glade (the forgotten stones, the holidays as clues, the Chinese New Year ending). ChatGPT is good for that bit. You throw half-ideas at it and it throws more back.</p>
          <p>Once the ideas were properly written down as design docs, the project moved to <strong>Claude Code</strong>, which actually builds things: it writes the code, runs the tests, renders screenshots to check its own work, and keeps a running list of questions for me (the designer, obviously) to answer. ChatGPT was the notebook. Claude Code is the workshop.</p>
        </div>

        <div class="card legend reveal">
          <h3>The pieces</h3>
          <div class="legend-grid">
            <div class="legend-item"><strong>Godot 4</strong><small>A real game engine. 3D, lighting, the works.</small></div>
            <div class="legend-item"><strong>Blender</strong><small>Builds every building, piece of furniture and Pokémon from code.</small></div>
            <div class="legend-item"><strong>Claude</strong><small>Writes the code, and does the villagers' talking.</small></div>
            <div class="legend-item"><strong>The NAS</strong><small>A box at home that runs the shared farm.</small></div>
            <div class="legend-item"><strong>Phones</strong><small>A Galaxy Z Flip, an S25 and an Xperia. Portrait or sideways.</small></div>
          </div>
        </div>

        <div class="card legend reveal">
          <h3>Who does what (the machines, not us)</h3>
          <p>Five things pass the work along, kind of like a relay race:</p>
          <ul class="play-loop">
            <li><strong>Claude Code</strong> runs on the <strong>iMac</strong>. It writes the game code, and it also writes <strong>Python scripts for Blender</strong>.</li>
            <li><strong>Blender</strong> runs those scripts and builds the 3D models (the cottages, workshops, furniture and the Pokémon) out of code. Nobody sculpts anything by hand, which is great, because neither of us can. It also builds the furniture people commission in the game, live.</li>
            <li><strong>Godot</strong> (also on the iMac) turns everything into the actual game. Claude Code runs Godot from the command line to test the game and take screenshots, so it can SEE whether the barn is upside down before I do.</li>
            <li>When a new version is ready, the iMac exports an Android app and uploads it to the <strong>NAS</strong> (the little always-on storage box at home). Our phones check the NAS and <strong>update themselves</strong>. It even waits until nobody's playing before it publishes, so nobody gets kicked out mid-harvest.</li>
            <li>The <strong>NAS</strong> also runs the game server that holds the shared farm, and a "Farm Host" that passes villager conversations to Claude and furniture orders to the iMac. It keeps daily backups too. Everything talks over <strong>Tailscale</strong>, a private network only our devices can join.</li>
          </ul>
          <p>Short version: Claude Code writes it on the iMac, Blender shapes it, Godot builds it, the NAS hosts it, and the phones play it.</p>
        </div>

        <div class="section-head reveal">
          <span class="kicker">The tricky bits</span>
          <h2>Stuff that was harder than it looks</h2>
        </div>

        <div class="wf-steps">
          {step(1, "Keeping two phones on one farm", "server · SQLite · Tailscale",
                "Both phones connect to the game server on the NAS, which keeps the ONE true copy of the farm. If a phone loses the connection, it doesn't quietly carry on by itself any more (that's how Chloe lost an afternoon of decorating, RIP). It keeps what you do, says it's rejoining, and sends it all over once it's back.",
                why="<b>Why:</b> if each phone kept its own farm, they'd disagree within about four seconds.")}

          {step(2, "Talking villagers", "Claude · moods · gestures",
                "When you type to a villager, the game sends their personality, what they know and your message to Claude. The reply comes back with words AND a mood, and the game checks it before showing it, so nobody goes off-script.")}

          {step(3, "Phones that turn sideways", "portrait · landscape",
                "The game started as portrait only (top half game, bottom half buttons). Now the S25, the Xperia and the Flip can play sideways too: the farm fills the screen and the buttons float over it, see-through. Even the gameplay recorder captures the whole sideways screen.",
                clip("gameplay-night.mp4", "Dusk into night: the street lamps and lanterns come on."))}

          {step(4, "The world is a log", "world curve",
                "The ground curves away from you like a rolling log (Animal Crossing does this) and wraps round at the edges. Looks lovely. Also bends everything, including furniture previews, which sank through their own turntables until that got fixed.")}
        </div>

        <div class="card wf-note reveal">
          <h3>The design / tech split</h3>
          <p>I write the <strong>design answers</strong> (what the milestones are, what each Pokémon's antic is, whether Mimikyu should be life-size — yes, obviously). The build then hands me back a list of <strong>designer questions</strong>, I answer them, and the next version shows up on my phone by itself. On 8 October I answered 23 in one go. It's basically a very slow group chat with a game engine.</p>
          <p><strong>Where's the code?</strong> It's closed source for now. Once it's finished, I plan to open source it on <a href="https://github.com/clairehjx" target="_blank" rel="noopener">my GitHub</a>.</p>
        </div>''',
     prev=("ccfarm-workshop.html", "The workshop"), nxt=("ccfarm-updates.html", "Updates"))

# ---------------------------------------------------------------- Updates
LOG = [
    ("9 Oct", "Phones that drop off the farm", "now rejoin instead of going off on their own, and tell you if Tailscale is off rather than just sulking."),
    ("8 Oct", "Four-room houses", "with a lantern in every room, lit at night."),
    ("8 Oct", "23 designer questions answered", "Shopfronts for the ramen and tea shops, Christmas stockings, Chinese New Year with Gracidea and a very special ramen, hair styles at the mirror, and Umbreon allowed indoors."),
    ("7 Oct", "The furniture workshop", "on the main street: commissions, a catalogue, two craftsmen, and you can finally sit on chairs."),
    ("7 Oct", "An app icon", "rendered from the game's own models. My house, Umbreon, me. Very on brand."),
    ("6 Oct", "Maker Studio's Furniture Maker", "and a My Creatures tab."),
    ("5 Oct", "Sideways play", "on the Galaxy S25, the Xperia and the Z Flip."),
    ("4 Oct", "Mimikyu rebuilt from my drawing", "and an Eevee in Chloe's backyard. Cloud shadows and grass that parts when you walk through it."),
    ("4 Oct", "Separate wallets and bags", "so Chloe can no longer spend my money."),
    ("3 Oct", "Christmas, milestones, wardrobe", "the designer's ten milestones, outfits and hair, shopkeeper emotes, a life-size Mimikyu."),
    ("Sept", "The two-player farm", "the NAS game server, the start screen, the Android app that updates itself."),
]
items = "\n".join(f'            <li><time>{d}</time><strong>{t}</strong> {x}</li>' for d, t, x in LOG)
page("ccfarm-updates.html", "ccfarm updates",
     "What's changed in ccfarm, roughly by the day.",
     "ccfarm · updates", "What's new",
     "The game changes almost every day, so here's the log. Newest first. Dates are 2026.",
     f'''
        {shot("launcher-icon.png", "ccfarm's Android app icon", "The new app icon.", "phone")}
        <div class="card reveal">
          <ul class="log">
{items}
          </ul>
        </div>''',
     prev=("ccfarm-workflow.html", "How it's built"))
print("ok")
