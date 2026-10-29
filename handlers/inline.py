import hashlib
from aiogram import Router
from aiogram.types import (
    InlineQuery,
    InlineQueryResultGif,
    InlineQueryResultArticle,
    InputTextMessageContent
)
from data.gifs import CURATED_GIFS, get_random_gif
from data.emojis import EMOJI_CATEGORIES, EMOJI_COMBOS, EMOJI_ART

router = Router()

@router.inline_query()
async def inline_search(inline_query: InlineQuery):
    query = inline_query.query.strip().lower()
    results = []

    # 1. Agar foydalanuvchi qidiruv kiritgan bo'lsa
    found_gifs = []
    if query:
        for cat, gifs in CURATED_GIFS.items():
            if query in cat:
                found_gifs.extend(gifs)
    
    if not found_gifs:
        # Default barcha kategoriyalardan bir nechtadan olamiz
        for cat, gifs in CURATED_GIFS.items():
            found_gifs.append(gifs[0])
    
    # GIF natijalarini tayyorlash
    for i, gif_url in enumerate(found_gifs[:15]):
        result_id = hashlib.md5(f"gif_{gif_url}_{i}".encode()).hexdigest()
        results.append(
            InlineQueryResultGif(
                id=result_id,
                gif_url=gif_url,
                thumbnail_url=gif_url,
                title=f"🎬 GIF #{i+1}"
            )
        )

    # 2. Emojilar va Art natijalari
    for i, art in enumerate(EMOJI_ART[:4]):
        res_id = hashlib.md5(f"art_{i}".encode()).hexdigest()
        results.append(
            InlineQueryResultArticle(
                id=res_id,
                title=art["title"],
                description="Chiroyli Emoji Art rasmini yuborish",
                input_message_content=InputTextMessageContent(
                    message_text=f"<b>{art['title']}</b>\n\n<code>{art['art']}</code>",
                    parse_mode="HTML"
                )
            )
        )

    # 3. Emoji Kombinatsiyalari
    for i, combo in enumerate(EMOJI_COMBOS[:5]):
        res_id = hashlib.md5(f"combo_{i}".encode()).hexdigest()
        results.append(
            InlineQueryResultArticle(
                id=res_id,
                title=f"✨ {combo['combo']}",
                description=combo["meaning"],
                input_message_content=InputTextMessageContent(
                    message_text=f"✨ <b>{combo['combo']}</b>\n<i>{combo['meaning']}</i>",
                    parse_mode="HTML"
                )
            )
        )

    await inline_query.answer(results=results, cache_time=10, is_personal=True)
