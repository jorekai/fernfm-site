"""Erzeugt die statischen Seiten von fernFM (DE/EN). Aufruf: python3 build.py"""
import pathlib

ROOT = pathlib.Path(__file__).parent
EMAIL = "info@fernfm.com"
OWNER = "Nils Jorek"
ADDRESS_DE = "[Anschrift folgt]"
ADDRESS_EN = ADDRESS_DE
UPDATED = {"de": "20. November 2026", "en": "November 20, 2026"}
APP_URL = "https://apps.apple.com/app/id6836852211"

T = {
    "de": {
        "nav": [("index.html", "Start"), ("support.html", "Support"), ("privacy.html", "Datenschutz")],
        "foot": [("imprint.html", "Impressum"), ("privacy.html", "Datenschutz"), ("support.html", "Support")],
        "other": ("en", "English"),
        "updated": "Stand",
    },
    "en": {
        "nav": [("index.html", "Home"), ("support.html", "Support"), ("privacy.html", "Privacy")],
        "foot": [("imprint.html", "Legal notice"), ("privacy.html", "Privacy"), ("support.html", "Support")],
        "other": ("de", "Deutsch"),
        "updated": "Last updated",
    },
}

PAGES = {}

PAGES[("de", "index.html")] = ("fernFM: Radio aus aller Welt", "Radio aus aller Welt für das iPhone. Ohne Konto, ohne Werbung.", f"""
<p class="eyebrow">Radio für das iPhone</p>
<h1>Radio aus aller Welt. Ruhig gemacht.</h1>
<p class="lead">fernFM spielt Zehntausende Sender aus aller Welt, merkt sich die Songs, die du gehört hast, und kommt ohne Konto, ohne Werbung und ohne Tracking aus.</p>
<p><a href="{APP_URL}">Im App Store laden</a></p>
<div class="card"><h2>Kostenlos</h2><ul>
<li>Sender suchen nach Genre, Land und Sprache</li>
<li>Entdecken auf dem Globus und Sender in deiner Nähe</li>
<li>Favoriten und Sender-Playlists</li>
<li>Song-Verlauf und Song-Erkennung</li>
<li>AirPlay und Steuerung auf dem Sperrbildschirm</li></ul></div>
<div class="card"><h2>fernFM Plus, einmalig</h2><ul>
<li>CarPlay mit Favoriten, Playlists und Entdecken</li>
<li>Songs speichern, in Sammlungen ordnen, als Apple-Music-Playlist exportieren</li>
<li>iCloud-Abgleich zwischen deinen Geräten</li>
<li>Widgets für den Home-Bildschirm</li></ul>
<p>Kein Abo. Mit Familienfreigabe für die ganze Familie.</p></div>
""")

PAGES[("en", "index.html")] = ("fernFM: Radio from around the world", "Radio from around the world for iPhone. No account, no ads.", f"""
<p class="eyebrow">Radio for iPhone</p>
<h1>Radio from around the world. Made calm.</h1>
<p class="lead">fernFM plays tens of thousands of stations from around the world, remembers the songs you heard and works without an account, ads or tracking.</p>
<p><a href="{APP_URL}">Download on the App Store</a></p>
<div class="card"><h2>Free</h2><ul>
<li>Search stations by genre, country and language</li>
<li>Explore on the globe and find stations near you</li>
<li>Favorites and station playlists</li>
<li>Song history and song recognition</li>
<li>AirPlay and lock screen controls</li></ul></div>
<div class="card"><h2>fernFM Plus, one-time</h2><ul>
<li>CarPlay with favorites, playlists and discover</li>
<li>Save songs, sort them into collections, export them as an Apple Music playlist</li>
<li>iCloud sync between your devices</li>
<li>Home screen widgets</li></ul>
<p>No subscription. Shared with your family through Family Sharing.</p></div>
""")

