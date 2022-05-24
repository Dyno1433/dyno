# @nikitabots

"""
Greetings,

 ⤷ Custom greetings plugin with Ascii text art

   © @nikitaroy_31
   © @nikitabots
"""

import os
import random

from config import SUDO_USERS
from pyrogram import filters, Client
from pyrogram.types import Message
from callsmusic.callsmusic import client as nikki
from helpers.decorators import sudo_users_only
from helpers.filters import e_o_r, command, get_text

# Strings collection
S = (
    "..... (¯`v´¯)♥️\n"
    ".......•.¸.•´\n"
    "....¸.•´  🅷🅸\n"
    "... (   BABYy\n"
    "☻/ \n"
    "/▌✿🌷✿\n"
    "/ \     \|/\n"
)

X = (
    ".......🦋🦋........🦋🦋\n"
    "...🦋.........🦋🦋.......🦋\n"
    "...🦋............💙..........🦋\n"
    ".....🦋🅣🅗🅐🅝🅚🅢 🦋\n"
    "....... 🦋.................🦋\n"
    "..............🦋......🦋\n"
    "...................💙\n"
)



BYE_TEXTS = [
    """
╭━━╮
┃╭╮┣┳┳━╮
┃╭╮┃┃┃┻┫
╰━━╋╮┣━╯
╱╱╱╰━╯
    """,
    """
███████████████████
█▄─▄─▀█▄─█─▄█▄─▄▄─█
██─▄─▀██▄─▄███─▄█▀█
▀▄▄▄▄▀▀▀▄▄▄▀▀▄▄▄▄▄▀
    """,
    """

░█▀▀█ █──█ █▀▀ 
░█▀▀▄ █▄▄█ █▀▀ 
░█▄▄█ ▄▄▄█ ▀▀▀
    """,
    """
▒█▀▀█ █░░█ █▀▀ 
▒█▀▀▄ █▄▄█ █▀▀ 
▒█▄▄█ ▄▄▄█ ▀▀▀
    """,
    """
🎁🐲  𝐛Ƴ𝕖  🎄💗
    """
]

GOOD_NIGHT_TEXTS = [
    """
█▀▀ █▀█ █▀█ █▀▄
█▄█ █▄█ █▄█ █▄▀

█▄░█ █ █▀▀ █░█ ▀█▀
█░▀█ █ █▄█ █▀█ ░█░
    """,
    """
╔══╗────╔╗
║╔═╬═╦═╦╝║
║╚╗║╬║╬║╬║
╚══╩═╩═╩═╝
╔═╦╦╗─╔╗╔╗
║║║╠╬═╣╚╣╚╗
║║║║║╬║║║╔╣
╚╩═╩╬╗╠╩╩═╝
────╚═╝
    """,
    """
╭━━━╮╱╱╱╱╱╱╱╭╮
┃╭━╮┃╱╱╱╱╱╱╱┃┃
┃┃╱╰╋━━┳━━┳━╯┃
┃┃╭━┫╭╮┃╭╮┃╭╮┃
┃╰┻━┃╰╯┃╰╯┃╰╯┃
╰━━━┻━━┻━━┻━━╯
╭━╮╱╭╮╱╱╱╭╮╱╭╮
┃┃╰╮┃┃╱╱╱┃┃╭╯╰╮
┃╭╮╰╯┣┳━━┫╰┻╮╭╯
┃┃╰╮┃┣┫╭╮┃╭╮┃┃
┃┃╱┃┃┃┃╰╯┃┃┃┃╰╮
╰╯╱╰━┻┻━╮┣╯╰┻━╯
╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╰━━╯
    """,
    """
╭━━╮╱╱╱╱╭╮
┃╭━╋━┳━┳╯┃
┃╰╮┃╋┃╋┃╋┃
╰━━┻━┻━┻━╯
╭━┳┳╮╱╭╮╭╮
┃┃┃┣╋━┫╰┫╰╮
┃┃┃┃┃╋┃┃┃╭┫
╰┻━┻╋╮┣┻┻━╯
╱╱╱╱╰━╯
    """,
    """
✮     ✯  ✯      ✮      ✯    
  ✯       ✮    ✮   ✮       ✯  
 ✯     ✮     🌛    ✯    ✯ 
   ✯      ✮     ✮       ✮   ✯
  ✯     ✯       ✯        ✮       ✮

    🌟🌠   g๏𝑜𝓭 Ⓝί𝓰𝐇t  🎯🌠
    """,
    """
｡♥️｡･ﾟ♡ﾟ･｡♥️｡･｡･｡･｡♥️｡･\n╱╱╱╱╱╱╱╭╮╱╱╱╭╮╱╭╮╭╮\n╭━┳━┳━┳╯┃╭━┳╋╋━┫╰┫╰╮\n┃╋┃╋┃╋┃╋┃┃┃┃┃┃╋┃┃┃╭┫\n┣╮┣━┻━┻━╯╰┻━┻╋╮┣┻┻━╯\n╰━╯╱╱╱╱╱╱╱╱╱╱╰━╯\n｡♥️｡･ﾟ♡ﾟ･｡♥️° ♥️｡･ﾟ♡ﾟ･
    """,
    """
♛┈⛧┈┈•༶🦋⋇⋆✦⋆⋇🦋༶•┈┈⛧┈♛\n╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨\n╔══╗────╔╗╔═╦╦╗─╔╗╔╗\n║╔═╬═╦═╦╝║║║║╠╬═╣╚╣╚╗\n║╚╗║╬║╬║╬║║║║║║╬║║║╔╣\n╚══╩═╩═╩═╝╚╩═╩╬╗╠╩╩═╝\n──────────────╚═╝\n╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨\n♛┈⛧┈┈•༶🦋⋇⋆✦⋆⋇🦋༶•┈┈⛧┈♛･
    """
]

