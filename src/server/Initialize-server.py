import _thread
import os
from socket import *
from tkinter import *

import pyDes


def initialize_server():
    s = socket(AF_INET, SOCK_STREAM)
    host = 'localhost'  
    port = 1234
    s.bind((host, port))
    s.listen(1)

    
    conn, addr = s.accept()

    return conn


def GUI():
    global chatlog
    global textbox

    
    gui = Tk()
   
    gui.title("Server Chat")
    
    gui.geometry("380x430")

