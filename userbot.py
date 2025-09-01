import os
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from flask import Flask
from threading import Thread

# Ambil dari Railway Environment Variable
API_ID = int(os.environ["API_ID"])
API_HASH = os.environ["API_HASH"]
STRING_SESSION = os.environ["STRING_SESSION"]

# Pakai StringSession biar bisa login sekali doang
client = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH)

# Template pesan
TEMPLATES = {
    "a": {"msg": "hit @jelayi 58k 1b fw 🆓💝/🧸 @seleprem testi @bhunnies"},
    "b": {"msg": "hit @jelayi testi @bhunnies @seleprem"},
    "c": {"msg": "hit @jelayi chibi art dan wm t.me/canvasjelay/8 ready t.me/canvasjelay/1067 results @artdumpy"},
    "d": {"msg": "hit @jelayi chibi art dan wm t.me/canvasjelay/8 ready t.me/canvasjelay/1067 results @artdumpy", "img": "WhatsApp Image 2025-09-01 at 22.40.15_b7a7634e.jpg"},
    "e": {"msg": "Ukiyo🩵Jelay", "img": "foto_bareng_bubub.jpg"}
}

# Event handler (kalo lu sendiri ngetik a/b/c/d)
@client.on(events.NewMessage(outgoing=True))
async def handler(event):
    text = event.raw_text.lower().strip()
    if text in TEMPLATES:
        await event.delete()  # hapus pesan asli
        data = TEMPLATES[text]

        if "img" in data:
            await event.respond(file=data["img"], message=data["msg"])
        else:
            await event.respond(data["msg"])

print("✅ Userbot siap jalan di Railway...")

# --- Flask biar Railway tetep aktif ---
app = Flask('')

@app.route('/')
def home():
    return "✅ Userbot aktif di Railway!"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# Start bot
keep_alive()
client.start()
client.run_until_disconnected()
