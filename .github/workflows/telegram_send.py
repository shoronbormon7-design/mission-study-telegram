import os
import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

API_ID = int(os.environ["TELEGRAM_API_ID"])
API_HASH = os.environ["TELEGRAM_API_HASH"]
SESSION = os.environ["TELEGRAM_SESSION"]
POST_TIME = os.environ["POST_TIME"]

POSTS = {
    "05:00": """📚 **Everyone Study Mood On ❤️❤️**

🔴 **Live Study Link 🥳:**
[https://t.me/mission_study_official?livestream=dc75a890c19345472f](https://t.me/mission_study_official?livestream=dc75a890c19345472f)

🤍 **Our Website:**
[https://missionstudyofficial.blogspot.com](https://missionstudyofficial.blogspot.com)

⚠️ **Note:**
Everyone, Website-এ **Timer ON** রেখে Study করবেন ❤️
রাতে সবার **Study History** দেখা হবে 👈""",

    "13:00": """⏸️ **Everyone, Break Time! ❤️**

🕐 **1:00 PM — 2:00 PM**

Take some rest, recharge yourself, and get ready for the next study session. 📚✨""",

    "14:00": """⏰ **Break Time End! ❤️**

📚 **Everyone Study Mood On ❤️❤️**

🥳 **Live Study Link:**
[https://t.me/mission_study_official?livestream=dc75a890c19345472f](https://t.me/mission_study_official?livestream=dc75a890c19345472f)

🤍 **Our Website:**
[https://missionstudyofficial.blogspot.com](https://missionstudyofficial.blogspot.com)

⚠️ **Note:**
Website-এ **Timer ON** রেখে Study করবেন ❤️
রাতে সবার **Study History** দেখা হবে 👈""",

    "22:00": """🎯 **Everyone, Today’s Target Complete! ❤️**

সবাই নিজের Website-এর **Study History-এর Screenshot** দিয়ে দেখাও। 📸❤️

⏰ **আবার দেখা হচ্ছে কাল সকাল ৫টা থেকে...** ✅✅✅

👥 **Group Link:**
[https://t.me/mission_study_official_group](https://t.me/mission_study_official_group)"""
}


if POST_TIME not in POSTS:
    raise ValueError(f"Invalid POST_TIME: {POST_TIME}")


async def main():
    async with TelegramClient(
        StringSession(SESSION),
        API_ID,
        API_HASH
    ) as client:

        if not await client.is_user_authorized():
            raise RuntimeError("Telegram session is not authorized.")

        await client.send_message(
            "@mission_study_official",
            POSTS[POST_TIME],
            parse_mode="md"
        )

        print(f"Posted successfully: {POST_TIME}")


if __name__ == "__main__":
    asyncio.run(main())
