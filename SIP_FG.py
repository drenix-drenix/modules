from .. import loader, utils
import requests
import os

class SIPMod(loader.Module):
	strings = {"name": "SIP_FG"}

	async def sipcmd(self, message):
		args = utils.get_args_raw(message)
		try:
			response = requests.get(url=f'http://ip-api.com/json/{args}').json()

			data = {
				'[Айпи]': response.get('query'),
				'[Провайдер]': response.get('isp'),
				'[Организация]': response.get('org'),
				'[Страна]': response.get('country'),
				'[Регион]': response.get('regionName'),
				'[Город]': response.get('city'),
				'[ZIP]': response.get('zip'),
				'[Широта]': response.get('lat'),
				'[Долгота]': response.get('lon'),
	        }

			full = ''
			for k, v in data.items():
				full += f'{k} : {v}\n'

			await message.edit(f'{full}\nПоиск информации по IP завершён!')
			
		except requests.exceptions.ConnectionError:
			await message.edit('Ошибка!')
