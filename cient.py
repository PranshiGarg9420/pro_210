from glob import glob
from threading import Thread
import socket
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from playsound import playsound
import os
import time
import pygame   
from pygame import mixer

SERVER= None
IP_ADDRESS= '127.0.0.1'
PORT= 8050
BUFFER_SIZE= 4096

global song_counter
song_counter = 0

name= None
listbox= None
filePathLabel= None
infoLabel= None



def play():
    global song_slected
    song_selected= listbox.get(ANCHOR)

    pygame
    mixer.init()
    mixer.music.load('shared_files/'+ song_selected)
    mixer.music.play()
    if(song_selected != ''):
        infoLabel.configure(text='Now Playing: '+ song_selected)
    else:
        infoLabel.configure(text='')


def stop():
    global song_selected

    pygame
    mixer.init()
    mixer.music.load('shared_files/'+ song_selected)
    mixer.music.pause()
    infoLabel.configure(text='')


def resume():
    global song_selected

    mixer.init()
    mixer.music.load('shared_files/'+ song_selected)
    mixer.music.play()


def pause():
    global song_selected
    pygame
    mixer.init()
    mixer.music.load('shared_files/'+ song_selected)
    mixer.music.pause()


def musicWindow():
    global song_counter
    global name
    global listbox
    global filePathLabel
    global infoLabel

    window= Tk()
    window.title('Music Window')
    window.geometry('600x600')
    window.configure(bg='pink')
    
    selectlabel = Label(window, text= "Select Song",bg='pink', font = ("Calibri",15))
    selectlabel.place(x=2, y=1)
    
    listbox = Listbox(window,height = 15,width = 52,activestyle = 'dotbox',bg='pink',borderwidth=2, font = ("Calibri",14))
    listbox.place(x=10,y=40)
    for file in os.listdir('shared_files'):
        filename= os.fsdecode(file)
        listbox.insert(song_counter, filename)
        song_counter+=1

    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight = 1,relx = 1)
    scrollbar1.config(command = listbox.yview)
    
    PlayButton=Button(window,text="Play", width=13,bd=1,bg='tomato',font = ("Calibri",14), command=play)
    PlayButton.place(x=30,y=440)
    
    PauseButton=Button(window,text="Pause", width=13,bd=1,bg='tomato',font = ("Calibri",14), command=pause)
    PauseButton.place(x=200,y=490)

    ResumeButton=Button(window,text="Resume", width=13,bd=1,bg='tomato',font = ("Calibri",14), command=resume)
    ResumeButton.place(x=30,y=490)

    Stop=Button(window,text="Stop",bd=1,width=13,bg='tomato', font = ("Calibri",14), command=stop)
    Stop.place(x=200,y=440)
    
    Upload=Button(window,text="Upload",width=13,bd=1,bg='tomato', font = ("Calibri",14))
    Upload.place(x=30,y=540)
    
    Download =Button(window,text="Download",width=13,bd=1,bg='tomato', font = ("Calibri",14))
    Download.place(x=200,y=540)

    infoLabel = Label(window, text= "",fg= "blue",bg='tomato', font = ("Calibri",11))
    infoLabel.place(x=10, y=595)
    
    window.mainloop()





def setup():
    global IP_ADDRESS
    global SERVER
    global PORT

    server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((IP_ADDRESS, PORT))

    musicWindow()

setup()
