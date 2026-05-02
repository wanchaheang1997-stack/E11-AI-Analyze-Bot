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
    
    # ប៊ូតុងមេ (Main Menu)
    keyboard = [
        [InlineKeyboardButton("📢 ចូលរួម Channel", url="https://t.me/E11_Lab_Official")],
        [InlineKeyboardButton("👥 ចូលរួម Group Community", url="https://t.me/E11LabCommunity")],
        [InlineKeyboardButton("📋 ព័ត៌មាន និង សេវាកម្ម (ចុចទីនេះ)", callback_data='show_services')],
        [InlineKeyboardButton("📞 ទាក់ទង Admin", url="https://t.me/wanchaheang")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        f"សួស្តីបង {user_name}! 🙏 ស្វាគមន៍មកកាន់ E11 Lab Assistant។\n"
        "សូមជ្រើសរើសព័ត៌មានដែលបងចង់បានខាងក្រោម៖", 
        reply_markup=reply_markup
    )

async def handle_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'show_services':
        # បង្កើតប៊ូតុងជម្រើសទាំង ៤ ដែលបងចង់បាន
        service_keyboard = [
            [InlineKeyboardButton("📈 Broker ខ្ញុំប្រើ (Exness & GTC)", callback_data='show_brokers')],
            [InlineKeyboardButton("🌐 E11 Lab Library (Blog)", url="https://e11lablibrary.blogspot.com")],
            [InlineKeyboardButton("📺 វីដេអូមេរៀន (YouTube)", url="https://youtube.com/@e11lab_official")],
            [InlineKeyboardButton("🔵 Facebook Page", url="https://www.facebook.com/share/1B7fxHXxZ4/")],
            [InlineKeyboardButton("⬅️ ត្រឡប់ក្រោយ", callback_data='back_to_start')]
        ]
        await query.edit_message_text(
            text="សូមជ្រើសរើសសេវាកម្មដែលបងចាប់អារម្មណ៍៖",
            reply_markup=InlineKeyboardMarkup(service_keyboard)
        )

    elif query.data == 'show_brokers':
        # បង្កើតប៊ូតុងសម្រាប់ Broker ទាំង ២
        broker_keyboard = [
            [InlineKeyboardButton("1. Exness Broker", url="https://one.exnessonelink.com/a/c_2n7hv0b8qh")],
            [InlineKeyboardButton("2. GTCFX Broker", url="https://web.mygtc.app/login/register?ref=130059052")],
            [InlineKeyboardButton("⬅️ ត្រឡប់ក្រោយ", callback_data='show_services')]
        ]
        await query.edit_message_text(
            text="នេះគឺជា Broker ដែលខ្ញុំប្រើប្រាស់៖",
            reply_markup=InlineKeyboardMarkup(broker_keyboard)
        )

    elif query.data == 'back_to_start':
        # ប៊ូតុងត្រឡប់ទៅ Main Menu វិញ
        main_keyboard = [
            [InlineKeyboardButton("📢 ចូលរួម Channel", url="https://t.me/E11_Lab_Official")],
            [InlineKeyboardButton("👥 ចូលរួម Group Community", url="https://t.me/E11LabCommunity")],
            [InlineKeyboardButton("📋 ព័ត៌មាន និង សេវាកម្ម", callback_data='show_services')],
            [InlineKeyboardButton("📞 ទាក់ទង Admin", url="https://t.me/wanchaheang")]
        ]
        await query.edit_message_text(
            text="សូមជ្រើសរើសព័ត៌មានដែលបងចង់បានខាងក្រោម៖",
            reply_markup=InlineKeyboardMarkup(main_keyboard)
        )

if __name__ == '__main__':
    threading.Thread(target=run_web).start()
    
    if TOKEN:
        app = ApplicationBuilder().token(TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        app.add_handler(CallbackQueryHandler(handle_button))
        
        print("Bot is updating with your 4 services...")
        app.run_polling()
        
