import tkinter as tk
import requests

URL = "https://api.quotable.io/random"

def fetch_quote():
    response = requests.get(URL)
    data = response.json()
    quote = data["content"]
    author = data["author"]
    return quote, author

def update_quote():
    quote, author = fetch_quote()
    quote_label.config(text=quote)
    author_label.config(text=f"~{author}")

root = tk.Tk()
root.title("Quotes Generator")
root.geometry("1000x350")

frame = tk.Frame(root)
frame.pack(padx=30, pady=40)

quote_label = tk.Label(frame, text="", font=("Georgia", 13), wraplength=800)
quote_label.pack()

author_label = tk.Label(frame, text="", font=("Georgia", 9))
author_label.pack(pady=10)

button = tk.Button(frame, text="Get Quote", command=update_quote,
                   bg='#89CFF0', fg='black',
                   activebackground='#5DADE2', activeforeground='black',
                   highlightbackground='black', highlightthickness=1,
                   relief='flat')  # Use 'solid' for a solid border
button.pack(pady=20)

root.mainloop()
