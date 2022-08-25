from .. import loader, utils
import os
import yadisk

class testMod(loader.Module):
	strings = {"name": "Яндекс Диск"}
	
	async def дискcmd(self, message):
		args = utils.get_args_raw(message)
		y = yadisk.YaDisk(token=args)
		reply = await message.get_reply_message()
		file = reply.media.document.attributes[0].file_name
		if reply.media:
			await message.client.download_media(message=reply)
		y.upload(file,file)
		os.remove(file)
		await message.edit(f'<b>Файл <code>{file}</code>\nУспешно загружен на ЯДиск!\n</b>')