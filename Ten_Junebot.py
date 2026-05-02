from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8716416403:AAHpuWpB9K-Hw24SQEdlrvkGmqrgV-7I1Zo"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я твой бот. Напиши что-нибудь!")

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Я умею отвечать на сообщения. Просто напиши мне!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text(f"Ты написал: {text}")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_cmd))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

print("Бот запущен...")
app.run_polling()