import webbrowser

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

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
            print('ab bol v do...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'annie' in command:
                command = command.replace('annie', '')

                print(command)
    except:
        pass
    return command


def run_annie():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is ' + time)
    elif 'date' in command:
        date = datetime.datetime.now().strftime('%a, %b %d, %y')
        print(date)
        talk('current date is ' + date)
    elif 'who is your father' in command:
        talk("Anup kunal created me so he is my father")
    elif 'who is priya' in command:
        talk("priya is girlfriend of kunal")
    elif 'how are you' in command:
        talk("i am absolutely fine")
    elif 'who is your creator' in command:
        talk("Anup kunal created me")
    elif 'who are you' in command:
        talk("i am annie and i am created by anup kunal")
    elif 'who is' in command:
        person = command.replace('who is ', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'tell me about' in command:
        person = command.replace('tell me about', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'are you single' in command:
        talk("no  i am in relationship with kunal")
    elif 'i love you' in command:
        talk("sorry i have no feelings")
    elif 'do you love me' in command:
        talk("sorry i have no feelings")
    elif 'open google' in command:
        webbrowser.open("google.com")
    elif 'open you tube' in command:
        webbrowser.open("youtube.com")

    elif 'kaisi ho' in command:
        talk("mai achhi hu")
    elif 'ganna bjao' in command:
        song = command.replace('ganna bjao', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'apne bare kuchh btao' in command:
        talk("mai annie hu, aur mujhe anup kunal ne bnaya hai")

    elif 'stop || ruk jao' in command:
        talk("thank you for using annie, have a nice day")
        exit(run_annie())

    else:
        talk("please say again")


while True:
    run_annie()
