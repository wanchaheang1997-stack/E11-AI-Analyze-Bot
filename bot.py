import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, BotCommand
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

CHANNEL_LINK = "https://t.me/E11_Lab_Official"
COMMUNITY_LINK = "https://t.me/E11LabCommunity"
NOTION_LIBRARY = "https://showy-food-c40.notion.site/E11-LAB-LIBRARY-46733417906d45ab83e464fb98401410"
YOUTUBE_CHANNEL = "https://youtube.com/@e11lab_official"
EXNESS_LINK = "https://one.exnessonelink.com/a/c_2n7hv0b8qh"
GTCFX_LINK = "https://web.mygtc.app/login/register?ref=130059052"

async def post_init(application: Application):
    await application.bot.set_my_commands([
        BotCommand("start", "🧪 ចាប់ផ្ដើម E11 Lab Guide"),
        BotCommand("help", "🆘 ជំនួយ")
    ])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    welcome_text = (
        f"Welcome to **E11 Lab 🧪**, {user.first_name}!\n\n"
        "ដើម្បីប្រើប្រាស់ Tools និងចូលទៅកាន់ Library សូមចុច Subscribe ឆានែលយើងខ្ញុំសិន៖\n\n"
        f"📢 [E11 Lab Official]({CHANNEL_LINK})\n"
        f"👥 [E11 Community]({COMMUNITY_LINK})\n\n"
        "**តើបងបាន Subscribe រួចរាល់ហើយឬនៅ?**"
    )
    keyboard = [
        [InlineKeyboardButton("✅ បាទ រួចរាល់ហើយ", callback_data='is_subscribed')],
        [InlineKeyboardButton("❌ នៅមិនទាន់បាន Join ទេ", callback_data='not_subscribed')]
    ]
    if update.message:
        await update.message.reply_text(welcome_text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')
    else:
        await update.callback_query.edit_message_text(welcome_text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')

async def handle_subscription(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == 'is_subscribed':
        text = "**Access Granted! ✅**\n\nឥឡូវនេះបងអាចប្រើប្រាស់មុខងារទាំងអស់ខាងក្រោម៖"
        keyboard = [
            [InlineKeyboardButton("🏛️ ចុះឈ្មោះ Broker", callback_data='broker_menu')],
            [InlineKeyboardButton("📺 របៀបប្ដូរ Partner (YouTube)", url=YOUTUBE_CHANNEL)],
            [InlineKeyboardButton("📚 ឯកសារមេរៀន (Notion)", url=NOTION_LIBRARY)],
            [InlineKeyboardButton("🌐 Website", url="https://e11lab.com")]
        ]
        await query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')
    elif query.data == 'not_subscribed':
        await query.edit_message_text("សូមចុច Join Channel ខាងលើសិន រួចត្រឡប់មកវិញ។", 
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ ត្រឡប់ក្រោយ", callback_data='back_to_start')]]))

async def broker_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = f"**🏛️ ចុះឈ្មោះជាមួយដៃគូ Broker**\n\n🟡 [Exness]({EXNESS_LINK})\n🔵 [GTCfx]({GTCFX_LINK})"
    await query.edit_message_text(text, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Menu", callback_data='is_subscribed')]]), parse_mode='Markdown')

if __name__ == '__main__':
    TOKEN = os.getenv("BOT_TOKEN")
    application = Application.builder().token(TOKEN).post_init(post_init).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(start, pattern='^back_to_start$'))
    application.add_handler(CallbackQueryHandler(handle_subscription, pattern='^(is_subscribed|not_subscribed)$'))
    application.add_handler(CallbackQueryHandler(broker_menu, pattern='^broker_menu$'))
    application.run_polling()
