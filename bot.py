import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# កំណត់ Logging
logging.basicConfig(level=logging.INFO)
TOKEN = os.getenv("BOT_TOKEN")

# ១. នៅពេលគេចូលដល់ Bot ភ្លាម (ចុច /start)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    
    # រូបភាព Description (បងអាចប្តូរ Link រូបភាពរបស់បងនៅទីនេះ)
    photo_url = "https://e11lablibrary.blogspot.com/favicon.ico" # ឧទាហរណ៍៖ រូប Logo E11 Lab
    
    description_text = (
        f"សួស្តីបង {user_name}! ស្វាគមន៍មកកាន់ **E11 Lab Bot**។\n\n"
        "ទីនេះគឺជាមជ្ឈមណ្ឌលចែករំលែកចំណេះដឹងផ្នែក Trading និងបច្ចេកវិទ្យាថ្មីៗ។"
    )

    # ប៊ូតុងដើម្បីទៅជំហានទី ២
    keyboard = [[InlineKeyboardButton("🚀 ចាប់ផ្ដើមឥឡូវនេះ", callback_data='go_to_step2')]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_photo(
        photo=photo_url,
        caption=description_text,
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

# ២. ជំហានទី ២៖ ណែនាំឱ្យ Join Channel & Group
async def step2_onboarding(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    text = (
        "ដើម្បីបន្តប្រើប្រាស់ Bot នេះបាន សូមបងជួយ Join និង Subscribe ខាងក្រោមសិន៖\n\n"
        "1️⃣ **Join Group:** [E11 Lab Community](https://t.me/E11LabCommunity)\n"
        "2️⃣ **Subscribe Channel:** [E11 Lab Official](https://t.me/E11_Lab_Official)"
    )

    keyboard = [
        [
            InlineKeyboardButton("📢 Join Channel", url="https://t.me/E11_Lab_Official"),
            InlineKeyboardButton("👥 Join Group", url="https://t.me/E11LabCommunity")
        ],
        [InlineKeyboardButton("✅ ខ្ញុំបាន Join រួចរាល់ហើយ", callback_data='go_to_step3')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_caption(
        caption=text,
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

# ៣. ជំហានទី ៣៖ បង្ហាញ Option ទាំង ៤ (បងប្រាប់មកតែ ៣ ខ្ញុំថែមប៊ូតុងជំនួយការ ១ ទៀតឱ្យគ្រប់ ៤)
async def step3_options(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    text = "សូមជ្រើសរើសព័ត៌មានដែលបងចង់មើលខាងក្រោម៖"

    keyboard = [
        [InlineKeyboardButton("🌐 ទី១. E11 Lab Library", url="https://e11lablibrary.blogspot.com")],
        [InlineKeyboardButton("📺 ទី២. Lesson & Video", url="https://youtube.com/@e11lab_official")],
        [InlineKeyboardButton("🔵 ទី៣. Facebook Page", url="https://www.facebook.com/share/1B7fxHXxZ4/")],
        [InlineKeyboardButton("📞 ទី៤. ជំនួយការ (Support)", url="https://t.me/wanchaheang")] # ខ្ញុំថែមជូន
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_caption(
        caption=text,
        reply_markup=reply_markup
    )

if __name__ == '__main__':
    if not TOKEN:
        print("Error: BOT_TOKEN missing in Environment Variables!")
    else:
        app = ApplicationBuilder().token(TOKEN).build()
        
        app.add_handler(CommandHandler("start", start))
        app.add_handler(CallbackQueryHandler(step2_onboarding, pattern='^go_to_step2$'))
        app.add_handler(CallbackQueryHandler(step3_options, pattern='^go_to_step3$'))
        
        print("E11 Lab Bot is running...")
        app.run_polling()
