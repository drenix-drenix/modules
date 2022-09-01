import io

import requests
from telethon.tl.types import Message

from .. import loader, utils


@loader.tds
class Web2fileMod(loader.Module):
    """Скачивает содержимое ссылки и отправляет в виде файла"""

    strings = {
        "name": "Web2file",
        "no_args": "🚫 <b>Specify link</b>",
        "fetch_error": "🚫 <b>Download error</b>",
        "loading": "👀 <b>Downloading...</b>",
    }

    strings_ru = {
        "no_args": "🚫 <b>Укажи ссылку</b>",
        "fetch_error": "🚫 <b>Ошибка загрузки</b>",
        "loading": "👀 <b>Загрузка...</b>",
        "_cls_doc": "Скачивает содержимое ссылки и отправляет в виде файла",
    }

    async def web2filecmd(self, message: Message):
        """отправка содержимого ссылки в виде файла"""
        website = utils.get_args_raw(message)
        if not website:
            await utils.answer(message, self.strings("no_args", message))
            return
        try:
            f = io.BytesIO(requests.get(website).content)
        except Exception:
            await utils.answer(message, self.strings("fetch_error", message))
            return

        f.name = website.split("/")[-1]

        await message.respond(file=f)
        await message.delete()
