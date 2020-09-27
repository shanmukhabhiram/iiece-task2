import speech_recognition as sr
import pyttsx3
import webbrowser
'''engine=pyttsx3.init()
engine.say("hello sir")
engine.runAndWait()
print("hello sir")
r1=sr.Recognizer()
r1.energy_threshold=10000

with sr.Microphone() as source:
    engine.say("what do you want me to run sir")
    engine.runAndWait()
    print("what do you want me to run sir")
    audio=r1.listen(source)
data=r1.recognize_google(audio)
data=data.lower()
print(data)'''
r=''
data=input()
if  'calendar' in data:
    r='cal'
elif 'weather' in data:
    webbrowser.open("https://www.msn.com/en-in/weather")
    exit()
elif 'ifconfig' in data:
    r='ifconfig'
elif 'date' in data:
    r='date'
elif 'files' in data:
    r='ls'
elif 'commands' in data:
    r='compgen -c'
else:
    print(r)
    exit()
c='http://192.168.43.178/cgi-bin/hello.py?n={0}'.format(r)
webbrowser.open(c)

