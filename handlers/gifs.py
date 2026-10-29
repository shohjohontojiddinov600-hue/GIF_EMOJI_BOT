from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from keyboards.menu import get_gif_categories, get_gif_action_buttons
from data.gifs import get_random_gif, CURATED_GIFS

router = Router()

@router.message(F.text == "🎬 GIFlar")
async def show_gif_categories(message: Message):
    await message.answer(
        "🎬 <b>Qaysi mavzuda GIF qidiryapsiz?</b>\n\nQuyidagi kategoriyalardan birini tanlang:",
        reply_markup=get_gif_categories(),
        parse_mode="HTML"
    )

@router.callback_query(F.data == "gif_menu")
async def back_to_gif_menu(callback: CallbackQuery):
    await callback.message.edit_text(
        "🎬 <b>Qaysi mavzuda GIF qidiryapsiz?</b>\n\nQuyidagi kategoriyalardan birini tanlang:",
        reply_markup=get_gif_categories(),
        parse_mode="HTML"
    )
    await callback.answer()

@router.callback_query(F.data.startswith("gif_cat:"))
async def handle_gif_category(callback: CallbackQuery):
    category = callback.data.split(":")[1]
    
    gif_url = get_random_gif(category if category != "random" else None)
    cat_title = category.capitalize() if category != "random" else "Tasodifiy"

    await callback.answer("GIF yuklanmoqda...")
    
    try:
        await callback.message.answer_animation(
            animation=gif_url,
            caption=f"🎬 <b>Mavzu:</b> #{cat_title}",
            reply_markup=get_gif_action_buttons(category),
            parse_mode="HTML"
        )
    except Exception as e:
        # Agar URL yuklanishida Telegram cheklovi bo'lsa
        await callback.message.answer(
            f"🎬 <a href='{gif_url}'>GIFni ko'rish uchun bu erni bosing</a>\n\n<b>Mavzu:</b> #{cat_title}",
            reply_markup=get_gif_action_buttons(category),
            parse_mode="HTML"
        )
