from pyrogram import filters
from pyrogram.types import Message

def register_handlers(app, voice_manager):

    # START COMMAND
    @app.on_message(filters.command("start"))
    async def start_handler(client, message: Message):
        await message.reply_text(
            "🔥 WELCOME TO VAMPIRE VC FIGHT BOT 🔥\n\n"
            "⚡ A VERY POWERFULL BOT FOR VOICE CHAT\n"
            "🔊 LOUDLY VOICE AND PREMIUM WORK\n\n"
            "Type /help to see all commands."
        )

    # HELP COMMAND
    @app.on_message(filters.command("help"))
    async def help_handler(client, message: Message):
        await message.reply_text(
            "🛠 VAMPIRE VC FIGHT BOT COMMANDS 🛠\n\n"
            "🔹 /start - Bot information\n"
            "🔹 /help - Show this help message\n"
            "🔹 /play <file.mp3> - Join VC and play audio\n"
            "🔹 /stop - Leave voice chat\n\n"
            "🔥 FEATURES 🔥\n"
            "• Voice Chat Join\n"
            "• Audio Playback\n"
            "• Premium Working System\n"
            "• Powerful VC Control\n\n"
            "⚡ Made for powerful voice chat experience!"
        )

    # PLAY COMMAND
    @app.on_message(filters.command("play"))
    async def play_handler(client, message: Message):
        if len(message.command) < 2:
            return await message.reply("Usage: /play audio.mp3")

        file = message.command[1]
        chat_id = message.chat.id

        await voice_manager.join_and_play(chat_id, file)
        await message.reply("🎵 Playing Audio...")

    # STOP COMMAND
    @app.on_message(filters.command("stop"))
    async def stop_handler(client, message: Message):
        chat_id = message.chat.id
        await voice_manager.stop(chat_id)
        await message.reply("❌ Voice Chat Stopped")
