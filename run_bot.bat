@echo off
chcp 65001 >nul
echo ==============================================
echo GIF, Emoji va Stikerlar Botini ishga tushirish
echo ==============================================

python -m pip install -r requirements.txt
python bot.py

pause
