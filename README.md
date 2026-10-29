# 🎬 GIF, Emoji va Stikerlar Telegram Boti

Ushbu loyiha Telegram foydalanuvchilari uchun mo'ljallangan zamonaviy, tezkor va ko'p funksiyali bot hisoblanadi. Bot orqali turli kategoriyadagi GIFlarni topish, chiroyli Emojilar va Emoji Art san'at namunalaridan foydalanish hamda stiker to'plamlarini ko'rish va stikerlar haqida to'liq texnik ma'lumot (File ID, Set name) olish mumkin.

## 🚀 Asosiy Imkoniyatlar

- 🎬 **GIFlar bo'limi:**
  - Kategoriya bo'yicha GIFlar: *Kulgi, Sevgi, Reaksiyalar, Hayvonlar, Salomlashish, Bayram, Anime, Tasodifiy*
  - "Yana bitta GIF" tugmasi orqali tezkor almashtirish
- 😀 **Emojilar bo'limi:**
  - Kategoriya bo'yicha saralangan emojilar
  - **Emoji Art** (ramzli chiroyli matnli rasmlar)
  - **Emoji Kombinatsiyalari** (ma'noli emojilar to'plami va ularning ma'nosi)
- 🎭 **Stikerlar bo'limi:**
  - Eng mashhur va chiroyli stiker to'plamlari katalogi
  - **Stiker identifikatori:** Botga istalgan stiker yuborilganda uning `File ID`si, emojisi, formati (Oddiy / Video / Animatsiya) va to'plamiga to'g'ridan-to'g'ri havolani chiqarib beradi.
- 🎲 **Tasodifiy bo'lim:**
  - Tasodifiy GIF, tasodifiy emoji, art yoki kombinatsiya
- 🔍 **Inline Rejim:**
  - Istalgan chatda `@bot_nomi so'z` yozib, to'g'ridan-to'g'ri GIF va emojilarni yuborish imkoniyati!

---

## 🛠 Texnologiyalar

- **Python 3.10+**
- **Aiogram 3.15+** (Asinxron Telegram Bot freymvorki)
- **Aiohttp** (Asinxron HTTP so'rovlar)
- **Python-dotenv** (Maxfiy kalitlar va muhit o'zgaruvchilari uchun)

---

## 📦 O'rnatish va Ishga Tushirish

### 1. Loyihani klonlash yoki yuklab olish:
```bash
git clone https://github.com/shohjohontojiddinov600-hue/GIF_EMOJI_BOT.git
cd GIF_EMOJI_BOT
```

### 2. Virtual muhit yaratish va kutubxonalarni o'rnatish:
```bash
# Windows uchun
python -m venv venv
.\venv\Scripts\activate

# Kutubxonalarni o'rnatish
pip install -r requirements.txt
```

### 3. `.env` faylini sozlash:
Loyiha papkasidagi `.env` faylida bot tokeningizni ko'rsating:
```env
BOT_TOKEN=9029434351:AAFpzYKaxMVihX_vpMbTJtZePvnv619XYYw
```

### 4. Botni ishga tushirish:
```bash
python bot.py
```

---

## 📁 Loyiha Strukturasi

```
GIF_BOT/
├── data/                  # GIF, Emoji va Stiker ma'lumotlar bazasi
│   ├── emojis.py
│   ├── gifs.py
│   └── stickers.py
├── handlers/              # Bot handlerlari
│   ├── start.py
│   ├── gifs.py
│   ├── emojis.py
│   ├── stickers.py
│   ├── random_content.py
│   └── inline.py
├── keyboards/             # Reply va Inline tugmalar
│   └── menu.py
├── bot.py                 # Asosiy kirish nuqtasi
├── config.py              # Konfiguratsiya fayli
├── .env                   # Maxfiy tokenlar
├── .env.example           # Namuna muhit fayli
├── .gitignore             # Git chetlab o'tishi kerak bo'lgan fayllar
├── requirements.txt       # Bog'liqliklar ro'yxati
└── README.md              # Loyiha qo'llanmasi
```

---

## 👤 Muallif
**Shohjohon Tojiddinov**  
GitHub: [@shohjohontojiddinov600-hue](https://github.com/shohjohontojiddinov600-hue)
