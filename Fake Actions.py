from asyncio import sleep

from telethon import functions

from random import randint
from .. import loader, utils


@loader.tds
class FakeMod(loader.Module):
    """Имитация ваших действий"""

    strings = {"name": "Fake Actions"}

    async def typecmd(self, message):
        """Имитация набора текста"""
        activity_time = utils.get_args(message)
        await message.delete()
        if activity_time:
            try:
                async with message.client.action(message.chat_id, "typing"):
                    await sleep(int(activity_time[0]))
            except BaseException:
                return
        else:
            try:
                async with message.client.action(message.chat_id, "typing"):
                    await sleep(randint(30, 60))
            except BaseException:
                return

    async def voicecmd(self, message):
        """Имитация отправки голосового сообщения"""
        activity_time = utils.get_args(message)
        await message.delete()
        if activity_time:
            try:
                async with message.client.action(message.chat_id, "voice"):
                    await sleep(int(activity_time[0]))
            except BaseException:
                return
        else:
            try:
                async with message.client.action(message.chat_id, "voice"):
                    await sleep(randint(30, 60))
            except BaseException:
                return

    async def gamecmd(self, message):
        """Имитация вашей игровой активности"""
        activity_time = utils.get_args(message)
        await message.delete()
        if activity_time:
            try:
                async with message.client.action(message.chat_id, "game"):
                    await sleep(int(activity_time[0]))
            except BaseException:
                return
        else:
            try:
                async with message.client.action(message.chat_id, "game"):
                    await sleep(randint(30, 60))
            except BaseException:
                return

    async def videocmd(self, message):
        """Имитация отправки видео"""
        activity_time = utils.get_args(message)
        await message.delete()
        if activity_time:
            try:
                async with message.client.action(message.chat_id, "video"):
                    await sleep(int(activity_time[0]))
            except BaseException:
                return
        else:
            try:
                async with message.client.action(message.chat_id, "video"):
                    await sleep(randint(30, 60))
            except BaseException:
                return

    async def photocmd(self, message):
        """Имитация отправки фото"""
        activity_time = utils.get_args(message)
        await message.delete()
        if activity_time:
            try:
                async with message.client.action(message.chat_id, "photo"):
                    await sleep(int(activity_time[0]))
            except BaseException:
                return
        else:
            try:
                async with message.client.action(message.chat_id, "photo"):
                    await sleep(randint(30, 60))
            except BaseException:
                return

    async def documentcmd(self, message):
        """Имитация отправки документа"""
        activity_time = utils.get_args(message)
        await message.delete()
        if activity_time:
            try:
                async with message.client.action(message.chat_id, "document"):
                    await sleep(int(activity_time[0]))
            except BaseException:
                return
        else:
            try:
                async with message.client.action(message.chat_id, "document"):
                    await sleep(randint(30, 60))
            except BaseException:
                return

    async def locationcmd(self, message):
        """Имитация отправки местоположения"""
        activity_time = utils.get_args(message)
        await message.delete()
        if activity_time:
            try:
                async with message.client.action(message.chat_id, "location"):
                    await sleep(int(activity_time[0]))
            except BaseException:
                return
        else:
            try:
                async with message.client.action(message.chat_id, "location"):
                    await sleep(randint(30, 60))
            except BaseException:
                return

    async def recordvideocmd(self, message):
        """Имитация записи видео"""
        activity_time = utils.get_args(message)
        await message.delete()
        if activity_time:
            try:
                async with message.client.action(message.chat_id, "record-video"):
                    await sleep(int(activity_time[0]))
            except BaseException:
                return
        else:
            try:
                async with message.client.action(message.chat_id, "record-video"):
                    await sleep(randint(30, 60))
            except BaseException:
                return

    async def recordvoicecmd(self, message):
        """Имитация записи голосового сообщения"""
        activity_time = utils.get_args(message)
        await message.delete()
        if activity_time:
            try:
                async with message.client.action(message.chat_id, "record-audio"):
                    await sleep(int(activity_time[0]))
            except BaseException:
                return
        else:
            try:
                async with message.client.action(message.chat_id, "record-audio"):
                    await sleep(randint(30, 60))
            except BaseException:
                return

    async def recordroundcmd(self, message):
        """Имитация записи видео в кружочке"""
        activity_time = utils.get_args(message)
        await message.delete()
        if activity_time:
            try:
                async with message.client.action(message.chat_id, "record-round"):
                    await sleep(int(activity_time[0]))
            except BaseException:
                return
        else:
            try:
                async with message.client.action(message.chat_id, "record-round"):
                    await sleep(randint(30, 60))
            except BaseException:
                return

    async def scrncmd(self, message):
        """Уведомление о скриншоте (Только личные сообщения)"""
        a = 1
        r = utils.get_args(message)
        if r and r[0].isdigit():
            a = int(r[0])
        for _ in range(a):
            await message.client(
                functions.messages.SendScreenshotNotificationRequest(
                    peer=message.to_id, reply_to_msg_id=message.id
                )
            )
        await message.delete()