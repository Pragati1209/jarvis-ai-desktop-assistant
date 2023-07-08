import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour) 
    if hour>=0 and hour<=12:
        speak("Good Morning!")
    elif hour>=0 and hour<18:
        speak("Good Afternoon!")      
    else:
        speak("Good Evening!")      
    speak("I am Jarvis maam. Please tell me How may I help you?")

#def sendEmail(to,content):
  #  server=smtplib.SMTP('smtp.gmail.com',587)
   # server.ehlo()
   # server.starttls()
   # server.login('emailid','password')
    #server.sendmail('youremail',to,content)
    #server.close

def takeCommand():
    #it takes microphone inpput and returns string output

    r=sr.Recognizer()    
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print("User said:",query)
         
    except Exception as e:
       # print(e)
         print("Say that again please...")  
         return "None"
    return query   

if __name__ == "__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching wikipedia....")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia,")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'play music' in query:
            music='C:\\Users\\Pragati Singh\\Desktop\\New folder (2)\\JARVIS\\favourite song'
            songs=os.listdir(music)
            print(songs)
            os.startfile(os.path.join(music,songs[0]))
        elif 'the time' in query:   
            strTime=datetime.datetime.now().strftime("%H:%M:%S") 
            speak(f"Maam the Time is{strTime}")
        #elif 'send email'in query:
           # try:
             #   speak("What should I say?")
             #   content=takeCommand()
             #   to="pragatisingh.12sept@gmail.com"
             #   sendEmail(to,content)
             #   speak("Email has been sent")
           # except Exception as e:
              #  speak("Sorry Pragati,I was unable to send the email")   
            
   
    