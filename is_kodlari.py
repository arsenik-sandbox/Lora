from datetime import datetime
import datetime
from email import message
from email.mime import audio
from logging import shutdown
from pickle import FALSE
from pyexpat.errors import messages
import smtplib
from neuralintents import GenericAssistant
import speech_recognition
import pyttsx3 as tts
import win32com.client
import sys
import wikipedia
import webbrowser
import pyautogui
import locale
import pyowm
import os
import time
import winsound
from tkinter import *
import ctypes
import subprocess




locale.setlocale(locale.LC_ALL, 'tr_TR')
recognizer = speech_recognition.Recognizer()


speaker = tts.init()
speaker.setProperty('rate', 150)
speaker.setProperty('voice', '0x041f')





todo_list = []


def not_olustur():
    global recognizer

    speaker.say("Neyi not etmek istersin?")
    speaker.runAndWait()

    done = False

    while not done:
        try:

            with speech_recognition.Microphone() as mic:

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                note = recognizer.recognize_google(audio)
                note = note.lower()

                speaker.say("Bir dosya adı seçin")
                speaker.runAndWait()
                
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                filename = recognizer.recognize_google(audio)
                filename = filename.lower()

            with open(filename, 'w') as f:
                f.write(note)
                done = True
                speaker.say("Not başarıyla oluşturuldu{filename}")
                speaker.runAndWait()


        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("Anlayamadım")
            speaker.runAndWait()

def todo_ekle():
    global recognizer

    speaker.say("Yapacaklar listene ne eklemek istersin?")
    speaker.runAndWait()

    done = False 

    while not done:
        try:

            with speech_recognition.Microphone() as mic:

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                item = recognizer.recognize_google(audio)
                item = item.lower()

                todo_list.append(item)
                done = True

                speaker.say("{item} yapılacaklar listene başarıyla eklendi")
                speaker.runAndWait()

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("Anlayamadım")
            speaker.runAndWait()

def todo_listele():
    speaker.say("Yapılacaklar listesindeki şeyler şu şekilde")

    for item in todo_list:
        speaker.say(item)
    speaker.runAndWait()

def selamlama():
    speaker.say("Merhaba, sana nasıl yardımcı olabilirim?")
    speaker.runAndWait()

def vedalasma():
    speaker.say("Görüşürüz")
    speaker.runAndWait()
    sys.exit(0)


def saat_kac():
    speaker.say("Şuan saat"(datetime.now().strftime('%H:%M:%S')))
    speaker.runAndWait()

def wikide_arat():

    global recognizer

    speaker.say("Wikipedia'da ne aratmak istersin?")
    speaker.runAndWait()

    done = False 

    while not done:
        try:

            with speech_recognition.Microphone() as mic:

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                wiki = recognizer.recognize_google(audio)
                wiki = wiki.lower()
                results = wikipedia.summary(sentences = 3)
                done = True

                speaker.say("{wiki} için wikipedia'da bulduklarım:")
                speaker.say(results)
                speaker.runAndWait()

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("Anlayamadım")
            speaker.runAndWait()


def youtube_video_ac():

    global recognizer

    speaker.say("İstediğin video'yu arıyorum")
    speaker.runAndWait()

    done = False 

    while not done:
        try:

            with speech_recognition.Microphone() as mic:

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                videoİsmi = recognizer.recognize_google(audio)
                videoİsmi = videoİsmi.lower()

                adres = ('https://www.youtube.com/results?search_query=')+videoİsmi
                webbrowser.get().open(adres)
                pyautogui.moveTo(x=702, y=252)
                pyautogui.click(button='left', clicks=2, interval=7)                      
             
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("Anlayamadım")
            speaker.runAndWait()

def googleda_arat():

    global recognizer

    speaker.say("İstediğin video'yu arıyorum")
    speaker.runAndWait()

    done = False 

    while not done:
        try:

            with speech_recognition.Microphone() as mic:

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                arama = recognizer.recognize_google(audio)
                arama = arama.lower()

                adres = ('https://www.google.com/search?q=')+arama
                webbrowser.get().open(adres)
                pyautogui.moveTo(x=384, y=368)
                pyautogui.click(button='left',clicks=2,interval=7)  

                speaker.say("{arama} için Google'da bulduklarım")
                speaker.runAndWait()                   
             
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("Anlayamadım")
            speaker.runAndWait()


def twitter_ac():
    
    adres = ('https://www.twitter.com/')
    webbrowser.open_new_tab(adres)

def github_ac():

    adres = ('https://github.com/')
    webbrowser.open_new_tab(adres)

def haftanin_gunu():
    
    gun = datetime.datetime.now()
    speaker.say(datetime.datetime.strftime(gun, '%A'))
    speaker.runAndWait()

def tarih():

    tarih = datetime.datetime.now()
    speaker.say(datetime.datetime.strftime(tarih, '%d %B %Y'))
    speaker.runAndWait()


