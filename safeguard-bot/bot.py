from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor
import random

API_TOKEN = 'Your_bot_token'
CHANNEL_ID = # Your channel ID -102941024910 (like this) 

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

# Словарь для хранения состояния пользователей и правильных ответов капчи
user_states = {}

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    # Генерация простой математической капчи
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    answer = num1 + num2
    user_states[message.from_user.id] = answer
    
    await message.reply(f"Привет! Чтобы получить доступ, решите капчу:\n{num1} + {num2} = ?")

@dp.message_handler(lambda message: message.from_user.id in user_states)
async def verify_captcha(message: types.Message):
    try:
        user_answer = int(message.text)
    except ValueError:
        await message.reply("Пожалуйста, введите число.")
        return
    
    correct_answer = user_states[message.from_user.id]
    if user_answer == correct_answer:
        del user_states[message.from_user.id]
        
        # Генерация ссылки-приглашения в канал
        try:
            invite_link = await bot.export_chat_invite_link(CHANNEL_ID)
            await message.reply(f"Вы успешно прошли проверку! Вот ваша ссылка для доступа в канал: {invite_link}")
        except Exception as e:
            await message.reply(f"Произошла ошибка при получении ссылки-приглашения: {e}")
    else:
        await message.reply("Неправильный ответ. Попробуйте еще раз.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
