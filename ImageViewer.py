from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("Image Viewer")
root.iconbitmap('D:/python Code/Tinker/cons/im.ico')

my_img1=ImageTk.PhotoImage(Image.open('D:/python Code/Tinker/pics/me1.jpg'))
my_img2=ImageTk.PhotoImage(Image.open('D:/python Code/Tinker/pics/me2.jpg'))
my_img3=ImageTk.PhotoImage(Image.open('D:/python Code/Tinker/pics/me3.jpeg'))
my_img4=ImageTk.PhotoImage(Image.open('D:/python Code/Tinker/pics/me4.jpg'))
my_img5=ImageTk.PhotoImage(Image.open('D:/python Code/Tinker/pics/me5.jpg'))
my_img6=ImageTk.PhotoImage(Image.open('D:/python Code/Tinker/pics/we.jpg'))

images=[my_img1,my_img2,my_img3,my_img4,my_img5,my_img6]

my_label=Label(image=my_img1)
my_label.grid(row=0,column=0,columnspan=3)

status=Label(root, text="Image 1 of 6", bd=1, relief=SUNKEN, anchor=E)
status.grid(row=2,column=0,columnspan=3,sticky=E+W)


def forward(image_number):
    global my_label
    global button_back
    global button_forward

    my_label.grid_forget()
    my_label=Label(image=images[image_number-1])
    button_forward=Button(root,text=">>",command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: backward(image_number-1))

    status = Label(root, text=f'Image {image_number} of 6', bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=E + W)

    if image_number == 6 :
        button_forward=Button(root,text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_quit.grid(row=1, column=1)
    button_forward.grid(row=1, column=2)


def backward(image_number):
    global my_label
    global button_back
    global button_forward

    my_label.grid_forget()
    my_label = Label(image=images[image_number - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command= lambda: backward(image_number-1))

    status = Label(root, text=f'Image {image_number} of 6', bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=E + W)

    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_quit.grid(row=1, column=1)
    button_forward.grid(row=1, column=2)


button_back=Button(root,text="<<",command= backward, state=DISABLED)
button_quit=Button(root, text="EXIT", command=root.quit)
button_forward=Button(root,text=">>",command=lambda: forward(2))

button_back.grid(row=1,column=0)
button_quit.grid(row=1,column=1)
button_forward.grid(row=1,column=2)

root.mainloop()