GOOD_MORNING_TEXTS = [
    """
╭━━╮╱╱╱╱╭╮
┃╭━╋━┳━┳╯┃
┃╰╮┃╋┃╋┃╋┃
╰━━┻━┻━┻━╯
╭━┳━╮╱╱╱╱╱╱╭╮
┃┃┃┃┣━┳┳┳━┳╋╋━┳┳━╮
┃┃┃┃┃╋┃╭┫┃┃┃┃┃┃┃╋┃
╰┻━┻┻━┻╯╰┻━┻┻┻━╋╮┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━╯
    """,
    """
🐯 ⋆ 🕊  🎀  𝒢🌸❤️𝒹 𝑀🌞𝓇𝓃𝒾𝓃𝑔  🎀  🕊 ⋆ 🐯
    """,
    """
✷  🎀  𝒢🍪🍪𝒹 𝑀🍬𝓇𝓃𝒾𝓃𝑔  🎀  ✷
    """,
    """
🍧😝  g𝕆𝐨Ⓓ  🐨🔥

┏━┳━┓╋╋╋╋╋╋┏┓
┃┃┃┃┣━┳┳┳━┳╋╋━┳┳━┓
┃┃┃┃┃╋┃┏┫┃┃┃┃┃┃┃╋┃
┗┻━┻┻━┻┛┗┻━┻┻┻━╋┓┃
╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┗━┛
    """,
    """
♛┈⛧┈┈•༶🦋⋇⋆✦⋆⋇🦋༶•┈┈⛧┈♛\n╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨\n╔══╗────╔╗──────────╔╗\n║╔═╬═╦═╦╝║╔══╦═╦╦╦═╦╬╬═╦╦═╗\n║╚╗║╬║╬║╬║║║║║╬║╔╣║║║║║║║╬║\n╚══╩═╩═╩═╝╚╩╩╩═╩╝╚╩═╩╩╩═╬╗║\n────────────────────────╚═╝\n╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨\n♛┈⛧┈┈•༶🦋⋇⋆✦⋆⋇🦋༶•┈┈⛧┈♛･
    """
]

HI_TEXTS = [
    """
💣🍔  𝓗𝓘  🍫♦️
    """,
    """
██╗░░██╗██╗
██║░░██║██║
███████║██║
██╔══██║██║
██║░░██║██║
╚═╝░░╚═╝╚═╝
    """,
    """
█░█ █
█▀█ █
    """,
    """
🐟 ⋆ 🐬  🎀  𝐻𝒾  🎀  🐬 ⋆ 🐟
    """,
    """
╔╗─╔╗
║║─║║
║╚═╝╠╗
║╔═╗╠╣
║║─║║║
╚╝─╚╩╝
    """,
    """
❈★  🎀  𝐻𝒾  🎀  ★❈
    """
]

@nikki.on_message(command("byy")  & ~filters.edited)
@sudo_users_only
async def bye_bois(_, message: Message):
    await e_o_r(nikki_message=message, msg_text= random.choice(BYE_TEXTS))

@nikki.on_message(command("hui")  & ~filters.edited)
@sudo_users_only
async def hi_bruh(_, message: Message):
    await e_o_r(nikki_message=message, msg_text= random.choice(HI_TEXTS))

@nikki.on_message(command("gdm")  & ~filters.edited)
@sudo_users_only
async def gm_vmro(_, message: Message):
    await e_o_r(nikki_message=message, msg_text= random.choice(GOOD_MORNING_TEXTS))

@nikki.on_message(command("gdn")  & ~filters.edited)
@sudo_users_only
async def gn_vmro(_, message: Message):
    await e_o_r(nikki_message=message, msg_text= random.choice(GOOD_NIGHT_TEXTS))

@nikki.on_message(command("what")  & ~filters.edited)
@sudo_users_only
async def what_is_dis_vmro(_, message: Message):
    WHAT_CHOISES = ["Hol up! What? ( ‌❛ ‌ʖ‌❛ )", "Da what ( ‌❛ ⏥‌❛ ) ?", "Yo, what the ¯\_( ‌❛ ⏥‌❛ )_/¯", "Wait... Why me? (-’๏_๏’-)"]
    await e_o_r(nikki_message=message, msg_text= random.choice(WHAT_CHOISES))

