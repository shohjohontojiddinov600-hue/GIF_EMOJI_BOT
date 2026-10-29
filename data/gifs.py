import random
import aiohttp
from typing import List, Dict

# Telegramda to'g'ridan-to'g'ri ishlaydigan saralangan GIF havolalari
CURATED_GIFS: Dict[str, List[str]] = {
    "kulgi": [
        "https://media.giphy.com/media/10JhviFuU2gWD6/giphy.gif",
        "https://media.giphy.com/media/ltIFdjNAasOwVvKhvx/giphy.gif",
        "https://media.giphy.com/media/Q7ozWVYCR0nyW2rvPW/giphy.gif",
        "https://media.giphy.com/media/bC9czlgCMtw4cj8RgH/giphy.gif",
        "https://media.giphy.com/media/lOadmkNRBxvlLf03KD/giphy.gif",
    ],
    "sevgi": [
        "https://media.giphy.com/media/26BRv0ThflsDTqUXa/giphy.gif",
        "https://media.giphy.com/media/OpfkuToK5NLig/giphy.gif",
        "https://media.giphy.com/media/l4pTdcifPZLpDjL1e/giphy.gif",
        "https://media.giphy.com/media/3o7TKoWXm3okO1kgHC/giphy.gif",
        "https://media.giphy.com/media/M90mJvfWfd5mbUuULX/giphy.gif",
    ],
    "reaksiya": [
        "https://media.giphy.com/media/5VKbvrjxpVJCM/giphy.gif",  # Wow
        "https://media.giphy.com/media/xT0xezQGU5xCDJuCPe/giphy.gif",  # Clapping
        "https://media.giphy.com/media/l3q2K5jinAlChoCLS/giphy.gif",  # Shocked
        "https://media.giphy.com/media/3o7btPCcdNniyf0ArS/giphy.gif",  # Thumbs up
        "https://media.giphy.com/media/d2lcHJTG5Tscg/giphy.gif",  # Cry
    ],
    "hayvonlar": [
        "https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif",  # Cat
        "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif",  # Cute dog
        "https://media.giphy.com/media/12bjQ7uASAaCKk/giphy.gif",  # Panda
        "https://media.giphy.com/media/BzyTuYCmvSORqs1ABM/giphy.gif",  # Dancing cat
        "https://media.giphy.com/media/MDJ9IbxxvDUQM/giphy.gif",
    ],
    "salom": [
        "https://media.giphy.com/media/dzaUX7CAG0Ihi/giphy.gif",
        "https://media.giphy.com/media/3pZipqyo1sqUCaA0bL/giphy.gif",
        "https://media.giphy.com/media/ASd0Ukj0BCcGqG45NP/giphy.gif",
        "https://media.giphy.com/media/Nx0rz3jtxt969jVKVY/giphy.gif",
    ],
    "bayram": [
        "https://media.giphy.com/media/artj92V8o75VPL7AeQ/giphy.gif",
        "https://media.giphy.com/media/g5R9dok94mrIvplmZd/giphy.gif",
        "https://media.giphy.com/media/26tOZ42Mg6pbTUPHW/giphy.gif",
        "https://media.giphy.com/media/yoJC2GnSClbPOkV0eA/giphy.gif",
    ],
    "anime": [
        "https://media.giphy.com/media/26gR2f01UTtnjWNsQ/giphy.gif",
        "https://media.giphy.com/media/11ISwbgCxEzMyY/giphy.gif",
        "https://media.giphy.com/media/kbuQOkUefLRqLuwQRVV/giphy.gif",
        "https://media.giphy.com/media/3oz8xAFtqoOUUrsh7W/giphy.gif",
    ]
}

def get_random_gif(category: str = None) -> str:
    """Berilgan kategoriya bo'yicha yoki tasodifiy GIF havolasini qaytaradi"""
    if category and category.lower() in CURATED_GIFS:
        return random.choice(CURATED_GIFS[category.lower()])
    
    all_gifs = [gif for gifs in CURATED_GIFS.values() for gif in gifs]
    return random.choice(all_gifs)

async def search_giphy_api(query: str, api_key: str = None, limit: int = 5) -> List[str]:
    """Giphy API orqali GIF qidirish (agar API kalit mavjud bo'lsa)"""
    if not api_key:
        # Agar maxsus API kalit bo'lmasa, qidiruv so'ziga mos kategoriyadan olamiz
        q = query.lower()
        for cat in CURATED_GIFS:
            if cat in q:
                return CURATED_GIFS[cat][:limit]
        return [get_random_gif() for _ in range(limit)]

    url = f"https://api.giphy.com/v1/gifs/search"
    params = {
        "api_key": api_key,
        "q": query,
        "limit": limit,
        "rating": "g"
    }
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params, timeout=5) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return [item["images"]["original"]["url"] for item in data.get("data", [])]
    except Exception as e:
        print(f"Giphy API xatoligi: {e}")
    
    return [get_random_gif() for _ in range(limit)]
