import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

# Қателерді бақылау үшін логтауды қосамыз
logging.basicConfig(level=logging.INFO)

# Токен орта айнымалыларынан алынады
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN орта айнымалысы көрсетілмеген!")

# Markdown қолдауымен ботты іске қосу
bot = Bot(
    token=BOT_TOKEN, 
    default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN)
)
dp = Dispatcher()

# Reply-пернетақтаны құру
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Біз туралы"), KeyboardButton(text="Бағыттар")],
        [KeyboardButton(text="Байланыс")]
    ],
    resize_keyboard=True
)

@dp.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer(
        "Жастар ресурстық орталығының ботына қош келдіңіз! Төмендегі мәзірден өзіңізге қажетті бөлімді таңдаңыз:",
        reply_markup=main_keyboard
    )

@dp.message(F.text == "Біз туралы")
async def about_handler(message: Message):
    text = (
        "🏢 *Біз туралы*\n\n"
        "Жастар ресурстық орталығы өңіріміздегі жастар саясатын дамытумен айналысады. "
        "Біз ақпараттық қолдау көрсетіп, сіздің бастамаларыңызды жүзеге асыруға көмектесеміз және "
        "маңызды мемлекеттік бағдарламаларға қолжетімділікті қамтамасыз етеміз."
    )
    await message.answer(text)

@dp.message(F.text == "Бағыттар")
async def directions_handler(message: Message):
    text = (
        "🎯 *Біздің жұмыс бағыттарымыз:*\n\n"
        "• *Жұмысқа орналастыру:* жұмыс табуға көмектесу, оның ішінде NEET санатындағы жастарды қолдау.\n"
        "• *Мемлекеттік бағдарламалар:* «Жастар практикасы» және «Бастау Бизнес» бағыттары бойынша қолдау.\n"
        "• *Кеңес беру:* тегін психологиялық және заңгерлік көмек.\n"
        "• *Волонтерлік:* еріктілер қозғалысын дамыту және қолдау."
    )
    await message.answer(text)

@dp.message(F.text == "Байланыс")
async def contacts_handler(message: Message):
    text = (
        "📞 *Байланыс*\n\n"
        "Біз ұсыныстар мен сұрақтар үшін әрқашан ашықпыз!\n"
        "Барлық өзекті ақпаратты біздің әлеуметтік желілердегі ресми парақшаларымыздан таба аласыз.\n\n"
        "_(Мұнда нақты мекенжайлар мен телефон нөмірлерін қосуды ұмытпаңыз)_"
    )
    await message.answer(text)

async def main():
    # Бот желіде болмаған кездегі жиналып қалған жаңартуларды өткізіп жіберу
    await bot.delete_webhook(drop_pending_updates=True)
    # Polling-ті іске қосу
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())