from telegram import Update
from telegram.ext import ApplicationBuilder, ChatJoinRequestHandler, ContextTypes

# Замени на свой токен
TOKEN = '7760881876:AAECbRdhRi5_i3S_dedNavfb9gSN13KVOJg'

# Функция для автоматического одобрения заявок
async def approve_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.chat_join_request.chat.id
    user_id = update.chat_join_request.from_user.id

    # Одобряем заявку пользователя
    await context.bot.approve_chat_join_request(chat_id=chat_id, user_id=user_id)
    print(f"Одобрена заявка от пользователя {user_id}")

async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # Добавляем обработчик join requests
    app.add_handler(ChatJoinRequestHandler(approve_request))

    print("Бот запущен и работает!")
    await app.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
