import random
from .. import loader
from telethon.tl.types import Message


@loader.tds
class PremiumStickersMod(loader.Module):
    """Отправляет Premium стикеры бесплатно"""

    strings = {"name": "PremiumStickers"}

    async def premstickcmd(self, message: Message):
        """Отправка случайных Premium стикеров без Premium"""
        if message.out:
            await message.delete()

        await message.respond(
            f'<a href="https://t.me/premium/{random.randint(18, 131)}">­</a>',
        )