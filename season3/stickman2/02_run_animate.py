import tkinter as tk
import time

root = tk.Tk()
root.title("Walk Animate")
cv_width = 1280
cv_height = 720
cv = tk.Canvas(root, width=cv_width, height=cv_height, bg='black')
cv.pack()

run_right = [
    tk.PhotoImage(file="images/run300/run_right_1.png"),
    tk.PhotoImage(file="images/run300/run_right_2.png"),
    tk.PhotoImage(file="images/run300/run_right_3.png"),
    tk.PhotoImage(file="images/run300/run_right_4.png")
]
stickman_run = cv.create_image(cv_width / 2, cv_height / 2, image=run_right[0])

image_index = 0


def animate():
    global image_index
    image_index += 1
    cv.itemconfig(stickman_run, image=run_right[image_index % 4])


while True:
    animate()
    root.update_idletasks()
    root.update()
    time.sleep(0.12)
