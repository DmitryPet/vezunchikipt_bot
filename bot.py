import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
import os
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

users = {}

main_kb = ReplyKeyboardMarkup(resize_keyboard=True)
main_kb.add(KeyboardButton("🚗 Ищу попутку"), KeyboardButton("📦 Передать посылку"))
main_kb.add(KeyboardButton("🏖 Хочу к океану"), KeyboardButton("🛒 Заезд в магазины"))
main_kb.add(KeyboardButton("💬 Советы и логистика"), KeyboardButton("✍️ Настроить профиль"))

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    users[message.from_user.id] = {"name": message.from_user.full_name}
    await message.answer("Привет! Я бот ВЕЗУНчик 🤝\nЧем займёмся?", reply_markup=main_kb)

@dp.message_handler(lambda message: message.text == "✍️ Настроить профиль")
async def profile_setup(message: types.Message):
    await message.answer("Напиши город, в котором ты живёшь:")

@dp.message_handler(lambda message: message.text == "🚗 Ищу попутку")
async def find_ride(message: types.Message):
    await message.answer("Укажи маршрут и дату поездки. Я постараюсь найти тебе попутчиков!")

@dp.message_handler(lambda message: message.text == "📦 Передать посылку")
async def send_package(message: types.Message):
    await message.answer("Напиши откуда и куда передать посылку. Добавь дату, если важно.")

@dp.message_handler(lambda message: message.text == "🏖 Хочу к океану")
async def to_beach(message: types.Message):
    await message.answer("Красавчик! Я сообщу всем, кто тоже хочет к океану 🌊")

@dp.message_handler(lambda message: message.text == "🛒 Заезд в магазины")
async def to_shops(message: types.Message):
    await message.answer("Напиши, в какой магазин и город ты хочешь заехать, и когда.")

@dp.message_handler(lambda message: message.text == "💬 Советы и логистика")
async def logistics_tips(message: types.Message):
    await message.answer("Спроси про маршрут, парковку или поделись лайфхаком!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)