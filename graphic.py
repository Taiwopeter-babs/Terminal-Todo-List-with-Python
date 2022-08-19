from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Images")
root.geometry("500x520")
root.resizable(width=False, height=False)

# frame container
frame = LabelFrame(root, text="Jhene to KLaus", padx=10, pady=10)

# images definition
my_img1 = ImageTk.PhotoImage(
    Image.open("images/image1.jpg").resize((400, 400), Image.ANTIALIAS)
)
my_img2 = ImageTk.PhotoImage(
    Image.open("images/image2.jpg").resize((400, 400), Image.ANTIALIAS)
)
my_img3 = ImageTk.PhotoImage(
    Image.open("images/image3.jpg").resize((400, 400), Image.ANTIALIAS)
)
my_img4 = ImageTk.PhotoImage(
    Image.open("images/image4.jpg").resize((400, 400), Image.ANTIALIAS)
)
my_img5 = ImageTk.PhotoImage(
    Image.open("images/image5.jpg").resize((400, 400), Image.ANTIALIAS)
)
my_img6 = ImageTk.PhotoImage(
    Image.open("images/image6.jpg").resize((400, 400), Image.ANTIALIAS)
)

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5, my_img6]

# images container
label = Label(frame, image=my_img1)
label.grid(row=0, column=0, columnspan=3)

# status of images
status = Label(
    frame, text=f"image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E
)

# buttons' functions
def back(image_num):
    global label
    global button_bck
    global button_fwd

    label.grid_forget()
    label = Label(frame, image=image_list[image_num - 1])

    button_fwd = Button(
        frame, text=">>", fg="white", bg="green", command=lambda: forward(image_num + 1)
    )
    button_bck = Button(
        frame, text="<<", fg="white", bg="green", command=lambda: back(image_num - 1)
    )

    # status of images
    status = Label(
        frame,
        text=f"image {image_num} of " + str(len(image_list)),
        bd=1,
        relief=SUNKEN,
        anchor=W,
    )

    if image_num == 1:
        button_bck = Button(frame, text="<<", fg="white", bg="green", state=DISABLED)

    label.grid(row=0, column=0, columnspan=3)
    button_fwd.grid(row=1, column=2)
    button_bck.grid(row=1, column=0)

    # updating status of images
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


def forward(image_num):
    global label
    global button_bck
    global button_fwd

    label.grid_forget()
    label = Label(frame, image=image_list[image_num - 1])

    button_fwd = Button(
        frame, text=">>", fg="white", bg="green", command=lambda: forward(image_num + 1)
    )
    button_bck = Button(
        frame, text="<<", fg="white", bg="green", command=lambda: back(image_num - 1)
    )

    # status of images
    status = Label(
        frame,
        text=f"image {image_num} of " + str(len(image_list)),
        bd=1,
        relief=SUNKEN,
        anchor=E,
    )

    if image_num == 6:
        button_fwd = Button(frame, text=">>", fg="white", bg="green", state=DISABLED)

    label.grid(row=0, column=0, columnspan=3)
    button_fwd.grid(row=1, column=2)
    button_bck.grid(row=1, column=0)

    # updating status of images
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


# scrolling buttons
button_bck = Button(
    frame, text="<<", fg="white", bg="green", command=lambda: back(0), state=DISABLED
)
button_fwd = Button(
    frame, text=">>", fg="white", bg="green", command=lambda: forward(2)
)
button_exit = Button(frame, text="Exit Images", command=root.quit)

button_bck.grid(row=1, column=0)
button_exit.grid(row=1, column=1, pady=10)
button_fwd.grid(row=1, column=2)
status.grid(row=2, column=0, columnspan=3, sticky=W + E)
frame.grid(padx=10, pady=10, ipadx=50, ipady=50)


"""quit_button = Button(root, text='Exit Program', fg='white', bg="black", command=root.quit)
quit_button.grid(row=3, column=1)"""


root.mainloop()
