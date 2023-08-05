import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import wolframalpha
import random
import calendar

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning')
        print('Good Morning')
    elif hour>=12 and hour<16:
        speak('Good Afternoon')
        print('Good Afternoon')
    else:
        speak('Good Evening')
        print('Good Evening')
    print('Sir! I am your digital assistant CHARI. How can i help you?')
    speak('Sir! I am your digital assistant CHARI. How can i help you?')

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print(e)
        print("Sorry! Please say that again ....")
        speak("Sorry! Please say that again ....")
        return "None"
    return query

def getDate():
    now=datetime.datetime.now()
    my_date=datetime.datetime.today()
    weekday=calendar.day_name[my_date.weekday()]    
    monthnum=now.month
    daynum=now.day
    month_names=['January','February','March','April','May','June','July','August','September','October','November','December']

    ordinalnumber=['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th','11th','12th','13th','14th','15th','16th','17',
    '18th','19','20th','21st','22nd','23rd','24th','25','26th','27th','28th','29th','30th','31st']
    return 'Today is  '+weekday+' '+month_names[monthnum-1]+' '+ordinalnumber[daynum-1]+'. '


def sendEmail(to,content):
    server=smtplib.SMTP('smtplib.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sendermail@gmail.com', 'password')
    server.sendmail('sendermail@gmail.com', to, content)
    server.close()    


if __name__ == '__main__':
    wishMe()
    while True:
        query=takeCommand().lower()

        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query=query.replace("wikipedia", "")
            results=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)


        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open youtube' in query:
            webbrowser.open("youtube.com") 
        elif 'open github' in query:
            webbrowser.open("github.com")
        elif 'open gmail' in query:
            webbrowser.open("gmail.com")    
        elif 'open twitter' in query:
            webbrowser.open("twitter.com")
        elif 'open steam' in query:
            webbrowser.open("steam.com")    

        
            
        elif 'open calculator' in query:
            query.find('calculator')
            speak("Opening calculator!")
            os.startfile("calc")

            
        elif 'open command prompt' in query:
            cppath=("C:\\Users\\anand\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt")       
            cp=os.startfile(cppath)

        elif 'visual studio code' in query:
            vsc=("C:\\Users\\anand\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code") 
            os.startfile(vsc) 

        elif 'play music' in query:
            music_dir='F:\\Nani\\SONGS'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))  

        elif 'the time' in query:
            Time =datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir,The time is {Time}")
            speak(f"Sir,The time is {Time}")

        elif "today's date" in query:
            print(getDate())   
            speak(getDate())

        elif 'open movies' in query:
            mpath="F:\\Movies"
            os.startfile(mpath)


        elif 'email to anand' in query:
            try:
                speak("What should I say?")
                content="hello"
                to='anandyenigalla7077@gmail.com'
                sendEmail(to,content)
                speak('email has been sent')
            except Exception as e:
                print(e)
                speak("Sorry sir!email can't be sent")    

        elif 'quit' in query:
         print('Bye sir! Have a nice day')
         speak('Bye sir! Have a nice day')
         exit()    



  
           











