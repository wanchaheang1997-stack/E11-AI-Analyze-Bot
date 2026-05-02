import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # ពេលបងចុច /start វានឹងឆ្លើយតបអក្សរខាងក្រោមនេះភ្លាម
    await update.message.reply_text("បាទបង! Bot ដើរហើយ! នេះគឺជាកូដតេស្តកម្រិតមូលដ្ឋានបំផុត។")

if __name__ == '__main__':
    # ប្រើ Token ផ្ទាល់តែម្តងដើម្បីកុំឱ្យច្រឡំជាមួយ Environment Variable
    TOKEN = "8536745408:AAHpyjnUbFiYCp_JNf8cw4bQJp-0Z1eeciQ"
    
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    
    print("Bot is starting...")
    app.run_polling()
    
