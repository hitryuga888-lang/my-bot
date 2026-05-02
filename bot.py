from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes

TOKEN = "8716416403:AAHpuWpB9K-Hw24SQEdlrvkGmqrgV-7I1Zo"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Привет!", callback_data="hello")],
        [InlineKeyboardButton("Помощь", callback_data="help"),
         InlineKeyboardButton("О боте", callback_data="about")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Выбери действие:", reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "hello":
        await query.edit_message_text("Привет! Рад тебя видеть!")
    elif query.data == "help":
        await query.edit_message_text("Я бот с кнопками. Напиши /start чтобы начать!")
    elif query.data == "about":
        await query.edit_message_text("Я крутой бот, сделан на Python!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text(f"Ты написал: {text}")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
print("Бот запущен...")
app.run_polling()
