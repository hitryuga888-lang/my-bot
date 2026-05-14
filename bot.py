import asyncio
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Кнопки социальных сетей
def get_social_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Instagram", url="https://www.instagram.com/ten_june_rest/"),
            InlineKeyboardButton(text="VK", url="https://vk.com/tenjune_rest"),
        ],
        [
            InlineKeyboardButton(text="Telegram", url="https://t.me/TenJune_Rostov"),
            InlineKeyboardButton(text="Сделать заказ", url="https://eda.yandex.ru/r/ten_june"),
        ]
    ])
    return keyboard

# Команда /start
@dp.message(CommandStart())
async def start(message: types.Message):
    text = "Здравствуйте. Бот на данный момент находится в стадии разработки. О его запуске вы узнаете из социальных сетей"
    photo_url = "https://optim.tildacdn.com/tild6330-3238-4237-b939-653031623161/-/resize/420x/-/format/webp/_13.jpg.webp"
    
    await message.answer_photo(
        photo=photo_url,
        caption=text,
        reply_markup=get_social_keyboard()
    )

async def main():
    print("Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())