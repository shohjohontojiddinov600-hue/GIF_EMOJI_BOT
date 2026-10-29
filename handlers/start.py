from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from keyboards.menu import get_main_menu

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    welcome_text = (
        f"Assalomu alaykum, <b>{message.from_user.full_name}</b>! 👋\n\n"
        "🌟 <b>GIF, Emoji va Stikerlar Botiga xush kelibsiz!</b>\n\n"
        "Ushbu bot orqali siz:\n"
        "🎬 Eng sara va kulgili <b>GIF</b>larni topishingiz\n"
        "😀 <b>Emoji</b>lar, Emoji Art va ma'noli kombinatsiyalarni ko'rishingiz\n"
        "🎭 <b>Stiker</b> to'plamlarini topish va har qanday stiker haqida to'liq ma'lumot olishingiz\n"
        "🎲 Tasodifiy qiziqarli media kontentlardan bahramand bo'lishingiz mumkin!\n\n"
        "<i>Quyidagi menyudan kerakli bo'limni tanlang:</i>"
    )
    await message.answer(welcome_text, reply_markup=get_main_menu(), parse_mode="HTML")

@router.message(Command("help"))
@router.message(F.text == "ℹ️ Bot haqida")
async def cmd_help(message: Message):
    help_text = (
        "🤖 <b>Bot imkoniyatlari haqida:</b>\n\n"
        "1️⃣ <b>GIFlar</b> - Kategoriya bo'yicha GIFlar qidirish va do'stlarga yuborish.\n"
        "2️⃣ <b>Emojilar</b> - Chiroyli Emoji Art rasmlari, emojilar va qiziqarli kombinatsiyalar.\n"
        "3️⃣ <b>Stikerlar</b> - Mashhur stiker paketlari. Shuningdek, botga <b>har qanday stiker</b> yuborsangiz, uning File IDsi va to'plam havolasini chiqarib beradi.\n"
        "4️⃣ <b>Inline rejim</b> - Istalgan chatda bot nomini yozib (masalan: <code>@bot_nomi salom</code>), darhol GIF yoki emoji yuborishingiz mumkin!\n\n"
        "👨‍💻 <i>Yaratuvchi: Shohjohon Tojiddinov</i>\n"
        "🚀 <i>aiogram 3x asosida yaratilgan</i>"
    )
    await message.answer(help_text, reply_markup=get_main_menu(), parse_mode="HTML")

@router.message(F.text == "🔍 Inline rejim")
async def inline_info(message: Message):
    bot_info = await message.bot.get_me()
    text = (
        "🔎 <b>Inline rejimdan foydalanish:</b>\n\n"
        "Siz ushbu botni istalgan guruh yoki shaxsiy yozishmalarda to'g'ridan-to'g'ri ishlatishingiz mumkin!\n\n"
        f"<b>Qanday ishlatiladi:</b>\n"
        f"1. Istalgan chatda <code>@{bot_info.username} </code> deb yozing\n"
        f"2. Qidiruv so'zini kiriting (masalan: <code>@{bot_info.username} kulgi</code> yoki <code>@{bot_info.username} sevgi</code>)\n"
        f"3. Chiqqan GIF yoki emojini tanlab bosing va u darhol yuboriladi!\n\n"
        "<i>💡 Eslatma: Inline rejim ishlashi uchun @BotFather da Inline Mode yoqilgan bo'lishi kerak.</i>"
    )
    await message.answer(text, parse_mode="HTML")
