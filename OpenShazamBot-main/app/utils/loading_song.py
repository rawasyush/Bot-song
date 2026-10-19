import os
from aiogram.types import FSInputFile

from app.config import config

MP3_PATH = "loading.mp3"
ID_FILE = "loading_song_id.txt"


async def ensure_loading_song(bot):
    """Purana expired URL hata kar local silent mp3 ka Telegram file_id use karta hai.

    Pehli baar mp3 ADMIN ko bhejta hai (file_id lene ke liye) aur turant delete kar deta hai.
    file_id loading_song_id.txt mein save hota hai, dobara upload nahi hota.
    """
    if os.path.exists(ID_FILE):
        with open(ID_FILE) as f:
            file_id = f.read().strip()
        if file_id:
            config.LOADING_SONG = file_id
            return

    try:
        msg = await bot.send_audio(config.ADMIN, FSInputFile(MP3_PATH), title="loading")
    except Exception as e:
        print(f"⚠️ Loading audio set nahi hua: {e}")
        print("➡️ app/config.py mein ADMIN apni Telegram ID karo aur bot ko ek baar /start karo.")
        return

    config.LOADING_SONG = msg.audio.file_id
    with open(ID_FILE, "w") as f:
        f.write(config.LOADING_SONG)
    try:
        await msg.delete()
    except Exception:
        pass