PAGES[("de", "support.html")] = ("Support: fernFM", "Hilfe und Kontakt für fernFM.", f"""
<p class="eyebrow">Support</p>
<h1>Hilfe und Kontakt</h1>
<p class="lead">Fragen, Fehler oder ein Sender, der nicht spielt? Schreib an <a href="mailto:{EMAIL}">{EMAIL}</a>. Wir antworten in der Regel innerhalb von zwei Werktagen.</p>
<h2>Ein Sender spielt nicht</h2>
<p>fernFM nutzt die offene Senderdatenbank <a href="https://www.radio-browser.info">Radio-Browser</a>. Manche Streams sind zeitweise offline oder haben ihre Adresse geändert. fernFM versucht es automatisch erneut. Hilft das nicht, kannst du den Sender ausblenden und ihn auf radio-browser.info melden oder korrigieren.</p>
<h2>fernFM Plus wiederherstellen</h2>
<p>Öffne Einstellungen in fernFM, tippe auf fernFM Plus und dann auf „Käufe wiederherstellen“. Melde dich dafür mit der Apple-ID an, mit der du gekauft hast. Mit Familienfreigabe steht Plus auch deiner Familie zur Verfügung.</p>
<h2>Erstattung</h2>
<p>Käufe wickelt Apple ab. Eine Erstattung beantragst du unter <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>.</p>
<h2>iCloud-Abgleich</h2>
<p>Der Abgleich nutzt deinen iCloud-Account. Prüfe in den iOS-Einstellungen unter deinem Namen und iCloud, dass iCloud Drive aktiv ist. Favoriten, Playlists und Sammlungen erscheinen dann nach kurzer Zeit auf deinen anderen Geräten.</p>
<h2>Song-Erkennung</h2>
<p>Die Erkennung hört etwa zehn Sekunden des laufenden Streams an und fragt den Shazam-Katalog von Apple. Sie funktioniert nur auf einem echten iPhone und nicht bei jedem Sender, etwa bei Wortbeiträgen.</p>
<h2>Fehlerbericht senden</h2>
<p>Unter Einstellungen und Diagnose kannst du einen Fehlerbericht teilen. Er enthält App- und iOS-Version und den Fehler, aber keine Sender oder Songs.</p>
""")

PAGES[("en", "support.html")] = ("Support: fernFM", "Help and contact for fernFM.", f"""
<p class="eyebrow">Support</p>
<h1>Help and contact</h1>
<p class="lead">Questions, bugs or a station that does not play? Write to <a href="mailto:{EMAIL}">{EMAIL}</a>. We usually reply within two business days.</p>
<h2>A station does not play</h2>
<p>fernFM uses the open station database <a href="https://www.radio-browser.info">Radio Browser</a>. Some streams are offline for a while or have moved. fernFM retries on its own. If that does not help, you can hide the station and report or fix it on radio-browser.info.</p>
<h2>Restore fernFM Plus</h2>
<p>Open Settings in fernFM, tap fernFM Plus and then "Restore purchases". Use the Apple ID you bought it with. With Family Sharing, Plus is available to your family as well.</p>
<h2>Refunds</h2>
<p>Apple handles all purchases. You can request a refund at <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>.</p>
<h2>iCloud sync</h2>
<p>Sync uses your iCloud account. In iOS Settings, under your name and iCloud, make sure iCloud Drive is on. Favorites, playlists and collections then show up on your other devices after a short while.</p>
<h2>Song recognition</h2>
<p>Recognition listens to about ten seconds of the current stream and asks Apple's Shazam catalog. It only works on a real iPhone and not on every station, for example during talk.</p>
<h2>Send an error report</h2>
<p>Under Settings and Diagnostics you can share an error report. It contains the app and iOS version and the error, but no stations or songs.</p>
""")

