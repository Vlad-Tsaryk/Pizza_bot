import os
from aiogram.dispatcher.filters import Text
import logic

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, KeyboardButton
from dotenv import load_dotenv

load_dotenv()

# API key
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot)

user_values = {}


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton(text="Choose pizza")
    keyboard.add(button)
    with open(f'pizza bot.png', 'rb') as photo:
        await message.answer_photo(photo=photo)
    await message.answer("Hello, i'm pizza bot.\nI can help you to choose pizza for you)))", reply_markup=keyboard)


@dp.message_handler(Text(equals="Choose pizza"))
async def send_welcome(message: types.Message):
    buttons = [
        InlineKeyboardButton(text="Spicy", callback_data="taste_spicy"),
        InlineKeyboardButton(text="Umami", callback_data="taste_umami"),
        InlineKeyboardButton(text="Sweet and sour", callback_data="taste_sour_sweet")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.answer("Choose taste for your pizza: ", reply_markup=keyboard)


@dp.callback_query_handler(Text(startswith="taste_"))
async def callbacks_taste(call: types.CallbackQuery):
    action = call.data
    if action == "taste_spicy":
        user_values['taste_val'] = 24
    elif action == "taste_umami":
        user_values['taste_val'] = 52
    elif action == "taste_sour_sweet":
        user_values['taste_val'] = 73
    buttons = [
        InlineKeyboardButton(text="Low", callback_data="cheese_low"),
        InlineKeyboardButton(text="Middle", callback_data="cheese_mid"),
        InlineKeyboardButton(text="High", callback_data="cheese_high")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await call.message.edit_text(text='Select amount of cheese: ', reply_markup=keyboard)
    await call.answer()


@dp.callback_query_handler(Text(startswith="cheese_"))
async def callbacks_taste(call: types.CallbackQuery):
    action = call.data
    if action == "cheese_low":
        user_values['cheese_val'] = 3
    elif action == "cheese_mid":
        user_values['cheese_val'] = 6
    elif action == "cheese_high":
        user_values['cheese_val'] = 9
    buttons = [
        InlineKeyboardButton(text="1$ - 2$", callback_data="price_low"),
        InlineKeyboardButton(text="2$ - 5$", callback_data="price_mid"),
        InlineKeyboardButton(text=">5$", callback_data="price_high")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await call.message.edit_text(text='Select price: ', reply_markup=keyboard)
    await call.answer()


@dp.callback_query_handler(Text(startswith="price_"))
async def callbacks_taste(call: types.CallbackQuery):
    action = call.data
    if action == "price_low":
        user_values['price_val'] = 45
    elif action == "price_mid":
        user_values['price_val'] = 63
    elif action == "price_high":
        user_values['price_val'] = 89
    await call.message.edit_text(text=f'Your pizza:')
    caption = logic.fuzzy_l(**user_values)
    with open(f'{caption}.jpg', 'rb') as photo:
        await call.message.answer_photo(photo=photo, caption=caption)
    await call.answer()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
