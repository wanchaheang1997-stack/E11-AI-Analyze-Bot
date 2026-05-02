import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
TOKEN = os.getenv("BOT_TOKEN")

# Links ផ្លូវការ
EXNESS_LINK = "https://one.exnessonelink.com/a/c_2n7hv0b8qh"
GTCFX_LINK = "https://web.mygtc.app/login/register?ref=130059052"
YOUTUBE_LINK = "https://youtube.com/@e11lab"
LIBRARY_LINK = "https://e11lablibrary.blogspot.com"
TELEGRAM_OFFICIAL = "https://t.me/E11_Lab_Official"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    welcome_text = (
        f"Welcome to E11 Lab 🧪, {user_name}!\n\n"
        "🌟 **E11 Lab Introduction & Benefits**\n"
        "Join our community to access professional XAUUSD insights, "
        "Algo trading educational content, and advanced AI trading tools designed "
        "to enhance your trading journey.\n\n"
        "តោះ Subscribe ដើម្បីក្លាយជាផ្នែកមួយរបស់ពួកយើង!\n"
        "Let's subscribe to become part of our community!"
    )
    keyboard = [[InlineKeyboardButton("✅ I have subscribed", callback_data='is_subscribed')]]
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
            [InlineKeyboardButton("📺 Video Lessons", url=YOUTUBE_LINK)],
            [InlineKeyboardButton("📚 Notion Library", url=LIBRARY_LINK)],
            [InlineKeyboardButton("🌐 Website", url=TELEGRAM_OFFICIAL)]
        ]
        await query.message.edit_caption(
            caption="Access Granted! ✅\n\nឥឡូវនេះបងអាចប្រើប្រាស់មុខងារទាំងអស់ខាងក្រោម៖",
            reply_markup=InlineKeyboardMarkup(access_keyboard)
        )
    elif query.data == 'show_brokers':
        broker_keyboard = [
            [InlineKeyboardButton("🟡 Exness", url=EXNESS_LINK)],
            [InlineKeyboardButton("🔵 GTCfx", url=GTCFX_LINK)],
            [InlineKeyboardButton("⬅️ Back", callback_data='is_subscribed')]
        ]
        await query.message.edit_caption(
            caption="🏛️ **Brokers that I use**\n\nសូមជ្រើសរើស Broker ខាងក្រោមដើម្បីចុះឈ្មោះ៖",
            reply_markup=InlineKeyboardMarkup(broker_keyboard),
            parse_mode='Markdown'
        )

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_callback))
    app.run_polling()

