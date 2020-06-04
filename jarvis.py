import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys
import calendar
import pyowm
import subprocess
from gtts import gTTS
import requests
import json
engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('9HP8WL-PGP9AKJ9T5')

voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)
URL = 'https://www.sms4india.com/api/v1/sendCampaign'

# get request
def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType,
  'phone': phoneNo,
  'message':textMessage,
  'senderid':senderId
  }
  return requests.post(reqUrl, req_params)


def jarvis(audio):
    print('J.A.R.V.I.S: ' + audio)
    engine.say(audio)
    engine.runAndWait()
def findDay(date): 
    born = datetime.datetime.now().weekday() 
    return (calendar.day_name[born]) 

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        jarvis('Good Morning boss!')

    if currentH >= 12 and currentH < 18:
        jarvis('Good Afternoon boss!')

    if currentH >= 18 and currentH !=0:
        jarvis('Good Evening boss!')
input('press any key to continue')
greetMe()
greets = ("hello boss","welcome back boss","nice to see you back sir")
jarvis(random.choice(greets))

def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('boss(vamsi):' + query + '\n')
        
    except sr.UnknownValueError:
        jarvis('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))

    return query
        

if __name__ == '__main__':

    while True:
        query = myCommand().lower()
        if input(s) in query:
            my
        if'shutdown' in query:
            jarvis('initiating shutdown')
            os.system('shutdown /s /t/ 3')
            jarvis('3.2.1.')
                   
        if'restart'in query:
            jarvis('initiating restart')
            os.system('restart /s /t /3')
            jarvis('3.2.1.')
        
        if 'open code.org' in query:
            jarvis('okay')
            webbrowser.open('https://studio.code.org/projects')

        if'open code' in query:
            jarvis('okay')
            codePath = "C:\\Users\\nagma\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        if'code edit' in query:
            jarvis('okay')
            codePath = "C:\\Users\\nagma\\OneDrive\\Desktop\\jarvis.py"
            os.startfile(codePath)
            
        if 'play me a song' in query:
            jarvis("this is my suprise")
            stMsgs = ('https://www.youtube.com/watch?v=Thf60JU8E98'),('https://www.youtube.com/watch?v=XR7Ev14vUh8'),('https://www.youtube.com/watch?v=7wtfhZwyrcc')
            webbrowser.open(random.choice(stMsgs))

        if 'movietime jarvis' in query:
            jarvis("here , your favourite marvel iron man movies are here,kick off with these")
            stMsgs = ('https://www.jiocinema.com/watch/movies/iron-man/0/0/05f9acb08d7c11e89e8fede614b72917/0/0'),('https://www.jiocinema.com/watch/movies/iron-man-2/0/0/fe2cd7f087cc11e89e8fede614b72917/0/0'),('https://www.jiocinema.com/watch/movies/iron-man-3/0/0/23fe3d7087cd11e89e8fede614b72917/0/0'),('https://www.jiocinema.com/watch/movies/marvel-s-avengers--age-of-ultron/0/0/4ae50b404c7511e9903837af22bc175d/0/0'),('https://www.jiocinema.com/watch/movies/marvel-s-the-avengers/0/0/450bcb10890611e89e8fede614b72917/0/0'),('https://www.primevideo.com/detail/0I5LRK6CE9IXBRYT4BB0KXMKP5/ref=atv_dp_season_select_s2')
            webbrowser.open(random.choice(stMsgs))

        if'open settings ' in query:
            jarvis('okay')
            codePath = "C:\\Users\\nagma\\OneDrive\\Desktop\\Settings.lnk"
        if 'open jio movies' in query:
            jarvis('okay')
            webbrowser.open('https://www.jiocinema.com/')
    
        if 'open maps ' in query:
            jarvis('okay')
            webbrowser.open('https://www.google.com/maps/@17.4809431,78.395598,2843m/data=!3m1!1e3')
            
        if 'open amazon' in query:
            jarvis('okay')
            webbrowser.open('https://www.amazon.in/ref=nav_logo')

        if'send sms and introduce' in query:
            
            response = sendPostRequest(URL, 'K7WKDTTP50CUY2327D17Z929PXMQJDH7', '3C1N3LX70PQZ2LBS', 'stage', '7780582568', 'vamsinaidu356@gmail.com', 'hi iam jarvis' )
            """
              Note:-
                you must provide apikey, secretkey, usetype, mobile, senderid and message values
                and then requst to api
            """            
            jarvis(response.text)
 
        if 'open stackoverflow' in query:
            webbrowser.open('www.stackoverflow.com')
           
        if 'open youtube' in query:
            jarvis('okay sir')
            webbrowser.open('https://www.youtube.com/')
            
        if 'tell me a joke' in query:
            jarvis("here it goes sir")
            stMsgs = ["how many intriverts does it take to screw in a light bulb?, the answer- why does it have to be a group activity", "what do father chistmas' little heplers learn at school, the answer- elf-abet", "'write an essay on cricket',the teacher told the class.chintu finishes his work in five minutes. the teacher asks chintu to read aloud his essay to everyone.chintu reads the cricket match is cancelled because of rain."]
            jarvis(random.choice(stMsgs))
                    
        if 'open whatsapp' in query:
            jarvis('okay sir')
            codePath = "C:\\Users\\nagma\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(codePath)
                        
        elif 'open google' in query:
            jarvis('okay sir')
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in query:
            jarvis('okay sir')
            webbrowser.open('https://mail.google.com/mail/u/0/#inbox')

        elif "hi jarvis" in query:
            stMsgs = ["ola,that's hello in portunguese", " hello ,how may i help", "ciao, that's hello in italian,how may i help", "annyeonhaseyo,that's hello in korean how can i help", "gooday ,that's hello in australian, how can i help","namaskaram ,that's hello in telugu","namaskar, thats hello in hindi","vanakkam,that's hello in tamil,how may i help"]
            jarvis(random.choice(stMsgs))

        elif "hey jarvis what are you doing there" in query:
            stMsgs = ["i always try to update myself ", " trying to get myself better", "struck in this computer"]
            jarvis(random.choice(stMsgs))

        elif 'settings' in query:
          jarvis('okay')
          codePath = "C:\\Users\\nagma\\OneDrive\\Desktop\\Settings.lnk"
          os.startfile(codePath)

        elif'stop' in query:
            jarvis('okay')
            jarvis('Bye sir, have a good day.')
            sys.exit()

        if 'weather forecast' in query:
            owm = pyowm.OWM('c2f6bc7935b85ff0a749d23b9586686a')
            observation = owm.weather_at_place('Hyderabad,Telangana')
            w = observation.get_weather()
            print(w)
            print(w.get_wind())
            print(w.get_temperature('celsius'))
            print(w.get_humidity())


        elif 'compose an email to mum' in query:
            jarvis ("okay")
            webbrowser.open('https://mail.google.com/mail/u/0/?tab=wm&ogbl#inbox?compose=GTvVlcSDbFfcmfnKqNShxXbfgGltvfpSwMNzwFSpNfTXqLGZTxdDlNwGnsdRFlgFPWgCxjPSZVVrL')

        elif 'compose an email to myself' in query:
            jarvis ("okay")
            webbrowser.open('https://mail.google.com/mail/u/0/?tab=wm&ogbl#inbox?compose=GTvVlcSDbFfcmfnKqNShxXbfgGltvfpSwMNzwFSpNfTXqLGZTxdDlNwGnsdRFlgFPWgCxjPSZVVrL')

        elif 'compose an email to dad' in query:
            jarvis ("okay")
            webbrowser.open('https://mail.google.com/mail/u/0/?tab=wm&ogbl#inbox?compose=GTvVlcSDbFfcmfnKqNShxXbfgGltvfpSwMNzwFSpNfTXqLGZTxdDlNwGnsdRFlgFPWgCxjPSZVVrL')
          
        elif 'hello' in query:
            jarvis('Hello sir')

        elif 'kill power' in query:
            jarvis('Bye sir, have a good day.')
            sys.exit()

        if 'open fusion 360' in query:
            jarvis('okay')
            codePath = "C:\\Users\\nagma\\AppData\\Local\\Autodesk\\webdeploy\\production\\6a0c9611291d45bb9226980209917c3d\\FusionLauncher.exe"
            os.startfile(codePath)
                                                
        if'open python shell' in query:
            jarvis('okay')
            codePath = "C:\\Users\\nagma\\AppData\\Local\\Programs\\Python\\Python38-32\\Lib\\idlelib\\idle.pyw"
            os.startfile(codePath)
        
        if 'wikipedia' in query.lower():
            jarvis('searching wikipedia.....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences =1)
            print(results)
            jarvis(results)

        if'open camera' in query:
            jarvis('okay')
            codePath = "C:\\Users\\nagma\\OneDrive\\Desktop\\Camera.lnk"
            os.startfile(codePath)
        elif'day' in query:
            jarvis("its:")
            date = datetime.datetime.now()
            jarvis(findDay(date))    
        elif'the time' in query:
            now = datetime.datetime.now()
            jarvis ("its: ")
            jarvis (now.strftime("%H:%M"))
  
        elif'date'in query:
            now = datetime.datetime.now()
            jarvis ("its: ")
            jarvis (now.strftime("%d-%m-%Y"))
        if 'open dashboard' in query:
             jarvis('okay')
             webbrowser.open('https://code.whitehatjr.com/s/dashboard')
        

        if'open skype' in query:
            jarvis('here you go')
            codePath = "C:\\Program Files (x86)\\Microsoft\\Skype for Desktop\\Skype.exe"
            os.startfile(codePath)
            
        if 'open fusion 360' in query:
            jarvis('okay')
            codePath = "C:\\Users\\nagma\\AppData\\Local\\Autodesk\\webdeploy\\production\\6a0c9611291d45bb9226980209917c3d\\FusionLauncher.exe"
            os.startfile(codePath)

        if 'open screen recorder' in query:
          jarvis("okay")
          codePath = "C:\\Users\\nagma\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\ScreenRec\\ScreenRec.lnk"
          os.startfile(codePath)
  
        if 'what' in query:
            
            query = query
            jarvis('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    jarvis('ok, question')
                    jarvis('getting answers...')
                    jarvis("according to woframaplha.......")
                    jarvis(results)
                except:
                    jarvis('k')
                 
                         
            except:
                jarvis('..')
        jarvis("next")
                 
        
