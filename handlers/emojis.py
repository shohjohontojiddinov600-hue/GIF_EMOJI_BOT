from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.menu import get_emoji_menu
from data.emojis import (
    EMOJI_CATEGORIES, 
    get_random_emoji, 
    get_random_emoji_art, 
    get_random_emoji_combo
)

router = Router()

@router.message(F.text == "😀 Emojilar")
async def show_emoji_menu(message: Message):
    text = (
        "😀 <b>Emojilar olamiga xush kelibsiz!</b>\n\n"
        "Bu yerda siz turli toifadagi emojilar, qiziqarli kombinatsiyalar "
        "va chiroyli Emoji Art san'at namunalarini topishingiz mumkin.\n\n"
        "<i>Kerakli bo'limni tanlang:</i>"
    )
    await message.answer(text, reply_markup=get_emoji_menu(), parse_mode="HTML")

@router.callback_query(F.data == "emoji_art")
async def handle_emoji_art(callback: CallbackQuery):
    art_item = get_random_emoji_art()
    text = (
        f"🎨 <b>{art_item['title']}</b>\n\n"
        f"<code>{art_item['art']}</code>\n\n"
        "<i>Nusxa olish uchun ustiga bosing!</i>"
    )
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="🔄 Yana Art", callback_data="emoji_art"),
            InlineKeyboardButton(text="⬅️ Emojilar menyusi", callback_data="back_to_emoji_menu")
        ]
    ])
    await callback.message.answer(text, reply_markup=kb, parse_mode="HTML")
    await callback.answer()

@router.callback_query(F.data == "emoji_combo")
async def handle_emoji_combo(callback: CallbackQuery):
    combo_item = get_random_emoji_combo()
    text = (
        "🧩 <b>Emoji Kombinatsiyasi:</b>\n\n"
        f"✨ <b>{combo_item['combo']}</b>\n"
        f"💬 <b>Ma'nosi:</b> <i>{combo_item['meaning']}</i>"
    )
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="🔄 Boshqa kombinatsiya", callback_data="emoji_combo"),
            InlineKeyboardButton(text="⬅️ Emojilar menyusi", callback_data="back_to_emoji_menu")
        ]
    ])
    await callback.message.answer(text, reply_markup=kb, parse_mode="HTML")
    await callback.answer()

@router.callback_query(F.data.startswith("emoji_cat:"))
async def handle_emoji_category(callback: CallbackQuery):
    cat = callback.data.split(":")[1]
    
    if cat == "random":
        emoji = get_random_emoji()
        text = f"🎲 <b>Tasodifiy Emoji:</b>\n\n{emoji}"
    else:
        emojis_list = EMOJI_CATEGORIES.get(cat, [])
        emojis_text = "  ".join(emojis_list)
        text = (
            f"🏷 <b>Mavzu:</b> #{cat.capitalize()}\n\n"
            f"{emojis_text}\n\n"
            "<i>Nusxalash uchun istalgan emojini tanlab oling!</i>"
        )

    kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="🔄 Yana ko'rish", callback_data=f"emoji_cat:{cat}"),
            InlineKeyboardButton(text="⬅️ Menyuga qaytish", callback_data="back_to_emoji_menu")
        ]
    ])
    await callback.message.answer(text, reply_markup=kb, parse_mode="HTML")
    await callback.answer()

@router.callback_query(F.data == "back_to_emoji_menu")
async def back_to_emoji_menu(callback: CallbackQuery):
    text = (
        "😀 <b>Emojilar bo'limi:</b>\n\n"
        "O'zingizga ma'qul bo'lgan toifani tanlang:"
    )
    await callback.message.edit_text(text, reply_markup=get_emoji_menu(), parse_mode="HTML")
    await callback.answer()
