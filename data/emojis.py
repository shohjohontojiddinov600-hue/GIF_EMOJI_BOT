import random
from typing import Dict, List

EMOJI_CATEGORIES: Dict[str, List[str]] = {
    "quvonch": ["😀", "😃", "😄", "😁", "😆", "😅", "😂", "🤣", "😊", "😇", "🥳", "🤩"],
    "sevgi": ["❤️", "💖", "💕", "💞", "💓", "💗", "💘", "💝", "😍", "🥰", "😘", "😻"],
    "hayrat": ["😮", "😯", "😲", "😳", "🤯", "😱", "🙀", "😶‍🌫️", "🧐"],
    "kulgili": ["🤪", "😜", "😝", "😛", "🤡", "🤖", "👻", "👽", "👾", "🐒"],
    "hayvonlar": ["🐱", "🐶", "🦁", "🐯", "🐼", "🐨", "🦊", "🐰", "🐻", "🦄", "🦅", "🐬"],
    "taom": ["🍕", "🍔", "🍟", "🌭", "🍿", "🍩", "🍦", "🎂", "🍫", "🍓", "☕", "🧋"],
    "faoliyat": ["⚽", "🏀", "🎮", "🎯", "🎸", "🎧", "🎬", "🎨", "🚀", "🏆", "💎", "🔥"],
}

EMOJI_COMBOS: List[Dict[str, str]] = [
    {"combo": "🍿 + 🎬 + 🛋️", "meaning": "Kino oqshomi va miriqib dam olish"},
    {"combo": "☕ + 📖 + 🌧️", "meaning": "Yomg'irli kunda kitob va issiq qahva"},
    {"combo": "💻 + ☕ + 🎧", "meaning": "Dasturlash va sokin musiqa"},
    {"combo": "🍕 + 🎮 + 🕺", "meaning": "Do'stlar bilan o'yin kechasi"},
    {"combo": "🏖️ + 🍹 + 🕶️", "meaning": "Dengiz bo'yida unutilmas ta'til"},
    {"combo": "🚀 + 🌌 + 🛸", "meaning": "Koinot sirlari va parvoz"},
    {"combo": "🎂 + 🎉 + 🎁", "meaning": "Tug'ilgan kun muborak bo'lsin!"},
    {"combo": "🚗 + 🛣️ + 🌅", "meaning": "Quyosh botishida ajoyib sayohat"},
    {"combo": "💪 + 🏋️ + 🥗", "meaning": "Sog'lom hayot va fitnes mashg'ulotlari"},
    {"combo": "🧠 + 💡 + ✨", "meaning": "Yangi g'oya va ijodiy ilhom"},
]

EMOJI_ART: List[Dict[str, str]] = [
    {
        "title": "❤️ Sevgi Yurak Art",
        "art": (
            "⬜🟥🟥⬜🟥🟥⬜\n"
            "🟥🟥🟥🟥🟥🟥🟥\n"
            "🟥🟥🟥🟥🟥🟥🟥\n"
            "⬜🟥🟥🟥🟥🟥⬜\n"
            "⬜⬜🟥🟥🟥⬜⬜\n"
            "⬜⬜⬜🟥⬜⬜⬜"
        )
    },
    {
        "title": "🌟 Yulduz Art",
        "art": (
            "⬜⬜⬜⭐⬜⬜⬜\n"
            "⬜⬜⭐⭐⭐⬜⬜\n"
            "⭐⭐⭐⭐⭐⭐⭐\n"
            "⬜⭐⭐⭐⭐⭐⬜\n"
            "⬜⭐⬜⬜⬜⭐⬜"
        )
    },
    {
        "title": "☕ Qahva Art",
        "art": (
            "⬜⬜♨️⬜♨️⬜⬜\n"
            "⬜⬜♨️⬜♨️⬜⬜\n"
            "⬜🟫🟫🟫🟫⬜⬜\n"
            "⬜🟫🟫🟫🟫🟫⬜\n"
            "⬜🟫🟫🟫🟫⬜⬜\n"
            "⬜⬜🟫🟫⬜⬜⬜\n"
            "⬜🟫🟫🟫🟫⬜⬜"
        )
    },
    {
        "title": "🎂 Bayramona Tort Art",
        "art": (
            "⬜⬜🕯️⬜🕯️⬜⬜\n"
            "⬜⬜🍓⬜🍓⬜⬜\n"
            "⬜🟨🟨🟨🟨🟨⬜\n"
            "⬜🟫🟫🟫🟫🟫⬜\n"
            "🟨🟨🟨🟨🟨🟨🟨\n"
            "🟫🟫🟫🟫🟫🟫🟫"
        )
    }
]

def get_random_emoji_combo() -> Dict[str, str]:
    return random.choice(EMOJI_COMBOS)

def get_random_emoji_art() -> Dict[str, str]:
    return random.choice(EMOJI_ART)

def get_random_emoji(category: str = None) -> str:
    if category and category.lower() in EMOJI_CATEGORIES:
        return random.choice(EMOJI_CATEGORIES[category.lower()])
    all_emojis = [e for group in EMOJI_CATEGORIES.values() for e in group]
    return random.choice(all_emojis)
