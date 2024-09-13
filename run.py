import threading
import asyncio
from app import create_app
from app.bot.telegram_bot import main as bot_main

def run_flask():
    app = create_app()
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=5000)

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