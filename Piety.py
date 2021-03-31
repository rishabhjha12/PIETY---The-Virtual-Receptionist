import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 50)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("My Name Is Piety Sir. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('rjhha1097@gmail.com', 'melebabunethanathaya')
    server.sendmail('yashkhattar753@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")
            print("user said to open youtube")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com/")
            print("user said to open google")
        elif 'facebook' in query:
            webbrowser.open("https://www.facebook.com/")
            print("user said to open facebook")
        elif 'music' in query:
            webbrowser.open("https://www.youtube.com/watch?v=K9w6UBZOn5o")
            print("user said to play music")




        elif 'college' in query:

            speak(
                "Who says success doesn't have a name, it do have one it's Panipat institute of engineering and technology")
            webbrowser.open("https://www.youtube.com/watch?v=6qqpCcvBEhk")
            webbrowser.open("piet.co.in")

        elif 'whatsapp' in query:
            webbrowser.open("https://www.web.whatsapp.com")



        elif 'courses' in query:
            # webbrowser.open("https://www.youtube.com/watch?v=PHUG8lCrTRs")
            speak("We have everything that you dream off")
        elif 'contact' in query:
            speak(f" Mr. Rishabh Jha can be contacted at 7368962920")
            print (f"Mr. Rishabh Jha can be contacted at 7368962920")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            print(f"Sir, the time is {strTime}")

        elif 'can you' in query:
            speak(f"Except finding a girlfriend for a ugly person like you , i can do everything")

        elif 'what is the location' in query:
            speak(
                f"Panipat institute of engineering and technology is situated at NH 44, pattikalyana VPO, panipat district, haryana india")
        elif 'courses' in query:
            speak(
                f"we have Bachelor's of technology in computer science engineering, Information Technology, Mechanical Engineering,"
                f" Civil Engineering, Textile engineering and Electronics and Communication Engineering"
                f"Apart from that we offer Bachelor's of computer application, Master's of computer application, Bachelors of Business Administration and Master's of business Administration' ")
        elif 'ragging' in query:
            webbrowser.open("https://www.piet.co.in/academics/discipline/anti-ragging-rules/")
        elif 'library' in query:
            webbrowser.open("https://www.piet.co.in/academics/central-library/")


        elif 'location' in query:
            webbrowser.open(
                "https://www.google.com/maps/dir//P.I.E.T+-+Panipat+Institute+of+Engineering+%26+Technology,+70+Milestone,+Grand+Trunk+Rd,+Samalkha,+Haryana+132102/@29.2129166,77.0183464,14z/data=!4m16!1m6!3m5!1s0x0:0x9154ba66a1839189!2sP.I.E.T+-+Panipat+Institute+of+Engineering+%26+Technology!8m2!3d29.2110625!4d77.0164581!4m8!1m0!1m5!1m1!1s0x390dc89b535e9757:0x9154ba66a1839189!2m2!1d77.0164581!2d29.2110625!3e2")
            speak(
                f"Here is the location of PIET, Click on go in the left handside of your screen to get the exact direction from your location.")
        elif 'school ' in query:
            webbrowser.open("https://www.youtube.com/watch?v=DBcfxJYPglI")
            webbrowser.open("pietsanskriti.com")
        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "yashkhattar753@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend . I am not able to send this email")
