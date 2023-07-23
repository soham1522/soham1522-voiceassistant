import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import pyaudio
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    
    speak("Hi soham Please tell me how can i help you")
    
    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n")
    
    except Exception as e:
        print("say that again please...")
        return "None"
    return query   

if __name__ == '__main__':
    wishme()
    while True:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
            
        elif 'google' in query:
            speak("opening google")
            webbrowser.open("google.com")
        
        elif 'email' in query:
            speak("opening email")
            webbrowser.open("gmail.com")
        
        elif 'stack overflow' in query:
            speak("opening stackoverflow")
            webbrowser.open("stackoverflow.com")    
            
        elif 'the time' in query:
            strTime = datetime.datetime.now.strftime("%H:%M:%S")
            speak(f"sir the time is{strTime}")
            
        elif 'resume' in query:
            speak("opening your resume")
            resumepath = "C:\\Users\\soham\\OneDrive\\Desktop\\Soham Deshmukh .pdf"
            os.startfile(resumepath)
        
        elif 'chrome' in query:
            speak("opening chrome")
            chromepath = "C:\\Users\\Public\\Desktop\\Google Chrome.lnk"
            os.startfile(chromepath)
            
            