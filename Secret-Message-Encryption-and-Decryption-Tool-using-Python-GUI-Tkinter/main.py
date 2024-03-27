import tkinter as tk
from tkinter import simpledialog

# Function to encode the secret message
def encode(key, message):
    encoded_chars = []
    for i in range(len(message)):
        if message[i].isalpha():

