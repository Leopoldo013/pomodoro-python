# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 20
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 25
reps = 0
timer = None
import math
import emoji


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(time_set, text="00:00")
    label_timer.config(text="Timer")
    label_check.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_regre(long_break_sec)
        label_timer.config(text="Pausa", fg=RED)
    elif reps % 2 == 0:
        count_regre(short_break_sec)
        label_timer.config(text="Pausa", fg=PINK)
    else:
        count_regre(work_sec)
        label_timer.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_regre(count):
    count_minutos = math.floor(count / 60)
    count_segundos = count % 60

    if count_segundos < 10:
        count_segundos = f"0{count_segundos}"
    elif count_minutos < 10:
        count_minutos = f"0{count_minutos}"

    canvas.itemconfig(time_set, text=f"{count_minutos}:{count_segundos}")
    if count > 0:
        global timer
        timer = window.after(1000, count_regre, count - 1)
    else:
        start_timer()

        mark = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            mark += "!"
            print(mark)
            label_check.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

window = Tk()
window.title("#Crazy - Pomodoro#")
window.config(padx=150, pady=100, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
time_set = canvas.create_text(100, 130, text="00:00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=1, column=1)





# Botões

botao_start = Button(text="Start", width=10, command=start_timer)
botao_start.grid(row=2, column=0)

botao_reset = Button(text="Reset", width=10, command=reset_timer)
botao_reset.grid(row=2, column=2)

# Label

label_timer = Label(text="Timer", font=(FONT_NAME, 45, "bold"), bg=YELLOW)
label_timer.grid(row=0, column=1)

label_check = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, "bold"))
label_check.grid(row=3, column=1)

window.mainloop()
