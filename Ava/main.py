import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
from keyboard import press_and_release, write
import random
from time import sleep
engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def gapnitushunish():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        print("tekshiryabman...")
        javob = r.recognize_google(audio, language="eng")
        print(f"User said: {javob}")
        return javob
    except Exception as e:
        return "none"
    return javob
    

def sendEmile(to,xabar):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your emile id', 'your pasword')
    server.sendmail('your emile id', to, xabar)
    server.close

def salomlashuv():
        soat = datetime.datetime.now().hour
        if soat>=0 and soat<=12:
            speak("Good morning sir!")
        elif soat>=12 and soat<=18:
            speak("Good afternoon sir!")
        else:
            speak("Good evning sir!")
        speak('I am Ava sir your assistent how i can help you')

def all():
    while True:
        buyruq = gapnitushunish().lower()
        ism = "Ava"
        if "open notepad" in buyruq:
            path = ('C:\\Windows\\system32\\notepad.exe')
            os.startfile(path)
            speak("The notebook was opened at your command")
        elif "Hello" in buyruq or "hi" in buyruq:
            speak(f"Hello sir, i can help you")
        elif "camera" in buyruq:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()
        elif "my ip" in buyruq:
            ip = get("https://api.ipify.org").text
            speak(f"Your ip addres {ip}")

        elif "wikipediya" in buyruq:
            speak("I am serching wikipedia...")
            sorov = buyruq.replace('wikipedia', "")
            result = wikipedia.summary(sorov, sentences=2)
            speak('wikipediadan topildi')
            speak(result)
            print(result)
        elif "sleep now" in buyruq:
            speak("I am happy to serve you")
            break
            
        
        elif "YouTube" in buyruq:
            webbrowser.open("www.youtube.com")
            speak("buyrug'ingizga binoan youtube ochildi")
        
        elif "facebook" in buyruq:
            webbrowser.open("https://www.facebook.com/")
            speak("buyrug'ingizga binoan facebok ochildi")

        elif "instagram" in buyruq:
            webbrowser.open("https://www.instagram.com/")
            speak("buyrug'ingizga binoan instagram ochildi")
        
        elif "google" in buyruq:
            speak("Yahshi janob googledan nimani qidiramiz")
            cm = gapnitushunish().lower()
            webbrowser.open(f"{cm}")
        
        elif "send" in buyruq:
            kit.sendwhatmsg("+998909885351", "Salom men avaman",2,25)

        elif "music" in buyruq:
            kit.playonyt("headlight")
        
        elif "emile" in buyruq:
            try:
                speak("Nima deb jonatay")
                xabar = gapnitushunish().lower()
                to = "abubakirqorahojayev@gmail.com"
                sendEmile(to,xabar)
                speak("jonatildi")
            except Exception as e:
                print(e)
                speak('Kechirasiz bunday emile mavjud emas yoki xato kiritilgan!!')
        elif "how are you" in buyruq:
            speak("I am fine sir. how are you Today?")

        elif "i am fine" in buyruq:
            speak("I am glad to hear that")

        
        elif "thank you" in buyruq:
            speak("You are welcome")
        
        elif "what are you doing"in buyruq:
            speak("I await your order sir")
        
        elif "jarvis" in buyruq:
            speak('Yes sir i am here')
        
        elif "what tasks do we have today" in buyruq:
            speak("There are no assignments for today, sir.")
            speak("Do you have an assignment?")
         
        elif "i have a headache" in buyruq:
            headache_tablets = ["aspirin", "excerdin", "sinepar", "trimol", "bolnol"]
            rT = random.choice(headache_tablets)
            speak("Your headache is not severe or very severe")
            bosh = gapnitushunish()
            if "severe" in bosh:
                speak(f"I recommend {rT} medicine to you")
            else:
                speak("It is a little difficult for me to diagnose this type of disease, please see a doctor")
        
        elif "close notepad" in buyruq:
            os.system("taskkill /f /im notepad.exe")
            speak("notepad closed as per your command")
        
        elif "coding" in buyruq:
            speak("Do you want to open a new window or continue what you did yesterday?")
            code = gapnitushunish()
            if "window" in code:

                speak("Ok sir this is your new workstation")
                path = ('C:\\Users\\Komol\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk')
                os.startfile(path)
                sleep(7)
                press_and_release("Ctrl + Shift + n")
                sleep(7)
                press_and_release("f11")
                sleep(6)
                press_and_release("Ctrl + alt + left windows + n")
                sleep(3)
                press_and_release("down arrow")
                sleep(3)
                press_and_release("enter")
                sleep(3)
                press_and_release("Ctrl + s")

                speak("whatever the file name is")
                fN = gapnitushunish()
                if fN:
                    write(fN)
                    sleep(3)
                    press_and_release("enter")
            
            else:
                speak("Ok sir")
                path = ('C:\\Users\\Komol\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk')
                os.startfile(path)

                
            

            
        elif "alarm" in buyruq:
            speak("Sir, exactly what time should I set the alarm. for example tell me at 5:30 AM")
            tt = gapnitushunish()
            tt = tt.replace("set alarm to", "")
            tt = tt.replace(".","")
            tt = tt.upper()  
            import Alarm
            Alarm.alarm(tt)





if __name__ == "__main__":
    salomlashuv()
    all()
    while True:
        permisson = gapnitushunish()
        if "wake up" in permisson:
            all()
        elif "bye" in permisson:
            speak("Thanks for using me")
            sys.exit()
         
        
