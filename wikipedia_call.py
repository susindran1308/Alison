import os
import wikipedia
from gtts import gTTS
from playsound import playsound
from wolframalpha_call import WolframAlpha

class Wikipedia:
    def __init__(self, lang):
        self.answer = ''
        self.lang = lang

    def execute(self, question):

        if question.lower() in ["hello", "hi", "hey"]:
            return "Hi, How are you?"
        elif question.lower() in ["how are you", "are you ok", "how are you?", "are you ok?"]:
            return "I am great. How are you?"
        elif question.lower() in ["alison", "why is your name alison", "why is your name alison?"]:
            # wikipedia.set_lang(self.lang)
            self.answer = wikipedia.summary("alison d'laurentis", sentences=3)
            return self.answer
        else:
            try:
                wolf = WolframAlpha(self.lang)
                self.answer = wolf.execute(question)
                return self.answer

            except Exception:
                wikipedia.set_lang(self.lang)
                self.answer = wikipedia.summary(question, sentences=3)
                return self.answer

    def audio(self):
        tts = gTTS(text=self.answer, lang=self.lang)
        tts.save("wikipedia.mp3")
        playsound("wikipedia.mp3")
        os.remove("wikipedia.mp3")