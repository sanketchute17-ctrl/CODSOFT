import pyttsx3
import webbrowser
import wikipedia
import datetime

engine = pyttsx3.init()

engine.setProperty("rate",170)

def speak(text):

    engine.say(text)

    engine.runAndWait()


def process_command(command):

    command=command.lower()

    if "hello" in command:

        response="Hello Sanket. How can I help you?"

    elif "time" in command:

        response="The time is "+datetime.datetime.now().strftime("%H:%M")

    elif "open youtube" in command:

        response="Opening YouTube"

        webbrowser.open("https://youtube.com")

    elif "open google" in command:

        response="Opening Google"

        webbrowser.open("https://google.com")

    elif "search" in command:

        query=command.replace("search","")

        response="Searching "+query

        webbrowser.open("https://google.com/search?q="+query)

    else:

        try:

            response=wikipedia.summary(command,2)

        except:

            response="Sorry I do not know that yet"

    speak(response)

    return response