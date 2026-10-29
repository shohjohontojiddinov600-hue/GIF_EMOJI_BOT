from aiogram.types import (
    ReplyKeyboardMarkup, 
    KeyboardButton, 
    InlineKeyboardMarkup, 
    InlineKeyboardButton
)

def get_main_menu() -> ReplyKeyboardMarkup:
    """Asosiy menyu tugmalari"""
    keyboard = [
        [
            KeyboardButton(text="🎬 GIFlar"),
            KeyboardButton(text="😀 Emojilar")
        ],
        [
            KeyboardButton(text="🎭 Stikerlar"),
            KeyboardButton(text="🎲 Tasodifiy")
        ],
        [
            KeyboardButton(text="🔍 Inline rejim"),
            KeyboardButton(text="ℹ️ Bot haqida")
        ]
    ]
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
        input_field_placeholder="Kerakli bo'limni tanlang..."
    )

def get_gif_categories() -> InlineKeyboardMarkup:
    """GIF kategoriyalari inline tugmalari"""
    keyboard = [
        [
            InlineKeyboardButton(text="😂 Kulgi", callback_data="gif_cat:kulgi"),
            InlineKeyboardButton(text="❤️ Sevgi", callback_data="gif_cat:sevgi")
        ],
        [
            InlineKeyboardButton(text="😮 Reaksiyalar", callback_data="gif_cat:reaksiya"),
            InlineKeyboardButton(text="🐱 Hayvonlar", callback_data="gif_cat:hayvonlar")
        ],
        [
            InlineKeyboardButton(text="👋 Salomlashish", callback_data="gif_cat:salom"),
            InlineKeyboardButton(text="🎉 Bayram", callback_data="gif_cat:bayram")
        ],
        [
            InlineKeyboardButton(text="⚡ Anime", callback_data="gif_cat:anime"),
            InlineKeyboardButton(text="🎲 Tasodifiy GIF", callback_data="gif_cat:random")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def get_gif_action_buttons(category: str) -> InlineKeyboardMarkup:
    """Yana GIF olish tugmasi"""
    keyboard = [
        [
            InlineKeyboardButton(text="🔄 Yana bitta GIF", callback_data=f"gif_cat:{category}"),
            InlineKeyboardButton(text="📂 Boshqa kategoriya", callback_data="gif_menu")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def get_emoji_menu() -> InlineKeyboardMarkup:
    """Emoji bo'limi tugmalari"""
    keyboard = [
        [
            InlineKeyboardButton(text="🎨 Emoji Art", callback_data="emoji_art"),
            InlineKeyboardButton(text="🧩 Emoji Kombinatsiyalar", callback_data="emoji_combo")
        ],
        [
            InlineKeyboardButton(text="😃 Quvonch", callback_data="emoji_cat:quvonch"),
            InlineKeyboardButton(text="❤️ Sevgi", callback_data="emoji_cat:sevgi")
        ],
        [
            InlineKeyboardButton(text="🐱 Hayvonlar", callback_data="emoji_cat:hayvonlar"),
            InlineKeyboardButton(text="🍕 Taomlar", callback_data="emoji_cat:taom")
        ],
        [
            InlineKeyboardButton(text="🎲 Tasodifiy Emoji", callback_data="emoji_cat:random")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def get_stickers_menu() -> InlineKeyboardMarkup:
    """Stiker bo'limi tugmalari"""
    keyboard = [
        [
            InlineKeyboardButton(text="📦 Mashhur stiker to'plamlari", callback_data="sticker_packs"),
        ],
        [
            InlineKeyboardButton(text="🔎 Stiker ID sini aniqlash", callback_data="sticker_id_info"),
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def get_random_menu() -> InlineKeyboardMarkup:
    """Tasodifiy bo'lim tugmalari"""
    keyboard = [
        [
            InlineKeyboardButton(text="🎬 Tasodifiy GIF", callback_data="rand_gif"),
            InlineKeyboardButton(text="😀 Tasodifiy Emoji", callback_data="rand_emoji")
        ],
        [
            InlineKeyboardButton(text="🎨 Tasodifiy Emoji Art", callback_data="rand_art"),
            InlineKeyboardButton(text="🧩 Tasodifiy Kombinatsiya", callback_data="rand_combo")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)