def hava_durumu():
    global recognizer

    owm = pyowm.OWM("e402c33c5ae91a07f0adc05ef341c1c5")
    mgr = owm.weather_manager()

    speaker.say("Hangi şehir için hava durumu bilgisini görmek istersin?")
    speaker.runAndWait()

    done = False 

    while not done:
        try:

            with speech_recognition.Microphone() as mic:

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                sehir = recognizer.recognize_google(audio)
                sehir = sehir.lower()
                

                gozlem = mgr.weather_at_place("{sehir},TR")
                hava = gozlem.weather

                detayli = hava.get_detailed_status()
                sicaklik = hava.get_temperature('celcius')["temp"]

                speaker.say("{sehir} için hava durumu {detayli} ve {sicaklik} derece.")            
             
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("Anlayamadım")
            speaker.runAndWait()


def mail_olustur():
    global recognizer

    speaker.say("Kime mail göndermek istiyorsun?")
    speaker.runAndWait()

    done = False 

    while not done:
        try:

            with speech_recognition.Microphone() as mic:

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                username = input ("Mail Adresi")
                password = input ("Parola")

                sunucu = smtplib.SMTP('smtp.gmail.com', 587)
                sunucu.ehlo()
                sunucu.starttls()
                sunucu.login("{username}", "{password}")
                to = ["Gönderilecek Mail"]
                mesaj ="Deneme"
                try:
                    sunucu.sendmail(username, to, mesaj)
                    print ("Mail gönderimi başarılı")
                except:
                    print ("Mail gönderimi başarısız")

                sunucu.quit()

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("Anlayamadım")
            speaker.runAndWait()


def mail_oku():

    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    inbox = outlook.GetDefaultFolder(6)
    messages = inbox.Items
    message = messages.GetLast()

    speaker.say("{message.SenderName} kişisinden bir mailin var, mesaj başlığı {message.subject}, mesaj içeriği{message.body}")
    speaker.runAndWait()


def klasor_ac():
    
    speaker.say("Hangi klasörü açmamı istersin?")
    speaker.runAndWait()

    done = False 

    while not done:
        try:

            with speech_recognition.Microphone() as mic:

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                klasor = recognizer.recognize_google(audio)
                klasor = klasor.lower()

                os.system('cd ${klasor}')                
             
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("Anlayamadım")
            speaker.runAndWait()

def klasor_olustur():

    global recognizer

    speaker.say("Klasör nerede olutşturulsun?")
    speaker.runAndWait()

    done = False 

    while not done:
        try:

            with speech_recognition.Microphone() as mic:

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                klasor_yeri = recognizer.recognize_google(audio)
                klasor_yeri = klasor_yeri.lower()

                if klasor_yeri == "buraya" or "burası" or "bu dizin":
                    os.mkdir()

                else:
                    os.makedirs("{klasor_yeri}", mode = 0o755, exist_ok=True)

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("Anlayamadım")
            speaker.runAndWait()

def sistem_kapat():

    speaker.say("Bilgisayarını kapatmak istiyor musun?")
    speaker.runAndWait()

    done = False 

    while not done:
        try:

            with speech_recognition.Microphone() as mic:

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                shutdown = recognizer.recognize_google(audio)
                shutdown = shutdown.lower()

                if shutdown == 'no':
                   exit()
                else:
                    os.system("shutdown /s /t 1")           
             
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("Anlayamadım")
            speaker.runAndWait()
            

def alarm_olustur():

    print("alarm oluşturma modülü")
  
    
def alarm_listele():
    
    print("alarm listeleme modülü")

def antivirus():
    speaker.say("Virüs taramasını başlatıyorum")
    subprocess.Popen('powershell.exe [Start-MpScan')

    

def ekranı_kilitle():

    speaker.say("locking the device")
    ctypes.windll.user32.LockWorkStation()
    


mappings = {

    'selamlama': selamlama,
    'not_olustur': not_olustur,
    'todo_ekle': todo_ekle,
    'todo_listele': todo_listele,
    'vedalasma': vedalasma,
    'saat_kac': saat_kac,
    'wikide_arat': wikide_arat,
    'youtube_video_ac': youtube_video_ac,
    'googleda_arat': googleda_arat,
    'twitter_ac': twitter_ac,
    'github_ac': github_ac,
    'haftanin_gunu': haftanin_gunu,
    'tarih': tarih,
    'hava_durumu': hava_durumu,
    'mail_olustur': mail_olustur,
    'mail_oku': mail_oku,
    'klasor_ac': klasor_ac,
    'klasor_olustur': klasor_olustur,
    'sistem_kapat': sistem_kapat,
    'alarm_olustur': alarm_olustur,
    'alarm_listele': alarm_listele,
    'antivirus': antivirus,
    'ekranı_kilitle': ekranı_kilitle
}  
                




assistant = GenericAssistant('intentGelistir.json', intent_methods=mappings)
assistant.train_model()

while True:
    try:
        with speech_recognition.Microphone() as mic:

            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            message = recognizer.recognize_google(audio)
            message = message.lower()

        assistant.request(message)

    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer()