@nikki.on_message(command("dk")  & ~filters.edited)
@sudo_users_only
async def idk_anything(_, message: Message):
    IDK_CHOISES = ["Idk ¯\_( ‌─ ⏥‌─ )_/¯", "Who tf knows ¯\_( ‌❛ ⏥‌❛ )_/¯", "da fak? Idk anything ¯\_( ‌─ .‌─ )_/¯"]
    await e_o_r(nikki_message=message, msg_text= random.choice(IDK_CHOISES))

@nikki.on_message(command("wdf")  & ~filters.edited)
@sudo_users_only
async def wtf_wtf_wtf(_, message: Message):
    WTF_CHOISES = [
        "Wtf bro ¯_(⊙︿⊙)_/¯", "Da fak? ¯_(⊙_ʖ⊙)_/¯",
        "Yo wtf (ཫ‌﹏ੂཀ‌)", "***Fake Crying ༎ຶ‿༎ຶ***"
    ]
    await e_o_r(nikki_message=message, msg_text= random.choice(WTF_CHOISES))

@nikki.on_message(command("sad")  & ~filters.edited)
@sudo_users_only
async def sad_life(_, message: Message):
    SAD_CHOISES = [
        """
        █▀▀ ▄▀▄ █▀▄ 
▄██ █▀█ █▄▀
   🥺Nikita🥺
        """,
        "You make me sad ʕ•‌ᴥ•‌ʔ", "Ah, that hurts (;•‌༚•‌)",
        "Oh no, that's sad ( ‌˃‌⌂˂‌ ‌)"
        ]
    await e_o_r(nikki_message=message, msg_text= random.choice(SAD_CHOISES))



@nikki.on_message(command("bby")  & ~filters.edited)
@sudo_users_only
async def eviral(_, message: Message):
    await e_o_r(nikki_message=message, msg_text=S)


@nikki.on_message(command("tnx")  & ~filters.edited)
@sudo_users_only
async def fox(_, message: Message):
    await e_o_r(nikki_message=message, msg_text=X)


@nikki.on_message(command("hbday")  & ~filters.edited)
@sudo_users_only
async def hbd(_, message: Message):
    "Happy birthday art."
    inpt = get_text(message)
    text = f"♥️{inpt}♥️"
    if not inpt:
        text = ""
    await e_o_r(nikki_message=message, msg_text=
        f"{text}\n\n▃▃▃▃▃▃▃▃▃▃▃\n┊ ┊ ┊ ┊ ┊ ┊\n┊ ┊ ┊ ┊ ˚✩ ⋆｡˚ ✩\n┊ ┊ ┊ ✫\n┊ ┊ ✧🎂🍰🍫🍭\n┊ ┊ ✯\n┊ . ˚ ˚✩\n........♥️♥️..........♥️♥️\n.....♥️........♥️..♥️........♥️\n...♥️.............♥️............♥️\n......♥️.....Happy.......♥️__\n...........♥️..............♥️__\n................♥️.....♥️__\n......................♥️__\n...............♥️......♥️__\n..........♥️...............♥️__\n.......♥️..Birthday....♥️\n.....♥️..........♥️..........♥️__\n.....♥️.......♥️_♥️.......♥️__\n.........♥️♥️........♥️♥️.....\n.............................................\n..... (¯`v´¯)♥️\n.......•.¸.•´STAY BLESSED\n....¸.•´      LOVE&FUN\n... (   YOU DESERVE\n☻/ THEM A LOT\n/▌✿🌷✿\n/ \     \|/\n▃▃▃▃▃▃▃▃▃▃▃\n\n{text}",
    )
@nikki.on_message(command("chill")  & ~filters.edited)
@sudo_users_only
async def cheer(_, message: Message):
    "cheer text art."
    await e_o_r(nikki_message=message, msg_text=
        "💐💐😉😊💐💐\n☕️ Cheer Up  🍵\n🍂 ✨ )) ✨  🍂\n🍂┃ (( * ┣┓ 🍂\n🍂┃*💗 ┣┛ 🍂 \n🍂┗━━┛  🍂🎂 For YOU  🍰\n💐💐😌😚💐💐",
    )

@nikki.on_message(command("gtwl")  & ~filters.edited)
@sudo_users_only
async def getwell(_, message: Message):
    "Get Well art."
    await e_o_r(nikki_message=message, msg_text= "🌹🌹🌹🌹🌹🌹🌹🌹 \n🌹😷😢😓😷😢💨🌹\n🌹💝💉🍵💊💐💝🌹\n🌹 GetBetter Soon! 🌹\n🌹🌹🌹🌹🌹🌹🌹🌹"
    )

@nikki.on_message(command("luck")  & ~filters.edited)
@sudo_users_only
async def luck(_, message: Message):
    "Luck art."
    await e_o_r(nikki_message=message, msg_text="💚~🍀🍀🍀🍀🍀\n🍀╔╗╔╗╔╗╦╗✨🍀\n🍀║╦║║║║║║👍🍀\n🍀╚╝╚╝╚╝╩╝。 🍀\n🍀・・ⓁⓊⒸⓀ🍀\n🍀🍀🍀 to you💚"
    )