from .. import loader, utils
class КалькуляторMod(loader.Module):
	"""Простой калькулятор в Telegram"""
	strings = {'name': 'Калькулятор'}
	
	async def calccmd(self, message):
		"""(выражение или реплай на то, что нужно посчитать)
		
			Функции:
			** - возвести в степень
			/ - деление
			% - деление по модулю"""
		question = utils.get_args_raw(message)
		reply = await message.get_reply_message()
		if not question:
			if not reply:
				await utils.answer(message, "<b>2+2=5</b>")
				return
			else:
				question = reply.raw_text
		try:
			answer = eval(question)
			answer = f"<b>{question}=</b><code>{answer}</code>"
		except Exception as e:
			answer =  f"<b>{question}=</b><code>{e}</code>"
		await utils.answer(message, answer)
	
