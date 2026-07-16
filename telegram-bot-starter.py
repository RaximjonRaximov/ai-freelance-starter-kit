#!/usr/bin/env python3
"""
Oddiy Telegram FAQ bot namunasi.
Mijoz uchun kichik biznes bot sifatida sotilishi mumkin.
BotFather orqali token olinadi.
"""

import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# BotFather dan olingan tokenni o'rnating
BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# FAQ ma'lumotlarini shu yerda o'zgartiring
FAQ = {
    "hours": "Biz har kuni 09:00 dan 21:00 gacha ochiqmiz.",
    "address": "Bizning manzil: [shahar, ko'cha, uy].",
    "price": "Narxlar bo'yicha @yourusername ga yozing.",
    "contact": "Aloqa: +998 xx xxx xx xx",
}


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "Assalomu alaykum! Men bizning avtomatik yordamchiman.\n"
        "Quyidagi tugmalar orqali kerakli ma'lumotni oling:"
    )


@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer(
        "Mavjud buyruqlar:\n"
        "/start - boshlash\n"
        "/hours - ish vaqti\n"
        "/address - manzil\n"
        "/price - narxlarni bilish\n"
        "/contact - aloqa\n"
    )


@dp.message(Command("hours"))
async def cmd_hours(message: types.Message):
    await message.answer(FAQ["hours"])


@dp.message(Command("address"))
async def cmd_address(message: types.Message):
    await message.answer(FAQ["address"])


@dp.message(Command("price"))
async def cmd_price(message: types.Message):
    await message.answer(FAQ["price"])


@dp.message(Command("contact"))
async def cmd_contact(message: types.Message):
    await message.answer(FAQ["contact"])


@dp.message()
async def echo(message: types.Message):
    await message.answer(
        "Tushunmadim. /help orqali buyruqlarni ko'rib chiqing yoki admin bilan bog'laning: @yourusername"
    )


async def main():
    if BOT_TOKEN == "YOUR_BOT_TOKEN_HERE":
        print("Iltimos, BOT_TOKEN o'rnating!")
        return
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
