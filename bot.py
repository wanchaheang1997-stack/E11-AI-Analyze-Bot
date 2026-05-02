import os
import threading
from flask import Flask
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# --- ផ្នែកការពារ Render (Flask) ---
app_web = Flask('')
@app_web.route('/')
def home(): return "Bot is running!"
def run_web(): app_web.run(host='0.0.0.0', port=8080)

# --- ផ្នែកកូដ Bot ---
TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    
    # បង្កើតប៊ូតុងដែលភ្ជាប់ទៅកាន់ Group និង Channel របស់បងពិតប្រាកដ
    keyboard = [
        [
            InlineKeyboardButton("📢 ចូលរួម Channel", url="https://t.me/E11_Lab_Official")
        ],
        [
            InlineKeyboardButton("👥 ចូលរួម Group Community", url="https://t.me/E11LabCommunity")
        ],
        [
            InlineKeyboardButton("📞 ទាក់ទង Admin", url="https://t.me/wanchaheang")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    welcome_text = (
        f"សួស្តីបង {user_name}! 🙏 ស្វាគមន៍មកកាន់ E11 Lab Assistant។\n"
        "សូមជ្រើសរើសព័ត៌មានដែលបងចង់បានខាងក្រោម៖"
    )
    
    await update.message.reply_text(text=welcome_text, reply_markup=reply_markup)

if __name__ == '__main__':
    # បើក Flask ដើម្បីការពារ Render បិទ Bot
    threading.Thread(target=run_web).start()
    
    if not TOKEN:
        print("Error: BOT_TOKEN is missing in Environment Variables!")
    else:
        app = ApplicationBuilder().token(TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        
        print("Bot is starting with your Group & Channel links...")
        app.run_polling()
        
