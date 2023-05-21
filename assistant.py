#!/usr/bin/python3
# -*- coding: utf-8 -*-

from currency_functions import archivise_currency_course, currency_course, calculator, archivise_golden_price, \
    currency_avability
from xml_files import gold_price_dic

end = None
import pyttsx3 as tts
import speech_recognition as sr


################################################################################

def main():
    TTS = tts.init()
    TTS.setProperty('volume', 0.7)
    TTS.setProperty('rate', 190)

    STT = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
            print('---------------------------------------------------------------------------------------------------------------------------------------------')
            menu_list = ["Pokaż dostępne waluty", "Aktualny kurs walut", "Zamiana waluty na złotówki", "Aktualna cena złota", "Archiwalany kurs walut",
                         "Archiwalna cena złota"]
            print(menu_list)
            print('---------------------------------------------------------------------------------------------------------------------------------------------')
            TTS.say("Wybierz z listy co chcesz zrobić")
            TTS.runAndWait()
            audio = STT.listen(source)
            try:
                tekst = STT.recognize_google(audio, language='pl_PL')
                print(tekst)
                if tekst == 'koniec':
                    break
                elif tekst.lower() in ["sprawdić kurs walut", "kurs walut"]:
                    currency_course()
                elif tekst.lower() in ["pokaż dostępne waluty", "dostępne waluty"]:
                    currency_avability()
                elif tekst.lower() in ["zamiana waluty na złotówki", "zamień walutę", "kalkulator", "kalkulator walut"]:
                    calculator()
                elif tekst.lower() in ["cena złota", "złoto", "zaktualna cena złota"]:
                    TTS.say("W dniu dzisiejszym cena złota wynosi {p}".format(p=gold_price_dic['#text']))
                    TTS.runAndWait()
                elif tekst.lower() in ["archiwalna cena złota", "archiwum złoto", "cena złota archiwum"]:
                    archivise_golden_price()
                elif tekst.lower() in ["sprawdić archiwalny kurs walut", "archiwalny kurs walut", "archiwum waluty"]:
                    archivise_currency_course()
            except sr.UnknownValueError:
                print('nie rozumiem')
            except sr.RequestError as e:
                print('error:', e)


main()

################################################################################
