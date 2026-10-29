from typing import List, Dict

POPULAR_STICKER_PACKS: List[Dict[str, str]] = [
    {
        "name": "🐰 Qiziqarli Quyoncha (Animated)",
        "set_name": "AnimatedBunny",
        "url": "https://t.me/addstickers/AnimatedBunny",
        "desc": "Juda chiroyli animatsiyali quyoncha stikerlari"
    },
    {
        "name": "🐱 Tom & Jerry",
        "set_name": "TomAndJerryMemes",
        "url": "https://t.me/addstickers/TomAndJerryMemes",
        "desc": "Kulgili va afsonaviy Tom va Jerri multfilm stikerlari"
    },
    {
        "name": "🔥 Pepe the Frog",
        "set_name": "ClassicPepeStickers",
        "url": "https://t.me/addstickers/ClassicPepeStickers",
        "desc": "Eng mashhur internet mem stikerlari"
    },
    {
        "name": "💻 Dasturchilar (Programmers)",
        "set_name": "ProgrammersLife",
        "url": "https://t.me/addstickers/ProgrammersLife",
        "desc": "IT va dasturchilar uchun maxsus hazil stikerlar"
    },
    {
        "name": "🐼 Kulgili Panda",
        "set_name": "PandaFunPacks",
        "url": "https://t.me/addstickers/PandaFunPacks",
        "desc": "Yoqimtoy animatsiyali pandalar"
    },
    {
        "name": "⚡ Anime Reaksiyalar",
        "set_name": "AnimeReactionsCollection",
        "url": "https://t.me/addstickers/AnimeReactionsCollection",
        "desc": "Mashhur animelardagi eng sara hissiyotlar"
    }
]

def format_sticker_info(sticker) -> str:
    """Yuborilgan stiker haqida to'liq ma'lumot matnini yaratadi"""
    st_type = "Oddiy (Static)"
    if sticker.is_animated:
        st_type = "Animatsiyali (Lottie Animated)"
    elif sticker.is_video:
        st_type = "Video Stiker (WEBM)"

    text = (
        "🎭 <b>STIKER MA'LUMOTLARI:</b>\n\n"
        f"🏷 <b>Emoji:</b> {sticker.emoji or 'Mavjud emas'}\n"
        f"📦 <b>To'plam nomi (Set Name):</b> <code>{sticker.set_name or 'Nomaʼlum toʻplam'}</code>\n"
        f"🎞 <b>Turi:</b> {st_type}\n"
        f"📐 <b>O'lchami:</b> {sticker.width}x{sticker.height}\n"
        f"📁 <b>Fayl hajmi:</b> {round(sticker.file_size / 1024, 2) if sticker.file_size else 'N/A'} KB\n"
        f"🆔 <b>File ID:</b>\n<code>{sticker.file_id}</code>\n\n"
    )

    if sticker.set_name:
        text += f"👉 <a href='https://t.me/addstickers/{sticker.set_name}'>To'plamni Telegramda ochish</a>"

    return text
