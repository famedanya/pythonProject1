import asyncio
from aiogram import Bot, Dispatcher, F

from aiogram.filters import Command, Text
from aiogram.types import Message, ContentType, Sticker, voice, video

from config import config

API_TOKEN = config.token

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(Command(commands=['start']))
async def start_command(message: Message):
    await message.answer('Привет!')


@dp.message(Command(commands=['help']))
async def help_command(message: Message):
    await message.answer('Чем я могу помочь?')


@dp.message(Text(text=['1234']))
async def lucky_command(message: Message):
    await message.answer('Вы открыли пасхалку!')


#
#
# @dp.message(F.content_type == ContentType.PHOTO)
# async def echo_photo(message: Message):
#     await message.answer_photo(message.photo[0].file_id)
#
#
# @dp.message(F.content_type == ContentType.STICKER)
# async def echo_sticker(message: Message):
#     await message.answer_sticker(message.sticker.file_id)
#
#
# @dp.message(F.content_type == ContentType.VOICE)
# async def echo_voice(message: Message):
#     await message.answer_voice(message.voice.file_id)
#
#
# @dp.message(F.content_type == ContentType.VIDEO)
# async def echo_video(message: Message):
#     await message.answer_video(message.video.file_id)
#
#
# @dp.message()
# async def echo(message: Message):
#     await message.answer(message.text)


@dp.message(Text(text='Ответь'))
async def reply(message: Message):
    await message.reply('Ответил')


@dp.message()
async def echo_all(message: Message):
    await message.send_copy(message.chat.id)


async def main():
    try:
        print('Bot Started')
        await dp.start_polling(bot)

    finally:
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped')
