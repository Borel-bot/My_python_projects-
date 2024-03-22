import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Simple Calculator")

# Create the entry widget to show calculations
entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Function to add numbers and operations to the entry widget
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(number))

# Function to clear the entry widget
def button_clear():
    entry.delete(0, tk.END)

# Function to calculate the result
def button_equal():
    result = eval(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, str(result))

# Function to create a button 
def create_button(text, command, row, column):
    return tk.Button(root, text=text, padx=20, pady=20, command=command).grid(row=row, column=column)

# Create number buttons
for i in range(1, 10):
    create_button(i, lambda i=i: button_click(i), (i-1)//3 + 1, (i-1)%3)

# Create operation button
create_button(0, lambda: button_click(0), 4, 0)
create_button('+', lambda: button_click('+'), 1, 3)
create_button('-', lambda: button_click('-'), 2, 3)
create_button('*', lambda: button_click('*'), 3, 3)
create_button('/', lambda: button_click('/'), 4, 3)

# Create equal button
create_button('=', button_equal, 4, 2)

# Create clear button
create_button('C', button_clear, 4, 1)

# Run the application
root.mainloop()
