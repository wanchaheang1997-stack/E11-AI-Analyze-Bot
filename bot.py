import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# កំណត់ Logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# ទាញយក Token ពី Environment Variable
TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    welcome_text = (
        f"Welcome to E11 Lab 🧪, {user_name}!\n\n"
        "Join our community for professional XAUUSD insights and AI trading tools.\n\n"
        "តោះ Subscribe ដើម្បីក្លាយជាផ្នែកមួយរបស់ពួកយើង!"
    )
    keyboard = [[InlineKeyboardButton("✅ I have subscribed", callback_data='is_subscribed')]]
    
    # ប្រើ Link រូបភាពឱ្យបានត្រឹមត្រូវ
    await update.message.reply_photo(
        photo="https://telegra.ph/file/0e48119097723919f20c1.jpg", 
        caption=welcome_text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode='Markdown'
    )

async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == 'is_subscribed':
        access_keyboard = [
            [InlineKeyboardButton("🏛️ Brokers that I use", callback_data='show_brokers')],
            [InlineKeyboardButton("📺 Video Lessons", url="https://youtube.com/@e11lab")],
            [InlineKeyboardButton("📚 Notion Library", url="https://e11lablibrary.blogspot.com")],
            [InlineKeyboardButton("🌐 Website", url="https://t.me/E11_Lab_Official")]
        ]
        await query.message.edit_caption(
            caption="Access Granted! ✅\n\nសូមជ្រើសរើសមុខងារខាងក្រោម៖",
            reply_markup=InlineKeyboardMarkup(access_keyboard)
        )
    elif query.data == 'show_brokers':
        broker_keyboard = [
            [InlineKeyboardButton("🟡 Exness", url="https://one.exnessonelink.com/a/c_2n7hv0b8qh")],
            [InlineKeyboardButton("🔵 GTCfx", url="https://web.mygtc.app/login/register?ref=130059052")],
            [InlineKeyboardButton("⬅️ Back", callback_data='is_subscribed')]
        ]
        await query.message.edit_caption(
            caption="🏛️ **Brokers that I use**",
            reply_markup=InlineKeyboardMarkup(broker_keyboard),
            parse_mode='Markdown'

        )

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_callback))
    app.run_polling()
