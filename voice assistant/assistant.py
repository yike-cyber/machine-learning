

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
machine = pyttsx3.init()


def talk(text):
    machine.say(text)
    machine.runAndWait()


def input_instruction():
    global instruction

    try:
        with sr.Microphone() as origin:
            print("listening")
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            if "jarvis" in instruction:
                instruction = instruction.replace('jarvis', ' ')
                print(instruction)
            print(instruction)

    except:
        pass

    return instruction


def play_jarvis():
    instruction = input_instruction()
    print(instruction)
    if 'play' in instruction:
        song = instruction.replace('play', '')
        talk("playing " + song)
        pywhatkit.playonyt(song)

    elif 'time' in instruction:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + current_time)

    elif 'date' in instruction:
        current_date = datetime.datetime.now().strftime('%d/%m/%Y')
        talk("Today's date is " + current_date)

    elif 'how are you' in instruction:
        talk('I am fine, how are you?')

    elif 'what is your name' in instruction:
        talk('I am Jarvis, what can I do for you?')

    elif 'who is' in instruction:
        person = instruction.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print('hello')
        talk(info)

    else:
        talk('Please repeat')


play_jarvis()
