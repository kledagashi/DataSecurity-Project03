import base64
import os
from tkinter import *

import pyDes
from socket import *
import _thread



def initialize_client():
    s = socket(AF_INET, SOCK_STREAM)
    host = 'localhost'
    port = 1234
    s.connect((host, port))

    return s
