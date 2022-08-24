from .. import loader, utils
from asyncio import sleep

class EdMsgMod(loader.Module):
	strings = {"name": "EdMsg"}
	
	async def edcmd(self, message):
		args = utils.get_args_raw(message)
		text = args.split(" | ")
		words = text[1]
		text1 = text[0].split(" ")
		time = int(text1[0]) * 60
		words1 = " ".join(text1[1:])		
		await message.edit(words1)
		await sleep(time)
		await message.edit(words)
		