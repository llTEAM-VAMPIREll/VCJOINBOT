from pyrogram import filters
from pyrogram.types import Message

def register_handlers(app, voice_manager):

    @app.on_message(filters.command("start"))
    async def start_handler(client, message: Message):
        await message.reply_text(
            "🔥 WELCOME TO VAMPIRE VC FIGHT BOT 🔥\n\n"
            "⚡ A VERY POWERFULL BOT FOR VOICE CHAT\n"
            "🔊 LOUDLY VOICE AND PREMIUM WORK\n\n"
            "Type /play <file.mp3> to start playing audio."
        )

    @app.on_message(filters.command("play"))
    async def play_handler(client, message: Message):
        if len(message.command) < 2:
            return await message.reply("Usage: /play audio.mp3")

        file = message.command[1]
        chat_id = message.chat.id

        await voice_manager.join_and_play(chat_id, file)
        await message.reply("🎵 Playing Audio...")

    @app.on_message(filters.command("stop"))
    async def stop_handler(client, message: Message):
        chat_id = message.chat.id
        await voice_manager.stop(chat_id)
        await message.reply("❌ Stopped")
