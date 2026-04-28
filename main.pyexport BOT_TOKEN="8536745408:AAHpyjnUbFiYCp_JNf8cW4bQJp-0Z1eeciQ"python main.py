import os
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler

# --- សារស្វាគមន៍ (គ្មានលេខ 1. 2. 3.) ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text1 = (
        "Hello, we are **E11 Lab**. If you've clicked on my bot, then you want to start trading easy, right? 👋\n\n"
        "I've been trading for over 4 years now. We've built this community for everyone to learn and grow together. "
        "I will explain everything step by step. ✅"
    )
    await update.message.reply_text(text1, parse_mode='Markdown')
    
    await asyncio.sleep(2)
    text2 = (
        "Be sure to subscribe to my channel, there is a lot of information, education, news, "
        "and exclusive benefits like **Bot Alerts, Reports, TV Tools, EA, and Copy Trading**! 😊👇"
    )
    keyboard2 = [[InlineKeyboardButton("🟢 SUBSCRIBE CHANNEL 🟢", url="https://t.me/E11_Lab_Official")]]
    await update.message.reply_text(text2, reply_markup=InlineKeyboardMarkup(keyboard2))

    await asyncio.sleep(3)
    await update.message.reply_text("By the way, what is your name and do you have any experience in trading?")

# --- វគ្គឆ្លើយតបសំណួរ ---
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message.text.startswith('/'):
        text = (
            "Okay, let me tell you more. 💡\n\n"
            "យើងបង្កើត E11 Lab ឡើងដើម្បីផ្តល់ភាពងាយស្រូវដល់អ្នកដែលចង់ត្រេដ តែមិនទាន់ចេះ ឬមិនសូវជោគជ័យ។ "
            "You can see our results and back-testing in our channel.\n\n"
            "**តើមេរួចរាល់ដើម្បីរីកចម្រើនជាមួយគ្នាហើយឬនៅ?**"
        )
        keyboard = [[InlineKeyboardButton("✅ Ready! Let's Start", callback_data='ready')]]
        await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')

# --- វគ្គ Register (ដូច Amir Trader) ---
async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'ready':
        text = (
            "🚀 **Let's Start!**\n\n"
            "The first step is to register a trading account. The account must be created using these links!\n\n"
            "🔗 **Exness:** [Register Here](https://one.exnessonelink.com/a/c_2n7hv0b8qh)\n"
            "🔗 **GTCFX:** [Register Here](https://web.mygtc.app/login/register?ref=130059052)\n\n"
            "⚠️ **Attention:** Account must be new! If you already have an account, please register with a new email.\n\n"
            "After registration, write to me and I will tell you what to do next. ✨"
        )
        keyboard = [[InlineKeyboardButton("✅ I have registered!", callback_data='done_reg')]]
        await query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown', disable_web_page_preview=True)

if __name__ == "__main__":
    TOKEN = os.getenv("BOT_TOKEN")
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    app.add_handler(CallbackQueryHandler(button_callback))
    print("🚀 E11 Pro Flow (Clean) is starting...")
    app.run_polling(drop_pending_updates=True)

