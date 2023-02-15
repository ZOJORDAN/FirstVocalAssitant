
import speech_recognition as sr
"API qui permet de faire la transcription voix – texte"
import pyaudio
"Cette librairie permet de jouer et d’enregistrer de l’audio"
import pywhatkit
import pyttsx3
"Une bibliothèque de conversion texte-parole en Python"
import datetime
 

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', 'french')


def talk(text,rate=114):
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    "débit de parole"
    engine.setProperty('volume',1.0) 
    "volume"
    engine.setProperty('voice', voices[1].id)
    "changement de voix , 0 pour homme 1 pour"
    engine.say(text)
    engine.runAndWait()
    


def take_command():
    try:
        with sr.Microphone() as source:
            print('en ecoute...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice,language='fr-FR')
            command = command.lower()
            if 'griot' in command:
                command = command.replace('griot', '')
                print(command)
    except:
        pass
    return command


def run_griot():
    command = take_command()
    print(command)
    if 'heure' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('il est actuellement' + time)
    elif 'date' in command:
        talk('Regarde ton téléphone frère')
    elif 'Bonjour' in command:
        talk('Bonjour boss')
    elif 'es tu célibataire ?' in command:
        talk('je suis en couple avec alexa , mais ne le dis pas à siri')
    else:
        talk("veuillez répeter s'il vous plait")


while True:
    run_griot()