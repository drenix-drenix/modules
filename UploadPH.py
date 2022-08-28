from .. import loader, utils
import asyncio
import requests
from telethon.tl.types import DocumentAttributeFilename

def register(cb):
 cb(UploadPHMod())

class UploadPHMod(loader.Module):
	"""Загрузка видео и фото на telegra.ph"""
	strings = {"name": "UploadPH"}

	def __init__(self):
		self.name = self.strings['name']
		
	
	async def phcmd(self, message):
			"""(реплай на фото или видео)"""
			if message.is_reply:
				reply_message = await message.get_reply_message()
				data = await check_media(reply_message)
				if isinstance(data, bool):
					await message.edit("<b>Реплай на фото или видео/gif</b>")
					return
			else:
				await message.edit("<b>Реплай на фото или видео/gif</b>")
				return
					
				
			file = await message.client.download_media(data, bytes)
			path = requests.post('https://te.legra.ph/upload', files={'file': ('file', file, None)}).json()
			try:
				link = 'https://te.legra.ph'+path[0]['src']
			except KeyError:
				link = path["error"]
			await message.edit("<b>"+link+"</b>")
				
			
async def check_media(reply_message):
	if reply_message and reply_message.media:
		if reply_message.photo:
			data = reply_message.photo
		elif reply_message.document:
			if DocumentAttributeFilename(file_name='AnimatedSticker.tgs') in reply_message.media.document.attributes:
				return False
			if reply_message.audio or reply_message.voice:
				return False
			data = reply_message.media.document
		else:
			return False
	else:
		return False
	if not data or data is None:
		return False
	else:
		return data
		
		
		