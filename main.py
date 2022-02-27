from tkinter import *
from playsound import playsound

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
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_title.config(text="Timer", fg=GREEN)
    label_checklist.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        playsound("break_sound.wav")
        label_title.config(text="Break", fg=GREEN)
        count_down(long_break_sec)
    elif reps % 2 == 1:
        playsound("work_sound.wav")
        label_title.config(text="Work", fg=RED)
        count_down(work_sec)
    elif reps % 2 == 0:
        playsound("break_sound.wav")
        label_title.config(text="Break", fg=PINK)
        count_down(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = int(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(int(reps/2)):
            marks += "✓"
        label_checklist.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# label timer
label_title = Label(text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
label_title.grid(row=0, column=1)

# tomato
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 18, "bold"))
canvas.grid(row=1, column=1)

# btn start
btn_start = Button(text="Start", highlightthickness=0, command=start_timer)
btn_start.grid(row=2, column=0)

# btn reset
btn_reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
btn_reset.grid(row=2, column=2)

# check-list label
label_checklist = Label(text="", font=(FONT_NAME, 18), bg=YELLOW, fg=GREEN)
label_checklist.grid(row=3, column=1)


window.mainloop()
