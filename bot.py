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

# --- ផ្នែកកូដ Bot ផ្ដល់ព័ត៌មាន ---
TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📊 តារាងតម្លៃមាស", callback_data='gold')],
        [InlineKeyboardButton("📢 ចូលរួម Channel", url="https://t.me/E11Lab_Official")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("សួស្តីបង! ស្វាគមន៍មកកាន់ E11 Lab Assistant។ សូមជ្រើសរើស៖", reply_markup=reply_markup)

async def handle_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == 'gold':
        await query.edit_message_text("📈 តម្លៃមាសថ្ងៃនេះ៖ [កំពុង Update] \nចុច /start ដើម្បីទៅមេនុយវិញ។")

if __name__ == '__main__':
    # បើក Flask ក្នុង Thread ផ្សេង
    threading.Thread(target=run_web).start()
    
    # បញ្ឆេះ Bot
    if TOKEN:
        app = ApplicationBuilder().token(TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        app.add_handler(CallbackQueryHandler(handle_button))
        app.run_polling()
        
