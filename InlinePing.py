import logging
import time

from telethon.tl.types import Message

from .. import loader
from ..inline.types import InlineCall, InlineQuery

logger = logging.getLogger(__name__)


@loader.tds
class PingerMod(loader.Module):
    """Inline Pinger For Test"""

    strings = {
        "name": "InlinePing",
        "results_ping": "✨ <b>Telegram ping:</b> <code>{}</code> <b>ms</b>"
    }

    strings_ru = {"results_ping": "✨ <b>Скорость отклика Telegram:</b> <code>{}</code> <b>ms</b>"}

    @loader.command(ru_doc="Проверить скорость отклика юзербота")
    async def iping(self, message: Message):
        """Test your userbot ping"""
        start = time.perf_counter_ns()

        await self.inline.form(
            self.strings("results_ping").format(
                round((time.perf_counter_ns() - start) / 10**3, 3),
            ),
            reply_markup=[[{"text": "⏱️ Проверить ещё раз", "callback": self.ladno}]],
            message=message,
        )

    async def ladno(self, call: InlineCall):
        start = time.perf_counter_ns()
        await call.edit(
			self.strings("results_ping").format(
                round((time.perf_counter_ns() - start) / 10**3, 3),
            ),
			reply_markup=[[{"text": "⏱️ Проверить ещё раз", "callback": self.ladno,}],]
		)

    async def ping_inline_handler(self, query: InlineQuery):
        """Test your userbot ping"""
        start = time.perf_counter_ns()
        ping = self.strings("results_ping").format(
                round((time.perf_counter_ns() - start) / 10**3, 3),
            )
        button = [{
                    "text": "⏱️ Проверить ещё раз", 
                    "callback": self.ladno
                 }]
        return {
            "title": "Пинг",
            "description": "Нажми сюда",
            "thumb": "https://te.legra.ph/file/5d8c7f1960a3e126d916a.jpg",
            "message": ping,
            "reply_markup": button,
        }