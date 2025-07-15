import asyncio
import logging
import os
import sys

# Защита от повторного запуска
lock_file = "bot.lock"

if os.path.exists(lock_file):
    print("⚠️ Бот уже запущен. Завершите предыдущий процесс.")
    sys.exit(1)

with open(lock_file, 'w') as f:
    f.write(str(os.getpid()))

import atexit
atexit.register(lambda: os.remove(lock_file))

# Логирование
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(os.path.join(LOG_DIR, "bot.log"), encoding="utf-8"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("TelegramBot")

# Точка входа
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
from handlers.menu import start_menu, button_handler

async def main():
    logger.info("🚀 Запуск бота...")
    try:
        from config import TELEGRAM_CONFIG
        app = ApplicationBuilder().token(TELEGRAM_CONFIG['token']).build()
        app.add_handler(CommandHandler("start", start_menu))
        app.add_handler(CallbackQueryHandler(button_handler))
        logger.info("✅ Бот успешно запущен")
        await app.run_polling()
    except Exception as e:
        logger.error("❌ Критическая ошибка", exc_info=True)

if __name__ == "__main__":
    asyncio.run(main())