import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from config import BOT_TOKEN
from handlers import start, gifs, emojis, stickers, random_content, inline

# Loglarni sozlash
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

async def main():
    if not BOT_TOKEN:
        logger.error("XATOLIK: BOT_TOKEN aniqlanmadi! .env faylini tekshiring.")
        return

    # Bot obyektini yaratish
    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    
    # Dispatcher obyektini yaratish
    dp = Dispatcher()

    # Routerlarni ulash
    dp.include_router(start.router)
    dp.include_router(gifs.router)
    dp.include_router(emojis.router)
    dp.include_router(stickers.router)
    dp.include_router(random_content.router)
    dp.include_router(inline.router)

    # Eski kutilayotgan xabarlarni tozalash (polling boshlanishidan oldin)
    await bot.delete_webhook(drop_pending_updates=True)

    bot_info = await bot.get_me()
    logger.info(f"Bot muvaffaqiyatli ishga tushdi: @{bot_info.username}")
    print(f"\n===========================================")
    print(f"✅ Bot ishga tushdi: @{bot_info.username}")
    print(f"👉 Telegramda botni ochish: https://t.me/{bot_info.username}")
    print(f"===========================================\n")

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot to'xtatildi!")
