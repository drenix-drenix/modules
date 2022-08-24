from .. import loader, utils
from asyncio import sleep
import random

class TimeDelMsgMod(loader.Module):
	"""Данный модуль удаляет ваше сообщение через определенное время."""
	strings = {"name": "TimeDelMsg"}
	
	async def dcmd(self, message):
		"""Пример: .d 5s Привет, как дела?\ns - секунды; m - минуты; h - часы."""
		args = utils.get_args_raw(message)
		text = args.split(" ")
		txt = text[1:]
		txtjoin = " ".join(txt)
		numbs = text[0]
		timeq = list(numbs)
		lentime = len(timeq)
		secormin = timeq[lentime - 1]
		timeq.pop(lentime - 1)
		nm = int("".join(timeq))
		if secormin == "s":			
			timesmh = nm
		elif secormin == "m":
			timesmh = nm * 60
		elif secormin == "h":
			timesmh = nm * 60 * 60
		else:
			await message.reply("<b>Время указано неверно!\nМожно использовать только: s - секунды, m - минуты, h - часы.</b>")
		await message.edit(txtjoin)
		await sleep(timesmh)
		await message.delete()
		