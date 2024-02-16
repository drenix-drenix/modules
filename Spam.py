from .. import loader, utils
from asyncio import sleep, gather
import random

def register(cb):
    cb(SpamMod())

class SpamMod(loader.Module):
    """Модуль для выполнения различных видов спама."""
    strings = {'name': 'Spam'}

    async def spamcmd(self, message):
        """
        Обычный спам. Используй .spam <текст или реплай>.
        
        Этот метод отправляет сообщения или медиафайлы в чат или канал в большом количестве. 
        Количество сообщений генерируется случайным образом в диапазоне от 400 до 5000 при каждом запуске команды.
        """
        try:
            await message.delete()
            reply = await message.get_reply_message()
            count = random.randint(400, 5000)  # Генерируем случайное количество сообщений
            if reply:
                if reply.media:
                    for _ in range(count):
                        await message.client.send_file(message.to_id, reply.media)
                    return
                else:
                    for _ in range(count):
                        await message.client.send_message(message.to_id, reply)
            else:
                message_text = utils.get_args_raw(message)
                for _ in range(count):
                    await gather(*[message.respond(message_text)])
        except Exception as e:
            return await message.client.send_message(message.to_id, f'Произошла ошибка: {e}')

    async def cspamcmd(self, message):
        """
        Спам символами. Используй .cspam <текст или реплай>.
        
        Этот метод отправляет каждый символ из текста или ответного сообщения по отдельности в чат или канал.
        """
        await message.delete()
        reply = await message.get_reply_message()
        if reply:
            text = reply.raw_text
        else:
            text = utils.get_args_raw(message)
        text = text.replace(' ', '')  # Удаляем пробелы
        for char in text:
            await message.respond(char)

    async def wspamcmd(self, message):
        """
        Спам словами. Используй .wspam <текст или реплай>.
        
        Этот метод отправляет каждое слово из текста или ответного сообщения по отдельности в чат или канал.
        """
        await message.delete()
        reply = await message.get_reply_message()
        if reply:
            text = reply.raw_text
        else:
            text = utils.get_args_raw(message)
        words = text.split()  # Разбиваем текст на слова
        for word in words:
            await message.respond(word)

    async def delayspamcmd(self, message):
        """
        Спам с задержкой. Используй .delayspam <время:int> <текст или реплай>.
        
        Этот метод отправляет сообщения с задержкой между ними. 
        Первый аргумент - время задержки в секундах, второй аргумент - текст или ответное сообщение для отправки.
        """
        try:
            await message.delete()
            args = utils.get_args_raw(message)
            reply = await message.get_reply_message()
            time = int(args.split(' ', 1)[0])
            if reply:
                if reply.media:
                    async with message.client.action(message.chat_id, "record_video"):
                        for _ in range(5):
                            await message.client.send_file(message.to_id, reply.media, reply_to=reply.id)
                            await sleep(time)
                else:
                    for _ in range(5):
                        await reply.reply(args.split(' ', 1)[1])
                        await sleep(time)
            else:
                spam_text = args.split(' ', 1)[1]
                for _ in range(5):
                    await message.respond(spam_text)
                    await sleep(time)
        except Exception as e:
            return await message.client.send_message(message.to_id, f'Произошла ошибка: {e}')
