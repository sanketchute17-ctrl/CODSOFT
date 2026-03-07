import tkinter as tk
from ai_logic import best_move,check_winner
from PIL import Image,ImageTk
import pyttsx3
import random

engine = pyttsx3.init()

board=[]
buttons=[]
size=3

human_score=0
ai_score=0
draw_score=0


def speak(text):
    engine.say(text)
    engine.runAndWait()


def fireworks():

    colors=["yellow","orange","white"]

    for _ in range(12):

        x=random.randint(100,250)
        y=random.randint(50,150)

        for i in range(10):

            dx=random.randint(-50,50)
            dy=random.randint(-50,50)

            particle=canvas.create_oval(x,y,x+6,y+6,
                                        fill=random.choice(colors),
                                        outline="")

            canvas.move(particle,dx,dy)

        root.update()
        root.after(40)



def reset_board():

    global board

    board=[""]*(size*size)

    for b in buttons:
        b.config(text="",bg="white")



def player_move(i):

    global board

    if board[i]=="":
        board[i]="X"
        buttons[i]["text"]="X"
        buttons[i]["bg"]="#fff176"

        result=check_winner(board)

        if result:
            end_game(result)
            return

        thinking_label.config(text="AI thinking...")
        root.after(700,ai_move)



def ai_move():

    thinking_label.config(text="")

    move=best_move(board)

    if move!=-1:

        board[move]="O"
        buttons[move]["text"]="O"
        buttons[move]["bg"]="#ffd54f"

    result=check_winner(board)

    if result:
        end_game(result)



def end_game(result):

    global human_score,ai_score,draw_score

    if result=="X":

        human_score+=1
        speak("Human wins")
        fireworks()

    elif result=="O":

        ai_score+=1
        speak("AI wins")
        fireworks()

    else:

        draw_score+=1
        speak("Draw")

    score_label.config(
        text=f"Human:{human_score}  AI:{ai_score}  Draw:{draw_score}"
    )



def create_board():

    for i in range(size*size):

        btn=tk.Button(board_frame,
                      text="",
                      width=5,
                      height=2,
                      font=("Arial",24,"bold"),
                      bg="white",
                      command=lambda i=i:player_move(i))

        btn.grid(row=i//size,column=i%size,padx=6,pady=6)

        buttons.append(btn)



def start_game(mode):

    global size,board

    start_frame.pack_forget()

    size = 3 if mode=="normal" else 4

    board=[""]*(size*size)

    game_frame.pack()

    create_board()



def back_menu():

    game_frame.pack_forget()

    for b in buttons:
        b.destroy()

    buttons.clear()

    start_frame.pack()



def start_gui():

    global root,start_frame,game_frame,board_frame,score_label,canvas,thinking_label

    root=tk.Tk()
    root.title("AI Tic Tac Toe")

    root.configure(bg="#fff9c4")


    title=tk.Label(root,
                   text="TIC TAC TOE AI",
                   font=("Arial",28,"bold"),
                   bg="#fff9c4")

    title.pack(pady=10)


    img=Image.open("robot.png")
    img=img.resize((100,100))
    photo=ImageTk.PhotoImage(img)

    robot=tk.Label(root,image=photo,bg="#fff9c4")
    robot.image=photo
    robot.pack()


    start_frame=tk.Frame(root,bg="#fff9c4")
    start_frame.pack(pady=20)

    tk.Button(start_frame,text="NORMAL 3x3",
              font=("Arial",16),
              bg="#fdd835",
              command=lambda:start_game("normal")).pack(pady=8)

    tk.Button(start_frame,text="ADVANCED 4x4",
              font=("Arial",16),
              bg="#fbc02d",
              command=lambda:start_game("advanced")).pack(pady=8)


    game_frame=tk.Frame(root,bg="#fff9c4")

    board_frame=tk.Frame(game_frame,bg="#fff9c4")
    board_frame.pack()

    thinking_label=tk.Label(game_frame,text="",
                            font=("Arial",14),
                            bg="#fff9c4")
    thinking_label.pack()

    score_label=tk.Label(game_frame,
                         text="Human:0 AI:0 Draw:0",
                         font=("Arial",16),
                         bg="#fff9c4")
    score_label.pack(pady=5)

    tk.Button(game_frame,text="Retry",
              bg="#fdd835",
              command=reset_board).pack(pady=4)

    tk.Button(game_frame,text="Back",
              bg="#fbc02d",
              command=back_menu).pack(pady=4)

    canvas=tk.Canvas(game_frame,width=350,height=150,
                     bg="#fff9c4",highlightthickness=0)
    canvas.pack()

    root.mainloop()