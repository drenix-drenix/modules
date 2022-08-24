from .. import loader, utils


def register(cb):
    cb(TikTokMod())

class TikTokMod(loader.Module):
    """Модуль для скачивания видео без водяных знаков с TikTok"""
    strings = {'name': 'TikTok no WaterMark'}

    async def tikcmd(self, message):
        """Отправление видео"""
        await utils.answer(message, 'Видео загружается...')
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, "Отправь мне ссылку на видео из TikTok")
            return
        r = await message.client.inline_query('tikdobot', args)
        await message.client.send_file(message.to_id, r[1].result.content.url)
        await message.delete()