import tkinter as tk

def switch_theme():
    global bg_color, fg_color
    if bg_color == 'white':
        bg_color = 'black'
        fg_color = 'white'
    else:
        bg_color = 'white'
        fg_color = 'black'

    label.config(bg=bg_color, fg=fg_color)
    button.config(bg=bg_color, fg=fg_color)

root = tk.Tk()
root.title("Dark/Light Mode")

bg_color = 'white'
fg_color = 'black'

label = tk.Label(root, text="Welcome to Dark/Light Mode", bg=bg_color, fg=fg_color)
label.pack(pady=20)

button = tk.Button(root, text="Switch Theme", command=switch_theme, bg=bg_color, fg=fg_color)
button.pack()

root.mainloop()
