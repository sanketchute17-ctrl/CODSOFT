import customtkinter as ctk
from PIL import Image, ImageTk
import speech_recognition as sr
import threading
import time
from brain import process_command

ctk.set_appearance_mode("light")


def start_gui():

    app = ctk.CTk()
    app.geometry("900x650")
    app.title("MOCHI AI")

    title = ctk.CTkLabel(app,text="MOCHI AI",font=("Impact",45))
    title.pack(pady=20)

    # ---------- ROBOT GIF ----------

    gif = Image.open("robot.gif")

    frames=[]

    try:
        while True:
            frame = gif.copy()
            frames.append(ImageTk.PhotoImage(frame))
            gif.seek(len(frames))
    except:
        pass

    robot = ctk.CTkLabel(app,text="")
    robot.pack(pady=20)

    def animate(index):
        robot.configure(image=frames[index])
        app.after(100,animate,(index+1)%len(frames))

    animate(0)

    # ---------- CHAT ----------

    chat = ctk.CTkTextbox(app,width=700,height=300,font=("Arial Black",16))
    chat.pack(pady=20)

    # ---------- LISTEN ----------

    def listen():

        r = sr.Recognizer()

        try:
            with sr.Microphone() as source:

                r.adjust_for_ambient_noise(source, duration=0.1)

                audio = r.listen(source, timeout=2, phrase_time_limit=2)

            text = r.recognize_google(audio)

            return text.lower()

        except:
            return ""

    # ---------- AI LOOP ----------

    def assistant():

        chat.insert("end","Mochi: Hello Sanket. I am Mochi AI assistant\n")

        while True:

            command = listen()

            if command!="":

                chat.insert("end","You: "+command+"\n")

                response = process_command(command)

                chat.insert("end","Mochi: "+response+"\n")

                chat.see("end")

            time.sleep(0.01)

    threading.Thread(target=assistant,daemon=True).start()

    app.mainloop()
