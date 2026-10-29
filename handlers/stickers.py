from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.menu import get_stickers_menu
from data.stickers import POPULAR_STICKER_PACKS, format_sticker_info

router = Router()

@router.message(F.text == "🎭 Stikerlar")
async def show_stickers_menu(message: Message):
    text = (
        "🎭 <b>Stikerlar Bo'limi!</b>\n\n"
        "💡 <b>Bot imkoniyatlari:</b>\n"
        "1. Mashhur va eng chiroyli stiker to'plamlari katalogi\n"
        "2. Har qanday stikerni botga yuborib, uning <b>File ID</b> va <b>to'plam havolasini</b> aniqlash!\n\n"
        "<i>Kerakli amalni tanlang yoki shunchaki menga stiker yuboring:</i>"
    )
    await message.answer(text, reply_markup=get_stickers_menu(), parse_mode="HTML")

@router.callback_query(F.data == "sticker_packs")
async def list_sticker_packs(callback: CallbackQuery):
    text = "📦 <b>Tavsiya etiladigan sara stiker to'plamlari:</b>\n\n"
    
    keyboard = []
    for pack in POPULAR_STICKER_PACKS:
        text += f"• <b>{pack['name']}</b>\n  <i>{pack['desc']}</i>\n\n"
        keyboard.append([
            InlineKeyboardButton(text=f"➕ {pack['name']}", url=pack['url'])
        ])
    
    keyboard.append([
        InlineKeyboardButton(text="⬅️ Stiker menyusi", callback_data="back_to_sticker_menu")
    ])
    
    await callback.message.edit_text(
        text, 
        reply_markup=InlineKeyboardMarkup(inline_keyboard=keyboard),
        parse_mode="HTML"
    )
    await callback.answer()

@router.callback_query(F.data == "sticker_id_info")
async def info_sticker_id(callback: CallbackQuery):
    text = (
        "🔎 <b>Stiker ma'lumotlarini aniqlash juda oson!</b>\n\n"
        "Menga istalgan bitta stikerni yuboring.\n"
        "Men sizga uning:\n"
        "• Telegram File ID sini\n"
        "• Qaysi to'plamga tegishli ekanligini\n"
        "• Qo'shish havolasini (Add link)\n"
        "• Emotsiya (Emoji) bog'liqligini ko'rsatib beraman!"
    )
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬅️ Orqaga", callback_data="back_to_sticker_menu")]
    ])
    await callback.message.edit_text(text, reply_markup=kb, parse_mode="HTML")
    await callback.answer()

@router.callback_query(F.data == "back_to_sticker_menu")
async def back_to_sticker_menu(callback: CallbackQuery):
    text = (
        "🎭 <b>Stikerlar Bo'limi!</b>\n\n"
        "Kerakli bo'limni tanlang yoki botga to'g'ridan-to'g'ri stiker yuboring:"
    )
    await callback.message.edit_text(text, reply_markup=get_stickers_menu(), parse_mode="HTML")
    await callback.answer()

@router.message(F.sticker)
async def handle_incoming_sticker(message: Message):
    """Foydalanuvchi yuborgan stikerni tahlil qilib ma'lumot beradi"""
    sticker = message.sticker
    info_text = format_sticker_info(sticker)
    
    kb = None
    if sticker.set_name:
        kb = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="📥 To'plamni qo'shish", url=f"https://t.me/addstickers/{sticker.set_name}")]
        ])
    
    await message.reply(info_text, reply_markup=kb, parse_mode="HTML", disable_web_page_preview=True)
