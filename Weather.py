import requests
from aiogram.types import (
    InlineKeyboardMarkup,
    InlineQueryResultArticle,
    InlineKeyboardButton,
    InputTextMessageContent,
)
from urllib.parse import quote_plus
from telethon.tl.types import Message
from telethon.tl.functions.channels import JoinChannelRequest
from ..inline import GeekInlineQuery, rand  # noqa
from .. import loader  # noqa
from .. import utils  # noqa
import logging
import re

logger = logging.getLogger(__name__)

n = '\n'
rus = "ёйцукенгшщзхъфывапролджэячсмитьбю"

def escape_ansi(line):
    ansi_escape = re.compile(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]')
    return ansi_escape.sub('', line)


class WeatherMod(loader.Module):
    """Модуль "Погода" """
    id = 17
    strings = {
        "name": "Weather"
    }

    async def weathercitycmd(self, message: Message) -> None:
        """Установить город по умолчанию для прогноза погоды"""
        if args := utils.get_args_raw(message):
            self.db.set(self.strings['name'], 'city', args)
        await utils.answer(message, f"<b>🏙 Ваш текущий город: "
                                    f"<code>{self.db.get(self.strings['name'], 'city', '🚫 Не указан')}</code></b>")
        return

    async def weathercmd(self, message: Message) -> None:
        """Текущий прогноз погоды по выбранному городу """
        city = utils.get_args_raw(message)
        if not city:
            city = self.db.get(self.strings['name'], 'city', "")
        lang = 'ru' if city and city[0].lower() in rus else 'en'
        req = requests.get(f"https://wttr.in/{city}?m&T&lang={lang}")
        await utils.answer(message, f'<code>{n.join(req.text.splitlines()[:7])}</code>')

    async def weather_inline_handler(self, query: GeekInlineQuery) -> None:
        """Поиск города"""
        args = query.args
        if not args:
            args = self.db.get(self.strings['name'], 'city', "")
        if not args:
            return
        # req = requests.get(f"https://wttr.in/{quote_plus(args)}?format=j1").json()
        lang = 'ru' if args and args[0].lower() in rus else 'en'
        req = requests.get(f"https://wttr.in/{quote_plus(args)}?format=3")
        await query.answer(
            [
                InlineQueryResultArticle(
                    id=rand(20),
                    title=f"Forecast for {args}",
                    description=req.text,
                    # thumb_url="https://i.ytimg.com/vi/IMLwb8DIksk/maxresdefault.jpg",
                    input_message_content=InputTextMessageContent(
                        f'<code>{n.join(requests.get(f"https://wttr.in/{args}?m&T&lang={lang}").text.splitlines()[:7])}</code>',
                        parse_mode="HTML",
                    ),
                )
            ],
            cache_time=0,
        )
