import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyjokes
from googlesearch import search
search("Google", lang='en')

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # setting female voice

engine.say('Hello, I am pooh, what can I do for you?')

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
    except:
        pass
    return command

def run_pooh():
    command = take_command()
    print(command)

    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song) #play on youtube

    elif 'google' in command:
        value = command.replace('google', '')
        pywhatkit.search(value)
        print('searching' +value)
        talk(value)

    elif 'search' in command:
        value = command.replace('search', '')
        pywhatkit.search(value)
        print('searching' +value)
        talk(value)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
        print(time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        pywhatkit.search(person)
        print(person)
        talk(person)
    elif 'date' in command:
        date = datetime.datetime.now().strftime('%d:%B:%Y')
        talk('date is' + date)
        print(date)
    elif 'are you single' in command:
        talk('I am in a relationship with my wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'how are you' in command:
        talk('I am fine. You are very kind to ask, especially in these tempestuous times')
    elif 'hello' in command:
        talk('Hello dear!')
    elif 'thank you' in command:
        talk('I am honoured to serve')
    elif 'bye' in command:
        talk('Have a good day!')
        exit()
    else:
        talk('Something went wrong! please say it again')

while True:

    run_pooh()
