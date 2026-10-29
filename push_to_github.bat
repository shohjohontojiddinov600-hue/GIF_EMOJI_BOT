@echo off
chcp 65001 >nul
setlocal
echo ==============================================================
echo Loyihani GitHub-ga yuklash (Push qilish)...
echo Repozitoriy: https://github.com/shohjohontojiddinov600-hue/GIF_EMOJI_BOT.git
echo ==============================================================

set "GIT_PATH=%LOCALAPPDATA%\Programs\Git\cmd\git.exe"
if exist "%GIT_PATH%" (
    set "GIT_CMD=%GIT_PATH%"
) else (
    set "GIT_CMD=git"
)

"%GIT_CMD%" config --get user.name >nul 2>&1
if errorlevel 1 (
    "%GIT_CMD%" config --global user.name "shohjohontojiddinov600-hue"
    "%GIT_CMD%" config --global user.email "shohjohontojiddinov600@gmail.com"
)

echo.
echo 1. O'zgarishlar Git-ga saqlanmoqda...
"%GIT_CMD%" add .
"%GIT_CMD%" commit -m "Yangilanishlar va xatoliklar tuzatildi: GIF havolalari, animatsiya navigatsiyasi va menyular" 2>nul

echo.
echo 2. GitHub-ga push qilinmoqda...
echo (Agar brauzerda darcha ochilsa, GitHub akkauntingizga kirishni tasdiqlang)
"%GIT_CMD%" push -u origin main

echo.
echo ==============================================================
if errorlevel 1 (
    echo [XATOLIK] GitHub-ga yuklashda xatolik yuz berdi.
    echo Agar Personal Access Token (PAT) yoki parol so'ralsa, uni kiriting.
) else (
    echo [MUVAFFAQIYATLI] Barcha kodlar GitHub-ga muvaffaqiyatli yuklandi!
)
echo ==============================================================
echo.
pause
