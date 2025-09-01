import os
from telethon import TelegramClient, events
from flask import Flask
from threading import Thread

# Ambil dari Railway Environment Variable (lebih aman)
API_ID = int(os.environ["API_ID"])
API_HASH = os.environ["API_HASH"]

# Session name terserah, biar nyimpen login
client = TelegramClient("userbot", API_ID, API_HASH)

# Daftar template
TEMPLATES = {
    "a": "hit @jelayi 58k 1b fw 🆓💝/🧸 @seleprem testi @bhunnies",
    "b": "hit @jelayi testi @bhunnies @seleprem",
    "c": "hit @jelayi chibi art dan wm t.me/canvasjelay/8
ready t.me/canvasjelay/1067 results @artdumpy"
}

# Event handler
@client.on(events.NewMessage(outgoing=True))
async def handler(event):
    text = event.raw_text.lower().strip()
    if text in TEMPLATES:
        await event.edit(TEMPLATES[text])

print("✅ Userbot jalan di Railway...")

# --- Tambahan Flask biar Railway anggap aktif ---
app = Flask('')

@app.route('/')
def home():
    return "✅ Userbot aktif di Railway!"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
# ------------------------------------------------

# Jalankan Flask + Bot
keep_alive()
client.start()
client.run_until_disconnected()
