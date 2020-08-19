import tkinter as tk
import time

root = tk.Tk()
cv_width = 1280
cv_height = 720
cv = tk.Canvas(root, width=cv_width, height=cv_height, bg='black')
cv.pack()


walk_right = [tk.PhotoImage(file="images/walk300/walk_right_1.png"),
              tk.PhotoImage(file="images/walk300/walk_right_2.png"),
              tk.PhotoImage(file="images/walk300/walk_right_3.png")]
stickman_walk = cv.create_image(cv_width/2, cv_height/2, image=walk_right[0])

image_index = 0


def walk_animate():
    global image_index
    image_index += 1
    cv.itemconfig(stickman_walk, image=walk_right[image_index % 3])


while True:
    walk_animate()
    root.update_idletasks()
    root.update()
    time.sleep(0.2)
