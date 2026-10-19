#!/data/data/com.termux/files/usr/bin/bash
# Ek baar chalao: bash setup_termux.sh
set -e
pkg update -y
pkg install -y python ffmpeg aria2 clang libffi openssl
pip install -r requirements.txt
mkdir -p songs
echo
echo "✅ Setup ho gaya."
echo "1) app/config.py mein ADMIN = apni Telegram ID"
echo "2) .env mein TOKEN check karo"
echo "3) Chalao: bash run.sh"