PAGES[("de", "privacy.html")] = ("Datenschutz: fernFM", "Datenschutzerklärung für die App fernFM.", f"""
<p class="eyebrow">Datenschutz</p>
<h1>Datenschutzerklärung</h1>
<p class="updated">{T['de']['updated']}: {UPDATED['de']}</p>
<p class="lead">Kurz gesagt: fernFM hat keinen eigenen Server, kein Konto, keine Werbung und kein Tracking. Deine Favoriten, Playlists und Songs liegen auf deinem Gerät und, wenn du fernFM Plus nutzt, in deinem eigenen iCloud-Account. Wir sehen davon nichts.</p>

<h2>1. Verantwortlicher</h2>
<p>{OWNER}<br>{ADDRESS_DE}<br>E-Mail: <a href="mailto:{EMAIL}">{EMAIL}</a></p>

<h2>2. Daten auf deinem Gerät</h2>
<p>Favoriten, Sender-Playlists, ausgeblendete Sender, der Song-Verlauf, gespeicherte Songs, Sammlungen und Fehlerberichte werden lokal in der App gespeichert. Sie verlassen das Gerät nur in den unten beschriebenen Fällen. Unter Einstellungen kannst du alle Daten löschen; beim Löschen der App werden sie ebenfalls entfernt.</p>

<h2>3. Dienste, mit denen die App direkt spricht</h2>
<p>Für diese Verbindungen sendet dein Gerät technisch bedingt seine IP-Adresse an den jeweiligen Anbieter. Wir erhalten diese Daten nicht.</p>
<ul>
<li><strong>Radio-Browser</strong> (radio-browser.info): Senderlisten, Suche und Senderdetails. Übermittelt werden deine Suchbegriffe und Filter. Beim Abspielen eines Senders wird die Sender-ID gemeldet, damit die Datenbank beliebte Sender zählen kann.</li>
<li><strong>Radiosender</strong>: Der Audiostream und die Songtitel kommen direkt vom Server des jeweiligen Senders. Senderlogos werden von der dort angegebenen Adresse geladen.</li>
<li><strong>Apple iTunes-Suche</strong>: Zu erkannten Songs werden Künstler und Titel an Apple gesendet, um Cover und einen Verweis auf Apple Music zu finden.</li>
</ul>

<h2>4. Sender in deiner Nähe (Standort)</h2>
<p>Nur wenn du „Sender in meiner Nähe“ antippst und den Zugriff erlaubst, liest fernFM einmalig einen ungefähren Standort. Er wird auf etwa einen Kilometer gerundet und nur für diese Suche an Radio-Browser gesendet. fernFM speichert den Standort nicht und nutzt ihn nicht im Hintergrund. Rechtsgrundlage ist deine Einwilligung (Art. 6 Abs. 1 lit. a DSGVO), die du in den iOS-Einstellungen jederzeit widerrufen kannst.</p>

<h2>5. Song-Erkennung (ShazamKit)</h2>
<p>Wenn du die Song-Erkennung startest, erzeugt fernFM aus etwa zehn Sekunden des laufenden Streams eine Audio-Signatur und sendet sie an Apples Shazam-Dienst. Das Mikrofon wird nicht verwendet. Es gilt die Datenschutzerklärung von Apple.</p>

<h2>6. iCloud-Abgleich (fernFM Plus)</h2>
<p>Mit fernFM Plus werden Favoriten, Playlists, gespeicherte Songs und Sammlungen über den iCloud-Schlüssel-Wert-Speicher in deinem eigenen iCloud-Account abgelegt. Apple verarbeitet diese Daten als Anbieter von iCloud. Wir haben keinen Zugriff darauf.</p>

<h2>7. Apple Music Export</h2>
<p>Wenn du eine Sammlung als Playlist exportierst und den Zugriff erlaubst, legt fernFM über MusicKit eine Playlist in deiner Apple-Music-Mediathek an.</p>

<h2>8. Käufe</h2>
<p>fernFM Plus wird über den App Store gekauft. Zahlung und Abwicklung übernimmt Apple. Die App prüft den Kauf auf dem Gerät über StoreKit. Wir erhalten keine Zahlungsdaten.</p>

<h2>9. Fehlerberichte</h2>
<p>Fehlerberichte bleiben auf dem Gerät. Sie enthalten App- und iOS-Version und den Fehler, aber keine Sender oder Songs. Nur wenn du einen Bericht ausdrücklich teilst, wird er über den von dir gewählten Weg versendet.</p>

<h2>10. Keine Analyse, keine Werbung</h2>
<p>fernFM enthält keine Analyse-, Tracking- oder Werbe-SDKs und erstellt keine Nutzerprofile.</p>

<h2>11. Diese Website</h2>
<p>Diese Seite wird über GitHub Pages (GitHub Inc., USA) ausgeliefert. GitHub verarbeitet dabei technisch notwendige Daten wie deine IP-Adresse in Server-Logs. Die Seite setzt keine Cookies und lädt keine externen Schriften oder Tracker.</p>

<h2>12. Deine Rechte</h2>
<p>Du hast nach der DSGVO das Recht auf Auskunft, Berichtigung, Löschung, Einschränkung der Verarbeitung, Datenübertragbarkeit und Widerspruch sowie das Recht, dich bei einer Datenschutz-Aufsichtsbehörde zu beschweren. Da wir keine personenbezogenen Daten über dich speichern, können die meisten Anfragen direkt in der App erledigt werden. Schreib uns gern an <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
""")

