from Eliana.Config import Config
from Eliana.events import register
from Eliana import CMD_HELP
from Eliana import tbot as borg
from Eliana import TEMP_DOWNLOAD_DIRECTORY
import os
from telethon import events
import random
import numpy as np
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import pytz 
import asyncio
import requests
from PIL import Image, ImageDraw, ImageFont
from telegraph import upload_file
import time
import html
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from telethon.utils import get_input_location
import random

@tbot.on(events.NewMessage(pattern="^/logu (.*)"))
async def slogo(event):
    if event.sender_id in SUDO_USERS:
        pass
    elif event.sender_id == OWNER_ID:
        pass
    elif event.sender_id not in SUDO_USERS:
        await event.reply("Sed")
        return
    else:
        return
    quew = event.pattern_match.group(1)
    if "|" in quew:
        iid, reasonn = quew.split("|")
    cid = iid.strip()
    reason = reasonn.strip()
    await event.reply("`Processing..`")
    text = cid
    hmm = ("IMG_20210219_203337_228.jpg", "IMG_20210210_170521_219.jpg", "IMG_20210215_104759_504.jpg", "IMG_20210215_103846_312.jpg")
    fun = ("Vermin Vibes V.otf", "Blacksword.otf")
    lol = random.choice(hmm)
    test = random.choice(fun)
    img = Image.open(f'./resources/{lol}')
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 500
    fillcolor = "white"
    shadowcolor = "black"
    font = ImageFont.truetype(f"./resources/{test}", 200)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    n = ("black", "green", "red", "blue", "black", "lightgreen", "black", "violet", "orange", "yellow", "gold", "silver")
    col = random.choice(n)
    draw.text((x, y), text, font=font, fill=f"{reason}", stroke_width=8, stroke_fill=f"{col}")
    fname2 = "LogoBy@FRIDAYOT.png"
    img.save(fname2, "png")
    await borg.send_file(event.chat_id, fname2, caption="Made By Anie")
    if os.path.exists(fname2):
            os.remove(fname2)
