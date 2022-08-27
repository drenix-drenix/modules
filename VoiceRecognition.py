from io import BytesIO

# requires: pydub speechRecognition
import speech_recognition as srec
from pydub import AudioSegment as auds

from .. import loader, utils


@loader.tds
class VoiceRecognitionMod(loader.Module):
    "Распознавание речи через Google Recognition API"
    strings = {"name": "VoiceRecognition", "pref": "<b>[VRC]</b> "}

    @loader.owner
    async def recvcmd(self, m):
        "(реплай на голосовое сообщение/аудио) - распознать речь"
        reply = await m.get_reply_message()
        if reply and reply.file.mime_type.split("/")[0] == "audio":
            m = await utils.answer(m, self.strings["pref"] + "Скачивание...")
            source = BytesIO(await reply.download_media(bytes))
            source.name = reply.file.name
            out = BytesIO()
            out.name = "recog.wav"
            m = await utils.answer(m, self.strings["pref"] + "Конвертация...")
            auds.from_file(source).export(out, "wav")
            out.seek(0)
            m = await utils.answer(m, self.strings["pref"] + "Обработка...")
            recog = srec.Recognizer()
            sample_audio = srec.AudioFile(out)
            with sample_audio as audio_file:
                audio_content = recog.record(audio_file)
            await utils.answer(
                m,
                self.strings["pref"]
                + recog.recognize_google(audio_content, language="ru-RU"),
            )
        else:
            await utils.answer(m, self.strings["pref"] + "реплай на аудио/голосовое сообщение...")