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
    text = "🎬 <b>Qaysi mavzuda GIF qidiryapsiz?</b>\n\nQuyidagi kategoriyalardan birini tanlang:"
    try:
        # Agar xabar oddiy matn bo'lsa uni tahrirlaymiz
        await callback.message.edit_text(text, reply_markup=get_gif_categories(), parse_mode="HTML")
    except Exception:
        # Agar xabar animatsiya bo'lsa, eskisini o'chirib yangi menyu chiqaramiz
        try:
            await callback.message.delete()
        except Exception:
            pass
        await callback.message.answer(text, reply_markup=get_gif_categories(), parse_mode="HTML")
    await callback.answer()

@router.callback_query(F.data.startswith("gif_cat:"))
async def handle_gif_category(callback: CallbackQuery):
    category = callback.data.split(":")[1]
    cat_title = category.capitalize() if category != "random" else "Tasodifiy"

    await callback.answer("GIF yuklanmoqda...")

    # Bir necha urinish bilan GIF yuborish (ishonchli ishlashi uchun)
    sent = False
    for _ in range(3):
        gif_url = get_random_gif(category if category != "random" else None)
        try:
            await callback.message.answer_animation(
                animation=gif_url,
                caption=f"🎬 <b>Mavzu:</b> #{cat_title}",
                reply_markup=get_gif_action_buttons(category),
                parse_mode="HTML"
            )
            sent = True
            break
        except Exception:
            continue

    if not sent:
        fallback_url = "https://media.giphy.com/media/10JhviFuU2gWD6/giphy.gif"
        try:
            await callback.message.answer_animation(
                animation=fallback_url,
                caption=f"🎬 <b>Mavzu:</b> #{cat_title}",
                reply_markup=get_gif_action_buttons(category),
                parse_mode="HTML"
            )
        except Exception:
            await callback.message.answer(
                f"🎬 <a href='{fallback_url}'>GIFni ochish</a>\n\n<b>Mavzu:</b> #{cat_title}",
                reply_markup=get_gif_action_buttons(category),
                parse_mode="HTML"
            )
