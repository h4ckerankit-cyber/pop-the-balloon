from telegram import Update, BotCommand
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext

BOT_TOKEN = 'YOUR_BOT_TOKEN'

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text(
        'Play the Balloon Pop Game!',
        reply_markup={'inline_keyboard': [[{'text': 'Play Now!', 'url': 'https://yourdomain.com/balloon-game'}]]}
    )

if __name__ == '__main__':
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    application.run_polling()
