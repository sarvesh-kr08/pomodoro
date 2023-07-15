from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    timer_label.config(text='Timer')
    checkmark_label.config(text="")
    canvas.itemconfig(timer_text, text='00:00')


# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1

    if reps % 2 == 0:
        countdown(SHORT_BREAK_MIN * 60)
        timer_label.config(text='Break', fg=PINK)
    elif reps == 8:
        countdown(LONG_BREAK_MIN * 60)
        timer_label.config(text='Break', fg=RED)
    else:
        countdown(WORK_MIN * 60)
        timer_label.config(text='Work', fg=GREEN)


def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        work_session = math.floor(reps/2)
        mark = ''
        for _ in range(work_session):
            mark += '✔'
        checkmark_label.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
# window.after(1000)
window.config(padx=100, pady=100, bg=YELLOW)
window.title('Pomodoro')
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)
timer_label = Label(text='Timer', font=(FONT_NAME, 35, 'bold'), bg=YELLOW, fg=GREEN)
timer_label.grid(column=1, row=0)
start_button = Button(text='START', command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text='RESET', command=reset_timer)
reset_button.grid(column=2, row=2)
checkmark_label = Label(font=(FONT_NAME, 35, 'bold'), fg=GREEN, bg=YELLOW)
checkmark_label.grid(column=1,row=3)


window.mainloop()
