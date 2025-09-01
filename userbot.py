import os
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from flask import Flask
from threading import Thread

# Ambil dari Railway Environment Variable
API_ID = int(os.environ["API_ID"])
API_HASH = os.environ["API_HASH"]
STRING_SESSION = os.environ["STRING_SESSION"]

# Connect ke Telegram pakai StringSession
client = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH)

# Daftar template
TEMPLATES = {
    "a": {"msg": "hit @jelayi 58k 1b fw 🆓💝/🧸 @seleprem testi @bhunnies"},
    "b": {"msg": "hit @jelayi testi @bhunnies @seleprem"},
    "c": {"msg": "hit @jelayi chibi art dan wm t.me/canvasjelay/8 ready t.me/canvasjelay/1067 results @artdumpy"},
    "d": {"msg": "hit @jelayi chibi art dan wm t.me/canvasjelay/8 ready t.me/canvasjelay/1067 results @artdumpy", "img": "foto_bareng_bubub.jpg"}  # pastikan file ini ada di repo
}

# Event handler
@client.on(events.NewMessage(outgoing=True))
async def handler(event):
    text = event.raw_text.lower().strip()
    if text in TEMPLATES:
        data = TEMPLATES[text]

        if "img" in data:
            # Edit jadi foto (hapus teks lama, ganti dengan media + caption)
            await event.delete()
            await event.respond(file=data["img"], message=data["msg"])
        else:
            # Edit teks langsung
            await event.edit(data["msg"])

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

keep_alive()
client.start()
client.run_until_disconnected()
