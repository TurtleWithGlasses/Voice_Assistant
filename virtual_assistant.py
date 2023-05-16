import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

# hear the microphone and return the audio as text

def transform_audio_into_text():

    # store recognizer in variable
    r = sr.Recognizer()

    # set microphone

    with sr.Microphone() as source:
        # waiting time
        r.pause_threshold = 0.8

        # report that recording has begun
        print("You can speak now")

        # save what you hear as audio

        audio = r.listen(source)

        try:
            # search on google
            request = r.recognize_google(audio, language="en-us")

            # test in text
            print("You said " + request)
            return request

        # in case it doesn't understand'
        except sr.UnknownValueError:
            print("Sorry, there is no service")
            return "I am still waiting"

        # in case the request cannot be resolved
        except sr.RequestError:
            print("Sorry, I cannot understand")
            return "I am still waiting"

        # unexpected error
        except:
            print("Sorry, something went wrong")
            return "I am still waiting"

# function so the assistant can be heard

def speak(message):

    # start engine of pyttsx3
    engine = pyttsx3.init()

    # deliver message
    engine.say(message)
    engine.runAndWait()

# inform the day of the week
def ask_day():

    # variable with today information
    day = datetime.date.today()
    print(day)

    # variable for day of the week
    week_day = day.weekday()
    print(week_day)

    # names of days
    calender = {0: "Monday",
                1: "Tuesday",
                2: "Wednesday",
                3: "Thursday",
                4: "Friday",
                5: "Saturday",
                6: "Sunday"}

    # say the day of the week

    speak(f"Today is {calender[week_day]}.")


# Inform what time it is

def ask_time():

    # variable with time information

    time = datetime.datetime.now()
    time = f"At this moment it is {time.hour} hours and {time.minute} minutes."
    print(time)

    # say the time

    speak(time)

# create greeting

def initial_greeting():

    # say greeting
    speak("Hello, I am Kelly. How can I help you?")

# main function of the assistant
def my_assistant():

    # active the greeting
    initial_greeting()

    # cut-off variable
    go_on = True

    # main loop
    while go_on:
        # activate the microphone
        my_request = transform_audio_into_text().lower()
        if "open youtube" in my_request:
            speak("Sure, I'm opening youtube")
            webbrowser.open("https://www.youtube.com")
            continue

        elif "open browser" in my_request:
            speak("Of course. I'm on it.")
            webbrowser.open("https://www.google.com")
            continue

        elif "open facebook" in my_request:
            speak("Of course. I'm on it.")
            webbrowser.open("https://www.facebook.com")
            continue

        elif "open gmail" in my_request:
            speak("Of course. I'm on it.")
            webbrowser.open("https://www.gmail.com")
            continue

        elif "tell me the day" in my_request:
            ask_day()
            continue

        elif "tell me the time" in my_request:
            ask_time()
            continue

        elif "wikipedia" in my_request:
            speak("I am looking for it")
            my_request = my_request.replace("wikipedia", "")
            answer = wikipedia.summary(my_request, sentences=6)
            speak("According to wikipedia: ")
            speak(answer)
            continue

        elif "search the internet for" in my_request:
            speak("Of course.")
            my_request = my_request.replace("search the internet for", "")
            pywhatkit.search(my_request)
            speak("This is what I found.")
            continue

        elif "play" in my_request:
            speak("That's a great idea")
            pywhatkit.playonyt(my_request)
            continue

        elif "joke" in my_request:
            speak(pyjokes.get_joke())
            continue

        elif "stock price" in my_request:
            share = my_request.split()[-2].strip()
            portfolio = {"apple": "APPL",
                         "amazon": "AMZN",
                         "google": "GOOGL"}
            try:
                searched_stock = portfolio[share]
                searched_stock = yf.Ticker(searched_stock)
                price = searched_stock.info["regularMarketPrice"]
                speak(f"I found it. The price of {share} is {price}.")
                continue
            except:
                speak("I am sorry, but I didn't find it.")
                continue

        elif "exit" in my_request:
            speak("See you next time.")
            break

my_assistant()