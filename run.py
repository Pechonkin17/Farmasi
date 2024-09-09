import threading
import asyncio
from app import create_app
from app.bot.telegram_bot import main as bot_main

def run_flask():
    app = create_app()
    app.run(debug=True, use_reloader=False)

def run_bot():
    try:
        asyncio.run(bot_main())
    except Exception as e:
        print(f"Failed to start bot: {e}")

if __name__ == "__main__":
    flask_thread = threading.Thread(target=run_flask)
    bot_thread = threading.Thread(target=run_bot)

    flask_thread.start()
    bot_thread.start()

    flask_thread.join()
    bot_thread.join()



"""
        1. Підписатися на розсилку - форма 'підпишіться на бот щоб бути в курсі усіх новин' і перекинути в телеграм бот + 
        2. Зробити ввід тільки цифр - або 10 або 12 і знак `+` +
        3. Створити бота, який надсилатиме розсилку
        4. Захостити сайт і бота 
        5. Шифрування даних в базі даних
        6. Поміняти пароль в базі даних
        6. Шрифти, розташування контенту
"""