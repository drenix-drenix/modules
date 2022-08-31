from .. import loader, utils


def register(cb):
    cb(HiddenTagMod())

class HiddenTagMod(loader.Module):
    """Скрытно тегнуть пользователя."""
    strings = {'name': 'HiddenTag'}

    async def tagcmd(self, message):
        """@пользователь (ваш текст) (необязательно)"""
        args = utils.get_args_raw(message).split(' ')
        reply = await message.get_reply_message()
        user, tag = None, None
        try:
            if len(args) == 1:
                args = utils.get_args_raw(message)
                user = await message.client.get_entity(args if not args.isnumeric() else int(args))
                tag = 'Тег пользователя'
            elif len(args) >= 2:
                user = await message.client.get_entity(args[0] if not args[0].isnumeric() else int(args[0]))
                tag = utils.get_args_raw(message).split(' ', 1)[1]
        except: return await message.edit("Не удалось найти пользователя.")
        await message.delete()
        await message.client.send_message(message.to_id, f'{tag} <a href="tg://user?id={user.id}">\u2060</a>', reply_to=reply.id if reply else None)