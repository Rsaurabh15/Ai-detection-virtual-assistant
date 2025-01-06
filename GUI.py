from tkinter import *
from PIL import Image, ImageTk
import speech_to_text
import action

# Single Tk instance
root = Tk()
root.title("AI Assistant")
root.geometry("500x675")
root.resizable(False, False)
root.config(bg="#6f8fAF")

# Function to handle bot interaction
def handle_interaction(user_input):
    bot_response = action.action(user_input)
    text.insert(END, f"User ---> {user_input}\n")
    if bot_response:
        text.insert(END, f"BOT <--- {bot_response}\n")
    if bot_response == "ok sir":
        root.destroy()

# Ask function
def ask():
    user_input = speech_to_text.speech_to_text()
    handle_interaction(user_input)

# Send function
def send():
    user_input = entry.get()
    if user_input.strip():
        handle_interaction(user_input)
        entry.delete(0, END)

# Delete function
def delete():
    text.delete("1.0", "end")

# Add main frame
frame = LabelFrame(root, padx=10, pady=10, borderwidth=3, relief="raised", bg="#6f8fAF")
frame.grid(row=0, column=0, padx=20, pady=20)

# Title label
Label(frame, text="AI Assistant", font=("Comic Sans MS", 16, "bold"), bg="#356696", fg="white").grid(row=0, column=0, padx=55, pady=10)

# Add image with resizing
try:
    image = Image.open("image/assistant.png")  # Replace with your image path
    image = image.resize((120, 120))  # Resize the image to fit the window size
    image = ImageTk.PhotoImage(image)
    Label(frame, image=image).grid(row=1, column=0, pady=10)
except FileNotFoundError:
    Label(frame, text="Image not found!", font=("Comic Sans MS", 12), bg="#6f8fAF", fg="red").grid(row=1, column=0, pady=10)

# Text widget to display conversation
text = Text(root, font=("Courier", 10, "bold"), bg="#f0f0f0", fg="black", wrap=WORD, height=15, width=55, padx=5, pady=5)
text.grid(row=1, column=0, padx=20, pady=10)

# Entry widget for user input
entry = Entry(root, font=("Comic Sans MS", 12), bg="#ffffff", fg="black")
entry.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

# Frame for buttons
button_frame = Frame(root, bg="#6f8fAF")
button_frame.grid(row=3, column=0, pady=10)

# Ask button
Button(button_frame, text="ASK", bg="#356696", fg="white", pady=8, padx=15, borderwidth=3, relief=SOLID, command=ask).pack(side=LEFT, padx=10)

# Send button
Button(button_frame, text="SEND", bg="#356696", fg="white", pady=8, padx=15, borderwidth=3, relief=SOLID, command=send).pack(side=LEFT, padx=10)

# Delete button
Button(button_frame, text="DELETE", bg="#356696", fg="white", pady=8, padx=15, borderwidth=3, relief=SOLID, command=delete).pack(side=LEFT, padx=10)

# Run the application
root.mainloop()

