from PyQt6 import *
from tkinter import *
import ttkSimpleDialog
import speech_recognition as sr
import pyttsx3
import pyaudio
# import winshell
import wikipedia
from Foundation import *
import webbrowser
from random import Random
import json
import keyboard
import operator
import datetime
import pyjokes
import pywhatkit
#import PyWhatKit
from playsound import playsound
import more_itertools
import importlib.util
import time
import sys
import Foundation
import os
import subprocess
#from elasticsearch import Elasticsearch
#from elasticsearch.helpers import bulk
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
import cv2
from requests import get
#import feedparser
import smtplib
import ctypes
#import shutil
#from twilio.rest import Client
#from clint.textui import progress
#from ecapture import ecapture as ec
#from bs4 import BeautifulSoup
# import win32com.client as wincl
from urllib.request import urlopen

# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# engine.setProperty('voices', voices[0].id)


r = sr.Recognizer()
mic = sr.Microphone()
with mic as source:
    print("Listening....")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    print(r.recognize_google(audio))


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=10, phrase_time_limit=5)

    try:
        print("Recognizing...")
        print(f"User said: {r.recognize_google(audio, language='en-in')}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return r.recognize_google(audio, language='en-in')


def say(text):
    subprocess.call(['say', text])


say("Helloo")


def sendEmail(to, content):
    server = smtplib.SMTP('01devinsh@gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('parigarg211@gmail.com', 'Engineers@946')
    server.sendmail('parigarg211@gmail.com', to, content)
    server.close()


def wishMe():
    hour = datetime.datetime.now().hour

    if hour >= 0 and hour < 12:

        say("Good Morning")

    elif hour >= 12 and hour < 18:

        say("Good Afternoon")

    else:

        say("Good Evening")


def date():
    now = datetime.datetime.now()
    month_name = now.month
    day_name = now.day
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                   'November', 'December']
    ordinalnames = ['1st', '2nd', '3rd', ' 4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th',
                    '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd', '24rd', '25th',
                    '26th', '27th', '28th', '29th', '30th', '31st']

    say("Today is " + month_names[month_name - 1] + " " + ordinalnames[day_name - 1] + '.')


def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"

    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["Notes.exe", file_name])


