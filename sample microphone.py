import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    audio = r.listen(source)

try:
    t = (r.recognize_google(audio))
    print(t)

except sr.UnknownValueError:
    print("Google speech recognition couldn't understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Cloud Speech service; {0}".format(e))
