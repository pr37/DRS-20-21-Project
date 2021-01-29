import sys
import socket
import selectors
import types
import pickle
import playsound

class PlayMusic():
    def __init__(self):
        super().__init__()
        playsound.playsound('muzika.mp3', True)