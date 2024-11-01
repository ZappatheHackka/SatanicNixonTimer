from tkinter import *
import math
from playsound import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Times New Roman"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = ""
sets = 0
num = 1

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global timer
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    canvas.itemconfig(model_text, text="")
    reps.config(text="")
    global sets
    sets = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global sets
    sets += 1
    work_secs = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if sets % 8 == 0:
        window.deiconify()
        window.attributes('-topmost', 1)
        window.attributes('-topmost', 0)
        countdown(long_break)
        canvas.itemconfig(model_text, text="Throw your feet up like a stuffy Liberal Elite for now, Franklin.")
        playsound("C:/Users\chris\PycharmProjects\pomodoro-start\Frozen_Remnants_Collections.mp3")
    elif sets % 2 == 0:
        window.deiconify()
        window.attributes('-topmost', 1)
        window.attributes('-topmost', 0)
        countdown(short_break)
        canvas.itemconfig(model_text, text="Work like a Democrat--Take a break!!")
        playsound("C:/Users/chris/PycharmProjects/pomodoro-start/Checkers_Speech_CoD_Zombies_Creepypasta.mp3")
    else:
        window.deiconify()
        window.attributes('-topmost', 1)
        window.attributes('-topmost', 0)
        countdown(work_secs)
        canvas.itemconfig(model_text, text="That bastard Kennedy is working hard, AND NOW YOU WILL TOO DAMMIT!!!")
        playsound("C:/Users\chris\PycharmProjects\pomodoro-start/Not_A_Crock.mp3")




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def countdown(count):
    global sets
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        canvas.create_window(240, 385, window=reps)
        mark = ""
        for _ in range(math.floor(sets/2)):
            mark += "⛧⁶⁶⁶"
            reps.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #


check_mark = "⛧⁶⁶⁶"


window = Tk()
window.title("The Orthogonian Labor Timer")
window.config(pady=10, padx=10, bg="red4")


titletext = Label(text="Hello, my fellow Orthogonian...", font=(FONT_NAME, 15, "bold"), bg="red4")
titletext.grid(row=0, column=2)

god = PhotoImage(file="37_richard_nixon.png")
canvas = Canvas(width=500, height=500)
canvas.create_image(250, 250, image=god)
timer_text = canvas.create_text(235, 130, text="00:00", fill="gray1", font=(FONT_NAME, 38, "bold"))
model_text = canvas.create_text(240, 15, text="", fill="white", font=(FONT_NAME, 10, "bold"))
canvas.grid(row=1, column=2)


start = Button(text="Begin Suffering")
start.config(padx=1, pady=1, command=start_timer)


end = Button(text="Be Born Anew", command=reset_timer)

reps = Label(bg="firebrick4", fg="black", font=("arial", 18, "bold"))


canvas.create_window(70, 280, window=start)
canvas.create_window(403, 278, window=end)


window.mainloop()
