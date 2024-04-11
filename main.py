from aiogram import Bot, Dispatcher, types
import asyncio
import GigaLogic
import Kandivsky

telegram_token = ""


bot = Bot(token=telegram_token)
dp = Dispatcher(bot=bot)


@dp.message(lambda message: "start" in message.text)
async def cmd_start(msg: types.Message) -> None:
    answer=GigaLogic.sent_message("Привет, кто ты?")
    await msg.answer(answer+" Также вы можете попросить меня нарисовать что-то. Просто напишите слово 'Нарисуй', а после дайте описание рисунка. Пример: Нарисуй мне фотореалистичную машину.")


@dp.message(lambda message: "Нарисуй" in message.text)
async def cmd_start(msg: types.Message) -> None:
    answer=Kandivsky.prints(msg.text)
    if answer:
        await bot.send_photo(chat_id=msg.chat.id, photo=types.FSInputFile("image.jpg"))
    else:
        "Error"

@dp.message()
async def cmd_start(msg: types.Message) -> None:
    answer=GigaLogic.sent_message(msg.text)
    await msg.answer(answer)


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
