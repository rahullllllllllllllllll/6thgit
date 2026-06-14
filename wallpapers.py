from tkinter import *
from PIL import Image,ImageTk
import os
file=["head4.gif","head5.gif","head6.gif"]
imgarray=[]
ut=Tk()
counter=1
def change():
    global counter
    imglabel.config(image=imgarray[counter%len(imgarray)])
    counter+=1

ut.title("Wallpaper")
ut.geometry("500x700")
ut.minsize(300,400)
ut.maxsize(500,700)
ill=Image.open("head4.gif")
ill.save("head4.ico")
ut.iconbitmap("head4.ico")
for i in file:
    img=Image.open(i)
    imig=img.resize((400,400))
    imgarray.append(ImageTk.PhotoImage(imig))
imglabel=Label(ut,image=imgarray[0])
imglabel.pack()
btn=Button(ut,text="NEXT WALLPAPER",bg="black",fg="white",command=change)
btn.pack(pady=(5))


ut.mainloop()