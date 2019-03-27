import os

import wolframalpha
from googletrans import Translator
from gtts import gTTS
from playsound import playsound


class WolframAlpha:

    def __init__(self, lang):
        self.answer=''
        self.lang = lang

    def execute(self, question):
        app_id = "9RV23R-TXQ2XU678Q"

        client = wolframalpha.Client(app_id)

        result = client.query(question)
        self.answer = next(result.results).text

        return self.answer

    def audio(self):
        tts = gTTS(text=self.answer, lang=self.lang)
        tts.save("wolfram.mp3")
        playsound("wolfram.mp3")
        os.remove("wolfram.mp3")

