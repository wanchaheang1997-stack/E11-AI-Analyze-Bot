import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# កំណត់ Logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# ដាក់ Token ផ្ទាល់ដើម្បីកុំឱ្យខុស (បងអាចដូរលេខ Token ថ្មីពី BotFather មកដាក់ត្រង់នេះ)
TOKEN = "8536745408:AAHpyjnUbFiYCp_JNf8cw4bQJp-0Z1eeciQ"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    welcome_text = f"Welcome {user_name} to E11 Lab! 🧪\n\nនេះគឺជា Bot តេស្តថ្មីស្រឡាង។"
    keyboard = [[InlineKeyboardButton("✅ I have subscribed", callback_data='sub')]]
    
    await update.message.reply_text(text=welcome_text, reply_markup=InlineKeyboardMarkup(keyboard))

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == 'sub':
        await query.edit_message_text(text="អរគុណបង! Bot ដំណើរការជោគជ័យហើយ! 🎉")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    print("Bot is starting...")
    app.run_polling()

