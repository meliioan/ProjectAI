import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Melly asculta...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'Melly' in command:
                command = command.replace('Melly', '')
                print(command)


    except:
        pass
    return command


def run_melly():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        print(time)
        talk('Current time is' + time)

    elif 'who is' in command:
        person = command.replace('who is', "")
        info = wikipedia.summary(person,1)
        print(info)
        talk(info)

    elif 'date' in command:
        talk("Sorry, I have a boyfriend")
    elif 'Are you single' in command:
        talk("None of your business")
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say that again.')

run_melly()