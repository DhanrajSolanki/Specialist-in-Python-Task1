import pyttsx3

import speech_recognition as sr

import os

import webbrowser

import time

import getpass


count=0
while count<2:
 
 print()
 pyttsx3.speak("For Using this program you have to tell your Password first")
 print("REMEMBER.....")
 print()
 print("\t You Have Only 2 Chances to write a correct password")
 print()
 print("\t For Using this program you have to tell your Password: ")
 print() 
 inpass='lw'

 apass=getpass.getpass("Enter your Password: ")

 
 if inpass==apass:
  pyttsx3.speak("You Entered Correct Password")
  print()
  pyttsx3.speak("Here is the Menu For this Program what can you do")
  print("Here is the Menu For this Program what can you do")
  print()
  print("\t - You can open chrome")
  print()
  print("\t - Browsering")
  print()
  print("\t - You can open Notepad")
  print()
  print("\t - You can open code writer")
  print()
  print("\t - You can access your LinkedIn and Github")
  print()
  print("\t - You can show date and time")
  print()
  print("\t - A lot's more stuff")

  pyttsx3.speak("Hello Everyone i am John what can i do for you")
  print("Hello Everyone i am John what can i do for you")
  r=sr.Recognizer()
  while True:
   with sr.Microphone() as source:
    print()
    print("Listening....")
    audio=r.listen(source)
    print("Done....")
   text=r.recognize_google(audio)
   print(text)

   if(("run" in text) or ("open" in text) or ("execute" in text)) and (("Notepad" in text) or ("text editor" in text)):
    pyttsx3.speak("Opening Notepad")
    os.system("notepad")
    time.sleep(5)
   elif(("show" in text) or ("display" in text) or ("open" in text)) and (("date" in text) or ("time" in text)):
    pyttsx3.speak("Showing today's Date")
    os.system("date")
    time.sleep(3)
   elif(("open" in text) or ("go to" in text)) and (("a w s" in text) or ("cloud" in text)):
    pyttsx3.speak("Going to AWS Login Page")
    webbrowser.open("https://aws.amazon.com/console/")
    time.sleep(10)
   elif (("run" in text) or ("execute" in text) or ("show" in text) or ("what's" in text)) and (("time" in text)):
    pyttsx3.speak("Showing time")
    os.system("time")
    time.sleep(5)
   elif(("run" in text) or ("open" in text) or ("execute" in text)) and (("code" in text) or ("Visual Studio" in text) or ("Code Writer" in text)):
    pyttsx3.speak("Opening Visual Studio for you")
    os.system("code")
    time.sleep(10)
   elif (("run" in text) or ("execute" in text) or ("open" in text)) and (("zoom" in text) or ("meeting" in text)):
    pyttsx3.speak("Opning Zoom Meeting For u")
    os.system("zoom")
    time.sleep(7)
   elif(("run" in text) or ("open" in text) or ("execute" in text)) and (("Chrome" in text) or ("browser" in text)):
    pyttsx3.speak("Opening Chrome for you")
    os.system("chrome")
    time.sleep(5)
   elif (("run" in text) or ("execute" in text) or ("open" in text)) and (("Telegram" in text)):
    pyttsx3.speak("Opning Telegram")
    os.system("telegram")
    time.sleep(10)
   elif(("run" in text) or ("open" in text) or ("execute" in text)) and (("VM" in text) or ("virtualbox" in text) or ("virtualization" in text)):
    pyttsx3.speak("Opening Virtualbox for you")
    os.system("virtualbox")
    time.sleep(10)
   elif(("open" in text) or ("go to" in text)) and (("LinkedIn" in text) or ("account" in text)):
    pyttsx3.speak("Going to Your Linkdin account")
    webbrowser.open("https://www.linkedin.com/in/solanki-dhanrajsinh-856232192/")
    time.sleep(20)
   elif(("open" in text) or ("goto" in text)) and (("repository" in text) or ("github" in text)):
    pyttsx3.speak("Going to Your Github Repository")
    webbrowser.open("https://github.com/")
    time.sleep(20)
   elif(("open" in text) or ("go to" in text)) and (("Google map" in text) or ("Map" in text)):
    pyttsx3.speak("Opening Google Map For you")
    webbrowser.open("https://www.google.com/maps/")
    time.sleep(20)
   elif(("show" in text) or ("display" in text) or ("what's" in text) or ("today" in text) or ("today's" in text)) and (("weather" in text) or ("temperature" in text)):
    pyttsx3.speak("Showing Weather Update For you")
    webbrowser.open("https://www.google.com/search?rlz=1C1CHBF_enIN855IN855&sxsrf=ALeKk03WZBj3-JcefRbAhAX6Hsd9xZRXog%3A1600236517285&ei=5athX_KLEY6F4-EPg72xkAY&q=weather+today+at+my+location&oq=weather+todays&gs_lcp=CgZwc3ktYWIQARgAMgQIABBHMgQIABBHMgQIABBHMgQIABBHMgQIABBHMgQIABBHMgQIABBHMgQIABBHUABYAGDacmgAcAJ4AIABAIgBAJIBAJgBAKoBB2d3cy13aXrIAQjAAQE&sclient=psy-ab")
    time.sleep(20)
   elif(("show" in text) or ("display" in text) or ("what's" in text) or ("today" in text) or ("today's" in text)) and (("News" in text) or ("news" in text)):
    pyttsx3.speak("Showing News Update For you")
    webbrowser.open("https://www.hindustantimes.com/")
    time.sleep(20)
   elif(("play" in text) or ("goto" in text) or ("audio" in text)) and (("music" in text) or ("Music" in text) or ("songs" in text) or ("song" in text)):
    pyttsx3.speak("Showing online music from saavn")
    webbrowser.open("https://www.jiosaavn.com/")
    time.sleep(20)
   elif ("exit" in text) or ("terminate" in text) or ("bye" in text):
    pyttsx3.speak("Thank you for using me")
    break
   else:
    pyttsx3.speak("Whatever You Asking is not in my list")
    print()
    print("\t TRY AGAIN!!")

 elif ("exit" in text) or ("terminate" in text) or ("bye" in text):
    pyttsx3.speak("Thank you for using me")
    break
 else:
  pyttsx3.speak("\t You Entered Wrong Password Sorry TRY AGAIN")
  count=count+1
  print()
  print("\t You have entered wrong password {} time and you have only {} are left to entered right password".format(count,2-count))
  pyttsx3.speak("\t You have entered wrong password {} time and you have only {} are left to entered right password".format(count,2-count))
  if count==2:
    print()
    print("You have Entered Wrong Password All time Authentication Failed")
    pyttsx3.speak("You have Entered Wrong Password All time Authentication Failed")
    break
  
  
   
 

 