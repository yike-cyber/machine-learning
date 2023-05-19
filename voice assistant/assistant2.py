import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import nltk
from nltk.corpus import wordnet

listener = sr.Recognizer()
machine = pyttsx3.init()
# nltk.download('wordnet')  # Download the WordNet corpus for word definitions

# Dictionary to store word information
word_info = {}

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

def learn_word(word):
    if word in word_info:
        talk(f"I already know about {word}")
        return

    talk(f"Sure, let's learn about {word}")
    talk(f"What is the definition of {word}?")
    definition = input_instruction()
    talk(f"What is the pronunciation of {word}?")
    pronunciation = input_instruction()
    talk(f"What are the synonyms of {word}?")
    synonyms = input_instruction()
    talk(f"What are the antonyms of {word}?")
    antonyms = input_instruction()

    # Store word information in the dictionary
    word_info[word] = {
        'definition': definition,
        'pronunciation': pronunciation,
        'synonyms': synonyms,
        'antonyms': antonyms
    }

    talk(f"Great! I have learned about {word}")

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

    elif 'define' in instruction:
        word = instruction.replace('define', '').strip()
        if word in word_info:
            talk(f"The definition of {word} is: {word_info[word]['definition']}")
        else:
            talk(f"I don't know the definition of {word}. Would you like to teach me?")
            response = input_instruction()
            if 'yes' in response:
                learn_word(word)

    elif 'pronounce' in instruction:
        word = instruction.replace('pronounce', '').strip()
        if word in word_info:
            talk(f"The pronunciation of {word} is: {word_info[word][' pronunciation']}")
    else:
        talk(f"I don't know the pronunciation of {word}. Would you like to teach me?")
        response = input_instruction()
    if 'yes' in response:
        learn_word(word)
    elif 'synonym' in instruction:
        word = instruction.replace('synonym', '').strip()
    if word in word_info:
        synonyms = word_info[word]['synonyms']
        talk(f"The synonyms of {word} are: {synonyms}")
    else:
        talk(f"I don't know the synonyms of {word}. Would you like to teach me?")
        response = input_instruction()
    if 'yes' in response:
        learn_word(word)

    elif 'antonym' in instruction:
        word = instruction.replace('antonym', '').strip()
        if word in word_info:
           antonyms = word_info[word]['antonyms']
           talk(f"The antonyms of {word} are: {antonyms}")
        else:
            talk(f"I don't know the antonyms of {word}. Would you like to teach me?")
            response = input_instruction()
        if 'yes' in response:
            learn_word(word)

    else:
         talk('Please repeat')
play_jarvis()


