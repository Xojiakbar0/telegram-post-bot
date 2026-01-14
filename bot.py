import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.enums import ChatMemberStatus

TOKEN = "BU_YERGA_TOKEN"
GROUP_ID = -1002048724865  # BU YERGA GURUH ID

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def is_admin(user_id: int):
    member = await bot.get_chat_member(GROUP_ID, user_id)
    return member.status in (
        ChatMemberStatus.ADMINISTRATOR,
        ChatMemberStatus.OWNER
    )

@dp.message(Command("post"))
async def post_handler(message: types.Message):
    if message.chat.id != GROUP_ID:
        return

    if not await is_admin(message.from_user.id):
        await message.reply("❌ Faqat adminlar post joylay oladi")
        return

    text = message.text.replace("/post", "").strip()
    if not text:
        await message.reply("✍️ Matn yozing:\n/post Bugun aksiya bor")
        return

    post = f"""
🔥 <b>YANGI E'LON!</b>

{text}

⏰ Shoshiling!
#elon #yangilik
"""

    await bot.send_message(
        GROUP_ID,
        post,
        parse_mode="HTML"
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

