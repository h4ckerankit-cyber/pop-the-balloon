from telegram import Update, BotCommand
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext

BOT_TOKEN = '7637662757:AAHXh695oXJ3N2Xm_rC5mmYQ6MKpmFpNgz0'

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text(
        'Play the Balloon Pop Game!',
        reply_markup={'inline_keyboard': [[{'text': 'Play Now!', 'url': 'https://pop-the-balloon-git-main-h4ckerankit-cybers-projects.vercel.app/'}]]}
    )

if __name__ == '__main__':
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    application.run_polling()
