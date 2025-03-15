from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Hello! This is TaskFi Bot. Let's get started!")

app = ApplicationBuilder().token("8065803577:AAE66ynPhgsJHvzwUCJwyU-Ct2-QnZpqw2s").build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
