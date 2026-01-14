from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

TOKEN = "8097504031:AAHd-YXhxyXqYblWf1YH8V0H1M9NGGHWwMM"
GROUP_ID = -1002048724865  # BU YERGA GURUH ID

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['post'])
async def send_post(message: types.Message):
    # Faqat guruhda ishlash
    if message.chat.id != GROUP_ID:
        return

    # Admin tekshirish
    member = await bot.get_chat_member(GROUP_ID, message.from_user.id)
    if member.is_chat_admin() or member.status == "creator":
        text = message.text.replace("/post", "").strip()
        if text:
            await bot.send_message(GROUP_ID, f"📢 Post:\n\n{text}")
        else:
            await message.reply("✍️ Post matnini yozing:\n/post Bugun yangilik bor")
    else:
        await message.reply("❌ Faqat adminlar post yuborishi mumkin")

if __name__ == "__main__":
    executor.start_polling(dp)



