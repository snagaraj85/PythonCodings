import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!") 

    else:
        speak("Good Evening!")  

    speak("I am JARVIS Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open mighty pups' in query:
            webbrowser.open("https://www.youtube.com/watch?v=eOYL8qQxxPw")   

        elif 'play music' in query:
            music_dir = 'E:\\Tamil Music\\Tamil Cute Mp3 Collection in 80s'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open notepad' in query:
            codePath = "C:\\Windows\\Notepad.exe"
            os.startfile(codePath)
            
        elif 'open photo' in query:
            codePath = "E:\\Rudhraesh\\11.09.16\\DSC_0545.jpg"
            os.startfile(codePath)

        elif 'shutdown computer' in query:
            print(f"Thank you, System is shutting down...")     
            speak(f"Thank you, System is shutting down...")
            os.system("shutdown /s /t 1")

        elif 'restart computer' in query:
            print(f"Thank you, System is restarting...")     
            speak(f"Thank you, System is restarting...")
            os.system("shutdown /r /t 1")

        elif 'logoff computer' in query:
            print(f"Thank you, Logging off you...")     
            speak(f"Thank you, Logging off you...")
            os.system("shutdown -l")   

        elif 'goodbye' in query:
              print(f"Thank you, bye for now. Visit me again...")     
              speak(f"Thank you, bye for now. Visit me again...")
              break
            

        
                
