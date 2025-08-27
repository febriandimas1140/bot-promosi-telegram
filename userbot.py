from telethon import TelegramClient, events

# Ganti ini dengan API ID & API HASH dari my.telegram.org
API_ID = 23030559
API_HASH = "e1507c98ccd8faf6b7fdb79141d79f83"

# Session name terserah, biar nyimpen login
client = TelegramClient("userbot", API_ID, API_HASH)

# Daftar template
TEMPLATES = {
    "a": "hit @jelayi 58k 1b fw 🆓💝/🧸 @seleprem testi @bhunnies",
    "b": "hmu chibi art DISKON t.me/canvasjelay/1197 results @artdumpy",
    "c": "hmu chibi art & wm t.me/canvasjelay/8 ready t.me/canvasjelay/1067 results @artdumpy"
}

# Event handler untuk setiap pesan yang dikirim akun lu sendiri
@client.on(events.NewMessage(outgoing=True))
async def handler(event):
    text = event.raw_text.lower().strip()
    if text in TEMPLATES:
        await event.edit(TEMPLATES[text])  # Edit pesan jadi template

print("✅ Userbot jalan, tunggu pesan lu sendiri...")
client.start()
client.run_until_disconnected()