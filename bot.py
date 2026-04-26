from pyrogram import Client, filters

API_ID = int("30393757")
API_HASH = "61bf9121fd68e732ab283144a0c6169f"
BOT_TOKEN = "8658970682:AAEAVpUdljpJdPFp_QzccNek6yeT52wJua8"

app = Client("musicbot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("🎵 Music Bot is Running ✅")

app.run()
