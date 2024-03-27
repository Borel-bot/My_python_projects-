import tkinter as tk
from tkinter import simpledialog

# Function to encode the secret message
def encode(key, message):
    encoded_chars = []
    for i in range(len(message)):
        if message[i].isalpha():
            shitf = 65 if message[i].isupper() else 97
            encoded_char = chr((ord(message[i]) + key - shift) %26 + shift)
            encoded_chars.append(encoded_char)
        else:

            encoded_chars.append(message[i])
    return ''.join(encoded_chars)
# Function to decode the secret message
def decode(key, message):
    return encode(-key, message)

# Function to handle the encode button click
def on_encode():
    key = int(key_entry.get())
    message = message_entry.get()
    encoded_message = encode(key, message)
    result_label.config(text=f'Encoded Message: {encoded_message}')

# Function to handle the decode button click
def on_decode():
    key = int(key_entry.get())
    message = message_entry.get()
    decode_message = decode(key, message)
    result_label.config(text=f'Decoded Message: {decoded_message}')

# Create the main window of the application
root = tk.Tk()
root.title("Secret message Encoder/Decoder")

# Create and place the key entry
tk.Label(root, text="Key:").grid(row=0, column=0)
key_entry = tk.Entry(root)
key_entry.grid(row=0, column=1)

# Create and place the message entry
tk.Label(root, text="Message:").grid(row=1, column=0)
message_entry = tk.Entry(root)
message_entry.grid(row=1, column=1)

# Create and place the result label
result_label = tk.Label(root, text="Result:")
result_label.grid(row=3, column=0, columnspan=2)

# Create and place the encode and decode buttons
encode_button = tk.Button(root, text="Encode", command=on_encode)
encode_button.grid(row=2, column=0)
decode_button = tk.Button(root, text="Decode", command=on_decode)
decode_button.grid(row=2, column=1)

# Run the main loop
root.mainloop()
