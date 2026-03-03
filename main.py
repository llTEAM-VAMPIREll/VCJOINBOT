import asyncio
from pyrogram import Client
from pytgcalls import PyTgCalls
from config import API_ID, API_HASH, BOT_TOKEN, SESSION_STRING

from bot.handlers import register_handlers
from vc.player import VoiceManager

# User account client (string session)
user_client = Client(
    "user",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION_STRING
)

# Bot client
bot_client = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

call = PyTgCalls(user_client)

voice_manager = VoiceManager(call)

async def main():
    await user_client.start()
    await bot_client.start()
    await call.start()

    register_handlers(bot_client, voice_manager)

    print("Bot Started Successfully 🚀")
    await asyncio.Event().wait()

asyncio.run(main())
