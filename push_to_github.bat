@echo off
setlocal
echo ==============================================
echo Loyihani GitHub-ga yuklash (Push qilish)...
echo ==============================================

set "GIT_PATH=%LOCALAPPDATA%\Programs\Git\cmd\git.exe"
if exist "%GIT_PATH%" (
    set "GIT_CMD=%GIT_PATH%"
) else (
    set "GIT_CMD=git"
)

"%GIT_CMD%" config --get user.name >nul 2>&1
if errorlevel 1 (
    "%GIT_CMD%" config --global user.name "Shohjohon Tojiddinov"
    "%GIT_CMD%" config --global user.email "shohjohon@users.noreply.github.com"
)

"%GIT_CMD%" init
"%GIT_CMD%" branch -M main
"%GIT_CMD%" remote remove origin 2>nul
"%GIT_CMD%" remote add origin https://github.com/shohjohontojiddinov600-hue/GIF_EMOJI_BOT.git
"%GIT_CMD%" add .
"%GIT_CMD%" commit -m "Initial commit: Telegram GIF, Emoji va Stikerlar boti yaratildi"
"%GIT_CMD%" push -u origin main

echo.
echo Amal bajarildi!
pause
