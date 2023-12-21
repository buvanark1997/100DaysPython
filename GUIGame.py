from tkinter import *
import math

# ------------------CONSTANTS--------------
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
tick=""
running_timer =  None
# ----------- count down mechanism-------------


def count_down(count):
    mins = math.floor(count / 60)
    secs = math.floor(count % 60)
    if secs < 10:
        secs = f"0{secs}"
        canvas.itemconfig(show_timer, text=f'{mins}:{secs}')
    if count > 0:
        global running_timer
        running_timer = window.after(1000, count_down, count - 1)
    else:
        start_timer_btn()




def start_timer_btn():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    global tick
    if reps <= 8:
        if reps % 2 != 0:
            count_down(work_sec)
            Timer.config(text="Work",fg="Green")
        elif reps == 8:
            print("cam for long break")
            count_down(long_break_sec)
            Timer.config(text="Break",fg="Red")
            tick += "✔"
            check_marks.config(text=f"{tick}")
        else:
            count_down(short_break_sec)
            Timer.config( text="Break",fg="Pink")
            tick += "✔"
            check_marks.config(text=f"{tick}")


def reset_timer_btn():
    check_marks.config(text="")
    Timer.config(text="Timer", fg="Green")
    window.after_cancel(running_timer)
    canvas.itemconfig(show_timer, text="00:00")
    global reps
    reps = 0


#  UI setup
window = Tk()
window.title("Pomodoro")
window.config(bg="white", padx=100, pady=50)
canvas = Canvas(width=400, height=300, bg="white", highlightthickness=0)

imageCanvas = PhotoImage(file="pomodoro.png")
canvas.configure(background="white")
canvas.create_image((200, 150), image=imageCanvas)
show_timer = canvas.create_text(200, 150, text="00:00", fill="white", font=("Calibri", 30, "bold"))

canvas.grid(row=1, column=1)

start = Button(text="Start", bg="white", command=start_timer_btn, highlightthickness=0)
start.grid(row=2, column=0)
Timer = Label(text="Timer", font=("Calibri", 40), fg="green", bg="white")
Timer.grid(row=0, column=1)
reset = Button(text="Reset", bg="white", command=reset_timer_btn, highlightthickness=0)
reset.grid(row=2, column=2)
check_marks = Label(fg="green", bg="white")
check_marks.grid(column=1, row=3)

window.mainloop()
