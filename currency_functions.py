import requests
import xmltodict

from assistant_functions import assistant_archive_currency, assistant_value, assistant_convert_currency, \
    assistant_archive_gold
import pyttsx3 as tts
import speech_recognition as sr


def calculator():
    TTS = tts.init()
    TTS.setProperty('volume', 0.7)
    TTS.setProperty('rate', 190)

    STT = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            try:
                TTS.say("Wybierz walutę")
                TTS.runAndWait()
                audio = STT.listen(source)
                tekst1 = STT.recognize_google(audio, language='pl_PL')
                print(tekst1)
                if tekst1 == "koniec":
                    break
                TTS.say("Podaj kwotę")
                TTS.runAndWait()
                audio = STT.listen(source)
                money = STT.recognize_google(audio, language='pl_PL')
                print(money)
                odp = assistant_convert_currency(tekst1, money)
                TTS.say(odp)
                TTS.runAndWait()
            except sr.UnknownValueError:
                TTS.say("Nie rozumiem, powtórz wszystko jeszcze raz")
                TTS.runAndWait()
            except sr.RequestError as e:
                print('error:', e)


def currency_course():
    TTS = tts.init()
    TTS.setProperty('volume', 0.7)
    TTS.setProperty('rate', 190)

    STT = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            TTS.say("Wybierz walutę")
            TTS.runAndWait()
            audio = STT.listen(source)
            tekst3 = STT.recognize_google(audio, language='pl_PL')
            print(tekst3)
            if tekst3 == "koniec":
                break
            odp = assistant_value(tekst3)
            TTS.say(odp)
            TTS.runAndWait()

def currency_avability():
    currency_table_xml = requests.get("https://www.nbp.pl/kursy/xml/a014z230120.xml")
    currency_table_xml.encoding = 'ISO-8859-2'
    currency_dic = xmltodict.parse(currency_table_xml.text)['tabela_kursow']['pozycja']
    for k in currency_dic:
        print(k['nazwa_waluty'])

def archivise_currency_course():
    TTS = tts.init()
    TTS.setProperty('volume', 0.7)
    TTS.setProperty('rate', 190)

    STT = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            TTS.say("Wybierz walutę")
            TTS.runAndWait()
            audio = STT.listen(source)
            tekst3 = STT.recognize_google(audio, language='pl_PL')
            print(tekst3)
            if tekst3 == "koniec":
                break
            TTS.say("Podaj datę")
            TTS.runAndWait()
            audio = STT.listen(source)
            date = STT.recognize_google(audio, language='pl_PL')
            odp = assistant_archive_currency(tekst3, date)
            TTS.say(odp)
            TTS.runAndWait()


def archivise_golden_price():
    TTS = tts.init()
    TTS.setProperty('volume', 0.7)
    TTS.setProperty('rate', 190)

    STT = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            TTS.say("Podaj datę")
            TTS.runAndWait()
            audio = STT.listen(source)
            date = STT.recognize_google(audio, language='pl_PL')
            print(date)
            odp = assistant_archive_gold(date)
            TTS.say(odp)
            TTS.runAndWait()
