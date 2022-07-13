import SpeechRecognition as sr

def fala():
    r = sr.SpeechRecognition()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            text = r.recognize_sphinx(audio)
            print(text)
        except sr.UnknownValueError:
            return "Sphinx não pode entender o audio"
        except sr.RequestError:
            return "Sphinx error; {0}".format(e)