if __name__ == '__main__':
    wishMe()

    while True:

        audios = r.recognize_google(audio).lower()
        if 'open safari' in audios:
            say("try to use the thing which you dont have........i mean mind")
            d = '/Applications'
            apps = list(map(lambda x: x.split('.app')[0], os.listdir(d)))

            app = 'Safari'
            os.system('open ' + d + '/%s.app' % app.replace(' ', '\ '))

            d = '/Applications'
            records = []
            apps = os.listdir(d)
            for app in apps:
                record = {}
                record['voice_command'] = 'open ' + app.split('.app')[0]
                record['sys_command'] = 'open ' + d + '/%s' % app.replace(' ', '\ ')
                records.append(record)
        elif 'your age' in audios:
            say("i am Younger than You but STILL SMARTER")
        elif 'open opera' in audios:
            say("search wisely its not a private tab")
            d = '/Applications'
            apps = list(map(lambda x: x.split('.app')[0], os.listdir(d)))

            app = 'Opera GX'
            os.system('open ' + d + '/%s.app' % app.replace(' ', '\ '))

            d = '/Applications'
            records = []
            apps = os.listdir(d)
            for app in apps:
                record = {}
                record['voice_command'] = 'open ' + app.split('.app')[0]
                record['sys_command'] = 'open ' + d + '/%s' % app.replace(' ', '\ ')
                records.append(record)
        elif 'open whatsapp' in audios:
            say("Opening Your chit chat aoo..by the way i know your so many secret")
            d = '/Applications'
            apps = list(map(lambda x: x.split('.app')[0], os.listdir(d)))

            app = 'WhatsApp'
            os.system('open ' + d + '/%s.app' % app.replace(' ', '\ '))

            d = '/Applications'
            records = []
            apps = os.listdir(d)
            for app in apps:
                record = {}
                record['voice_command'] = 'open ' + app.split('.app')[0]
                record['sys_command'] = 'open ' + d + '/%s' % app.replace(' ', '\ ')
                records.append(record)
        elif 'time' in audios:
            extract_var = "%I%M%p"
            say("Time is :")
            time = datetime.datetime.now().strftime(extract_var)
            say(time)
        elif "open youtube" in audios:
            say("taking you to youtbe")
            webbrowser.open("https://www.youtube.com")
        elif "open google" in audios:
            say("Sir what should i search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif "joke" in audios:
            say("you are so beautiful...haha i am just kidding")
            joke1 = pyjokes.get_joke(language="en", category="neutral")
            print(joke1)
            say(joke1)
        elif "bye bye" in audios:
            say("THANK YOU FOR VISIT")
        elif "who is" in audios:
            say("searching weikipedia")
            person = r.recognize_google(audio).replace('who is', '')
            info = wikipedia.summary(person, sentences=2)
            say("According to wikipedia")
            print(info)
            say(info)
        elif "hlo" in audios:
            wishMe()
        elif "day today" in audios:
            now = datetime.datetime.now()
            month_name = now.month
            day_name = now.day
            month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
                           'October', 'November', 'December']
            ordinalnames = ['1st', '2nd', '3rd', ' 4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th',
                            '13th', '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd',
                            '24rd', '25th', '26th', '27th', '28th', '29th', '30th', '31st']
            say("Today is " + month_names[month_name - 1] + " " + ordinalnames[day_name - 1] + '.')
        elif 'who are you' in audios or 'what can you do' in audios:
            say('I am ' + name_assistant + ' your personal assistant. I am programmed to minor tasks like opening youtube, google chrome, gmail and search wikipedia etcetra')

        elif 'who is' in audios or 'how' in audios:

            try:
                say('Searching Wikipedia...')
                statement = r.recognize_google(audio).replace("wikipedia", "")
                results = wikipedia.summary(statement, sentences=3)
                say("According to Wikipedia")
                wikipedia_screen(results)
            except:
                say("Error")

        elif 'news' in audios:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/city/mangalore")
            say('Here are some headlines from the Times of India, Happy reading')


        elif 'cricket' in audios:
            news = webbrowser.open_new_tab("cricbuzz.com")
            say('This is live news from cricbuzz')


        elif 'corona' in audios:
            news = webbrowser.open_new_tab("https://www.worldometers.info/coronavirus/")
            say('Here are the latest covid-19 numbers')
        elif "who made you" in audios or "who created you" in audios or "who discovered you" in audios:
            say("I was built by Devinsh & Partima")
            say(results)
        elif 'make a note' in audios:
            statement = r.recognize_google(audio).replace("make a note", "")
            note(statement)


        elif 'note this' in audios:
            statement = r.recognize_google(audio).lower().replace("note this", "")
            note(statement)

        elif 'open prime video' in audios:
            webbrowser.open_new_tab("primevideo.com")
            speak("Amazon Prime Video open now")
            time.sleep(5)
        elif 'open comand' in audios:
            os.system("start cmd")
        elif "open camera" in audios:
            cap = cv2.VideoCapture(0)
            say("don't be afraid it's you")
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break;
            cap.release()
            cv2.destroyAllWindows()
        elif "IP adress" in audios:
            ip = get('https://www.ipify.org').text
            say("your ip adress is{ip}")
            print(ip)

        elif "open facebook" in audios:
            webbrowser.open("https://www.facebook.com/")
        elif 'send email' in audios:
            try:
                say("What should I say?")
                content = takeCommand()
                say("whome should i send")
                to = "01devinsh@gmail.com"
                sendEmail(to, content)
                say("Email has been sent !")
            except Exception as e:
                print(e)
                say("I am not able to send this email")
        elif "send message" in audios:
            pywhatkit.sendwhatmsg("+918146608331", "just testing my voice assistant", 00, 55)
        elif "Play song" in audios:
            a = 'opening  google'
            say(a)
            pywhatkit.playonyt(audios)

        elif "calculate" in audios:

            app_id = "Wolframalpha api id"
            client = wolframalpha.Client(app_id)
            indx = audios.split().index('calculate')
            gle = audios.split()[indx + 1:]
            res = client.gle(' '.join(gle))
            answer = next(res.results).text
            print("The answer is " + answer)
            say("The answer is " + answer)

        elif 'search' in audios or 'play' in audios:

            query = r.recognize_google(audio).lower().replace("search", "")
            query = r.recognize_google(audio).replace("play", "")
            webbrowser.open(query)
        elif 'lock window' in audios:
            say("locking the device")
            ctypes.windll.user32.LockWorkStation()
        elif 'shutdown system' in audios:
            say("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')
        elif "don't listen" in audios or "stop listening" in audios:
            say("for how much time you want to stop jarvis from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)
        elif "i love you" in audios:
            say("It's hard to understand")
        elif "you be my gf" in audios or "you be my bf" in audios:
            say("I'm in relation with your ex")
        elif "Good Morning" in audios:
            say("A warm" + r.recognize_google(audio).lower())
            say("How are you Mister")
            say(assname)
        elif "weather" in audios:

            # Google Open weather website
            # to get API of Open weather
            api_key = "Api key"
            base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
            say(" City name ")
            print("City name : ")
            city_name = takeCommand()
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name
            response = requests.get(complete_url)
            x = response.json()

            if x["code"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in kelvin unit) = " + str(
                    current_temperature) + "\n atmospheric pressure (in hPa unit) =" + str(
                    current_pressure) + "\n humidity (in percentage) = " + str(
                    current_humidiy) + "\n description = " + str(weather_description))

            else:
                say(" City Not Found ")


        elif "Don't have any other work" in audios:
            say("thank you, take care")
            sys.exit()
        elif "where i am" in audios or "my location" in audios:
            say("wait.....let me check")
            try:
                ipAdd = requests.get("https://api.ipify.org").text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip' + ipAdd + '.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city = geo_data['city']
                country = geo_data['country']
                say(f"sir i am not sure but may be we are in city {city} and in country {country}")
            except Exception as e:
                say("sorry sir dew to network issue : i am unable to find your location")
                pass
        break
        say("sir do you have any other work")
