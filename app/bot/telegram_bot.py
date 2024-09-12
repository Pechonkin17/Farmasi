import logging
from os import getenv
from aiogram import Bot, Dispatcher, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bot = None
router = Router()

@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"{hbold(message.from_user.full_name)}, вітаємо Вас у боті!")

async def send_registration_notification(message: str, bot_instance: Bot) -> None:
    chat_id = getenv("CHAT_ID")
    if not chat_id:
        logger.error("Помила з CHAT_ID")
        return

    try:
        await bot_instance.send_message(chat_id, message)
        logger.info(f"Повідомлення надіслано адміністратору: {message}")
    except Exception as e:
        logger.error(f"Помилка при відправці повідомлення адміну: {e}")

async def main() -> None:
    global bot
    TOKEN = getenv("BOT_TOKEN")
    if not TOKEN:
        logger.error("Помилка BOT_TOKEN")
        return

    bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    dp.include_router(router)

    try:
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"Бот не запустився: {e}")
    finally:
        await bot.session.close()

async def send_message(text: str) -> None:
    TOKEN = getenv("BOT_TOKEN")
    chat_id = getenv("CHAT_ID")
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN не задано")
    if not chat_id:
        raise RuntimeError("CHAT_ID не задано")

    bot_instance = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    try:
        await bot_instance.send_message(chat_id, text)
        logger.info(f"Повідомлення надіслано: {text}")
    except Exception as e:
        logger.error(f"Повідомлення не надіслано: {e}")
    finally:
        await bot_instance.session.close()
