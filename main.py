import pyttsx3 

text_speech = pyttsx3.init()
while True :
    text = input("Enter the text which you want to say : ")
    if text == "q":
        text_speech.say("Thanks For Using RoboSpeaker")
        text_speech.runAndWait()
        break
    else:
        text_speech.say(text)
        text_speech.runAndWait()