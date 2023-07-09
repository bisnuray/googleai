import logging
import pprint
import google.generativeai as palm
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ParseMode

# Insert your API keys
API_KEY = "***************"  # PaLM API key
TG_BOT_TOKEN = "**************"  # Telegram bot token

palm.configure(api_key=API_KEY)

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TG_BOT_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    await message.reply("Welcome! Send /bard followed by your prompt to generate text.")

@dp.message_handler(lambda message: message.text.startswith('/bard'))
async def generate_text(message: types.Message):
    prompt = message.text[5:].strip()

    if not prompt:
        await message.reply("<b>Please provide a text prompt after the /bard command.</b>", parse_mode=ParseMode.HTML)
        return

    loading_message = await message.reply("<b>Generating output, please wait...</b>", parse_mode=ParseMode.HTML)

    model = "models/text-bison-001"
    try:
        completion = palm.generate_text(model=model, prompt=prompt, temperature=0, max_output_tokens=800)
        output_message = f'<b>Prompt:</b> {prompt}\n\n{completion.result}'
        await bot.send_message(chat_id=message.chat.id, text=output_message, parse_mode=ParseMode.HTML)
    except Exception as e:
        output_message = f'<b>❌ An error occurred while generating the text:\n\n{str(e)}</b>'
        await bot.send_message(chat_id=message.chat.id, text=output_message, parse_mode=ParseMode.HTML)

    await bot.delete_message(chat_id=message.chat.id, message_id=loading_message.message_id)

if __name__ == "__main__":
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
