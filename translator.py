from .. import loader, utils
from googletrans import LANGUAGES, Translator


@loader.tds
class TranslatorMod(loader.Module):
    """Гугл Переводчик"""
    strings = {'name': 'GTranslate'}

    async def trslcmd(self, message):
        """(с какого языка перевести) (на какой перевести) (текст) или .trsl (на какой язык перевести) (реплай на текст); просмотр всех языков – .trsl langs"""
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        langs = LANGUAGES
        lang = args.split()
        tr = Translator().translate
        if not args and not reply:
            return await message.edit("Нет аргументов или реплая.")
        if args == "langs":
            return await message.edit("<code>" + '\n'.join(str(langs).split(', ')) + "</code>")
        if reply:
            try:
            	trslreply = True
            	text = reply.text
            	if len(lang) >= 2:
            	    trslreply = False
                dest = langs[lang[0]]
                r = tr(args.split(' ', 1)[1] if trslreply is False else text, dest=dest)
            except: r = tr(reply.text)
        else:
            try:
                try:
                    src = langs[lang[0]]
                    dest = langs[lang[1]]
                    text = args.split(' ', 2)[2]
                    r = tr(text, src=src, dest=dest)
                except:
                    dest = langs[lang[0]]
                    text = args.split(' ', 1)[1]
                    r = tr(text, dest=dest)
            except KeyError: r = tr(args)
        return await message.edit(f"<b>[{r.src} ➜ {r.dest}]</b>\n{r.text}")