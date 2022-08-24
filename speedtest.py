from typing import Tuple

from telethon import TelegramClient
from telethon.tl.custom import Message
from telethon.tl.functions.channels import JoinChannelRequest

import speedtest  # pylint: disable=import-self

from .. import loader, utils


# noinspection PyCallingNonCallable,PyAttributeOutsideInit
# pylint: disable=not-callable,attribute-defined-outside-init,invalid-name
@loader.tds
class SpeedtestMod(loader.Module):
    """Проверяет скорость интернета на вашем сервере на speedtest.net"""

    strings = {
        "name": "Speedtest",
        "running": "🕑 <b>Проверяем скорость интернета...</b>",
        "result": (
            "<b>⬇️ Скачать: <code>{download}</code> MBit/s</b>\n"
            "<b>⬆️ Загрузить: <code>{upload}</code> MBit/s</b>\n"
            "<b>🏓 Пинг: <code>{ping}</code> ms</b>"
        ),
    }
    

    async def client_ready(self, client: TelegramClient, _):
        """client_ready hook"""
    async def speedtestcmd(self, message: Message):
        """Run speedtest"""
        m = await utils.answer(message, self.strings("running"))
        results = await utils.run_sync(self.run_speedtest)
        await utils.answer(
            m,
            self.strings("result").format(
                download=round(results[0] / 1024 / 1024),
                upload=round(results[1] / 1024 / 1024),
                ping=round(results[2], 3),
            ),
        )

    @staticmethod
    def run_speedtest() -> Tuple[float, float, float]:
        """Speedtest using `speedtest` library"""
        s = speedtest.Speedtest()  # pylint: disable=no-member
        s.get_servers()
        s.get_best_server()
        s.download()
        s.upload()
        res = s.results.dict()
        return res["download"], res["upload"], res["ping"]