import speech_recognition as sr

record = sr.Recognizer()
while(1):
    with sr.Microphone() as source:
        print("Recording")
        audio = record.listen(source)
        text = record.recognize_google(audio)
        print("you said "+text)
