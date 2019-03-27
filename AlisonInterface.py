from PyQt5 import QtWidgets
import sys
from gtts import gTTS
from playsound import playsound
import os
from googletrans import Translator
import wikipedia_call


class Interface():
    def __init__(self, lang):
        self.name = ''
        self.lang = lang
        self.app = QtWidgets.QApplication(sys.argv)
        self.w = QtWidgets.QWidget()

    def warning(self):
        msg = QtWidgets.QMessageBox()
        msg.setText("Type your name: ")
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        retval = msg.exec_()


    def main(self):
        b = QtWidgets.QLabel(self.w)

        self.w.setGeometry(300, 300, 500, 450)
        b.move(50, 20)
        self.w.setWindowTitle("Alison")

        alison_text = "Hello! I am Alison, Your virtual assistant."

        if self.lang == 'ta':
            t = Translator()
            alison_text = t.translate(alison_text, dest=self.lang).text

        self.name , okPressed = QtWidgets.QInputDialog.getText(self.w, "Alison", "Your name:", QtWidgets.QLineEdit.Normal, "")

        while self.name == '':
            self.warning()
            self.name, okPressed = QtWidgets.QInputDialog.getText(self.w, "Alison", "Your name:", QtWidgets.QLineEdit.Normal, "")

        index=alison_text.index("!")
        alison_text = alison_text[:index] + " " + self.name + alison_text[index:]
        b.setText(alison_text)

        textbox = QtWidgets.QLineEdit(self.w)
        textbox.move(50, 50)
        textbox.resize(380, 40)

        button = QtWidgets.QPushButton('Ask Alison', self.w)
        button.move(220, 100)

        ans = QtWidgets.QTextEdit(self.w)
        ans.move(50, 150)
        ans.resize(380, 200)
        ans.setText("_____")

        def on_click():
            wiki = wikipedia_call.Wikipedia(self.lang)
            text = textbox.text()
            textbox.setText("Please Wait ...... Fetching")
            answer = wiki.execute(text)
            ans.setText(answer)
            ans.update()
            self.w.update()
            wiki.audio()

        # connect the signals to the slots
        button.clicked.connect(on_click)

        self.w.show()
        tts = gTTS(text=alison_text, lang=self.lang)
        tts.save("hello.mp3")

        playsound("hello.mp3")
        os.remove("hello.mp3")

        sys.exit(self.app.exec_())