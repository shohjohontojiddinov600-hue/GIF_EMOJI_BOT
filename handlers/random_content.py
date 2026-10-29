from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.menu import get_random_menu, get_gif_action_buttons
from data.gifs import get_random_gif
from data.emojis import get_random_emoji, get_random_emoji_art, get_random_emoji_combo

router = Router()

@router.message(F.text == "🎲 Tasodifiy")
async def show_random_menu(message: Message):
    text = (
        "🎲 <b>Tasodifiy kontent tanlash bo'limi!</b>\n\n"
        "O'zingizga qiziq bo'lganini tanlang va kayfiyatingizni ko'taring:"
    )
    await message.answer(text, reply_markup=get_random_menu(), parse_mode="HTML")

@router.callback_query(F.data == "rand_gif")
async def handle_random_gif(callback: CallbackQuery):
    gif_url = get_random_gif()
    await callback.answer()
    try:
        await callback.message.answer_animation(
            animation=gif_url,
            caption="🎲 <b>Tasodifiy GIF!</b>",
            reply_markup=get_gif_action_buttons("random"),
            parse_mode="HTML"
        )
    except Exception:
        await callback.message.answer(
            f"🎬 <a href='{gif_url}'>Tasodifiy GIFni ko'rish</a>",
            reply_markup=get_gif_action_buttons("random"),
            parse_mode="HTML"
        )

@router.callback_query(F.data == "rand_emoji")
async def handle_random_emoji(callback: CallbackQuery):
    emoji = get_random_emoji()
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔄 Yana bitta emoji", callback_data="rand_emoji")]
    ])
    await callback.message.answer(f"🎲 <b>Tasodifiy Emoji:</b>\n\n{emoji}", reply_markup=kb, parse_mode="HTML")
    await callback.answer()

@router.callback_query(F.data == "rand_art")
async def handle_rand_art(callback: CallbackQuery):
    art_item = get_random_emoji_art()
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔄 Yana bitta art", callback_data="rand_art")]
    ])
    text = f"🎨 <b>{art_item['title']}</b>\n\n<code>{art_item['art']}</code>"
    await callback.message.answer(text, reply_markup=kb, parse_mode="HTML")
    await callback.answer()

@router.callback_query(F.data == "rand_combo")
async def handle_rand_combo(callback: CallbackQuery):
    combo = get_random_emoji_combo()
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔄 Boshqa kombinatsiya", callback_data="rand_combo")]
    ])
    text = f"🧩 <b>Kombinatsiya:</b> {combo['combo']}\n💬 <b>Ma'nosi:</b> <i>{combo['meaning']}</i>"
    await callback.message.answer(text, reply_markup=kb, parse_mode="HTML")
    await callback.answer()
