import logging
from os import getenv
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bot = None

async def set_commands(bot: Bot) -> None:
    commands = [
        {"command": "/start", "description": "Start the bot"},
        {"command": "/help", "description": "Get help"}
    ]
    await bot.set_my_commands(commands)

async def main() -> None:
    global bot
    TOKEN = getenv("BOT_TOKEN")
    if not TOKEN:
        logger.error("BOT_TOKEN is not set in the environment variables.")
        return

    bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    await set_commands(bot)

    logger.info("Starting bot...")

    try:
        await dp.start_polling()
    except Exception as e:
        logger.error(f"Polling failed: {e}")
    finally:
        await bot.session.close()

async def send_message(text: str) -> None:
    global bot
    if bot is None:
        raise RuntimeError("Bot is not initialized")
    chat_id = getenv("CHAT_ID")
    try:
        await bot.send_message(chat_id, text)
        logger.info(f"Message sent to Telegram: {text}")
    except Exception as e:
        logger.error(f"Failed to send message: {e}")