PAGES[("en", "privacy.html")] = ("Privacy: fernFM", "Privacy policy for the fernFM app.", f"""
<p class="eyebrow">Privacy</p>
<h1>Privacy policy</h1>
<p class="updated">{T['en']['updated']}: {UPDATED['en']}</p>
<p class="lead">In short: fernFM has no server of its own, no account, no ads and no tracking. Your favorites, playlists and songs stay on your device and, if you use fernFM Plus, in your own iCloud account. We see none of it.</p>

<h2>1. Controller</h2>
<p>{OWNER}<br>{ADDRESS_EN}<br>Email: <a href="mailto:{EMAIL}">{EMAIL}</a></p>

<h2>2. Data on your device</h2>
<p>Favorites, station playlists, hidden stations, the song history, saved songs, collections and error reports are stored locally in the app. They only leave the device in the cases described below. You can delete all data in Settings; deleting the app removes it as well.</p>

<h2>3. Services the app talks to directly</h2>
<p>For these connections your device necessarily sends its IP address to the provider. We do not receive this data.</p>
<ul>
<li><strong>Radio Browser</strong> (radio-browser.info): station lists, search and station details. Your search terms and filters are sent. When you play a station, its ID is reported so the database can count popular stations.</li>
<li><strong>Radio stations</strong>: the audio stream and song titles come straight from the station's server. Station logos load from the address the station provides.</li>
<li><strong>Apple iTunes Search</strong>: for recognized songs, artist and title are sent to Apple to find artwork and a link to Apple Music.</li>
</ul>

<h2>4. Stations near you (location)</h2>
<p>Only when you tap "Stations near me" and allow access does fernFM read an approximate location once. It is rounded to about one kilometer and sent to Radio Browser for this search only. fernFM does not store the location and does not use it in the background. The legal basis is your consent (Art. 6(1)(a) GDPR), which you can withdraw in iOS Settings at any time.</p>

<h2>5. Song recognition (ShazamKit)</h2>
<p>When you start song recognition, fernFM creates an audio signature from about ten seconds of the current stream and sends it to Apple's Shazam service. The microphone is not used. Apple's privacy policy applies.</p>

<h2>6. iCloud sync (fernFM Plus)</h2>
<p>With fernFM Plus, favorites, playlists, saved songs and collections are stored in the iCloud key-value store of your own iCloud account. Apple processes this data as the provider of iCloud. We have no access to it.</p>

<h2>7. Apple Music export</h2>
<p>When you export a collection as a playlist and allow access, fernFM uses MusicKit to create a playlist in your Apple Music library.</p>

<h2>8. Purchases</h2>
<p>fernFM Plus is bought through the App Store. Apple handles payment. The app verifies the purchase on the device through StoreKit. We receive no payment data.</p>

<h2>9. Error reports</h2>
<p>Error reports stay on the device. They contain the app and iOS version and the error, but no stations or songs. A report is only sent if you explicitly share it, through the channel you choose.</p>

<h2>10. No analytics, no ads</h2>
<p>fernFM contains no analytics, tracking or advertising SDKs and builds no user profiles.</p>

<h2>11. This website</h2>
<p>This site is served by GitHub Pages (GitHub Inc., USA). GitHub processes technically necessary data such as your IP address in server logs. The site sets no cookies and loads no external fonts or trackers.</p>

<h2>12. Your rights</h2>
<p>Under the GDPR you have the right of access, rectification, erasure, restriction of processing, data portability and objection, and the right to lodge a complaint with a supervisory authority. Since we store no personal data about you, most requests can be handled directly in the app. Feel free to write to <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
""")

PAGES[("de", "imprint.html")] = ("Impressum: fernFM", "Impressum von fernFM.", f"""
<p class="eyebrow">Impressum</p>
<h1>Impressum</h1>
<p>Angaben gemäß § 5 DDG</p>
<p>{OWNER}<br>{ADDRESS_DE}</p>
<p>E-Mail: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
<p>Verantwortlich für den Inhalt nach § 18 Abs. 2 MStV: {OWNER}, Anschrift wie oben.</p>
""")

PAGES[("en", "imprint.html")] = ("Legal notice: fernFM", "Legal notice for fernFM.", f"""
<p class="eyebrow">Legal notice</p>
<h1>Legal notice</h1>
<p>Information according to § 5 DDG (Germany)</p>
<p>{OWNER}<br>{ADDRESS_EN}</p>
<p>Email: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
""")


def page(lang, name, title, desc, body):
    t = T[lang]
    nav = "".join(f'<a href="{h}">{l}</a>' for h, l in t["nav"][1:])
    foot = "".join(f'<a href="{h}">{l}</a>' for h, l in t["foot"])
    other, other_label = t["other"]
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="../icon.png">
<link rel="apple-touch-icon" href="../icon.png">
<link rel="alternate" hreflang="{other}" href="../{other}/{name}">
<link rel="stylesheet" href="../style.css">
</head>
<body>
<main>
<header>
<a class="brand" href="index.html"><img src="../icon.png" alt="">fernFM</a>
<nav>{nav}<a href="../{other}/{name}" hreflang="{other}">{other_label}</a></nav>
</header>
{body.strip()}
<footer>{foot}<span>© 2026 {OWNER}</span></footer>
</main>
</body>
</html>
"""


for (lang, name), (title, desc, body) in PAGES.items():
    (ROOT / lang / name).write_text(page(lang, name, title, desc, body), encoding="utf-8")

(ROOT / "index.html").write_text("""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>fernFM</title>
<script>location.replace((navigator.language || '').toLowerCase().startsWith('de') ? 'de/' : 'en/');</script>
<meta http-equiv="refresh" content="1; url=en/">
</head><body><p><a href="de/">Deutsch</a> · <a href="en/">English</a></p></body></html>
""", encoding="utf-8")
(ROOT / ".nojekyll").write_text("")
print("ok", len(PAGES))
