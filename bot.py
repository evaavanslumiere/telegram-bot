from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "7924054088:AAH0DpoP5QrAz_14enDYNzVEFHQ9yTs2zCc"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Урок 1", callback_data='lesson1')],
        [InlineKeyboardButton("Урок 2", callback_data='lesson2')],
        [InlineKeyboardButton("Урок 3", callback_data='lesson3')],
        [InlineKeyboardButton("Урок 4", callback_data='lesson4')],
        [InlineKeyboardButton("Урок 5", callback_data='lesson5')],
        [InlineKeyboardButton("Книги и пособия", callback_data='books')],
        [InlineKeyboardButton("Связь с куратором", url='https://t.me/LurdesPolina')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Выберите раздел:", reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'lesson1':
        await query.edit_message_text("🎧 Урок 1: [аудио, видео, текст, фото]")
    elif query.data == 'lesson2':
        await query.edit_message_text("🎥 Урок 2: [здесь будет контент]")
    elif query.data == 'books':
        await query.edit_message_text("📚 Книги и пособия: [ссылки или файлы]")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.run_polling()

if __name__ == '__main__':
    main()
