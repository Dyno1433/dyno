from pyrogram import Client, filters 
from pyrogram.types import Message
from config import SUDO_USERS
from pyrogram import Client
from callsmusic.callsmusic import client as nikki
import asyncio

@Client.on_message(filters.command(["inviteall", "kidnapall"], [".", "/", "!"]) & filters.user(SUDO_USERS))
async def inviteall(client: Client, message: Message):
    hero = await message.reply_text("Starting...")
    text = message.text.split(" ", 1)
    queryy = text[1]
    chat = await nikki.get_chat(queryy)
    tgchat = message.chat
    await hero.edit_text(f"inviting users from {chat.username}")
    async for member in nikki.iter_chat_members(chat.id):
        user= member.user
        zxb= ["online" , "recently"]
        if user.status in zxb:
           try:
            await nikki.add_chat_members(tgchat.id, user.id)
           except Exception as e:
            mg= await client.send_message("me", f"error-   {e}")
            await asyncio.sleep(0.3)
            await mg.delete()
