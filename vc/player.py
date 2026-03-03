from pytgcalls.types.input_stream import AudioPiped

class VoiceManager:
    def __init__(self, call):
        self.call = call

    async def join_and_play(self, chat_id, file):
        await self.call.join_group_call(
            chat_id,
            AudioPiped(file)
        )

    async def stop(self, chat_id):
        await self.call.leave_group_call(chat_id)
