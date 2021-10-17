import tkinter as tk

FONT = ('Arial',24, 'bold')


# Window
window = tk.Tk()
window.title('MORSE CODE')
window.minsize(width=300, height=200)
window.config(padx=10, pady=10, bg='#004660')

# Canvas
canvas = tk.Canvas(width=400, height=100, bg='white', highlightthickness=0, highlightcolor='white')
canvas.grid(column=0, row=0, columnspan=2)

# logo
logo = tk.PhotoImage(file='img/logo.png')
canvas.create_image(210, -25, image=logo)

# input 
in_label = tk.Label(text='INPUT', font=('Arial',15,'normal'), fg='white', bg='#004660')
in_label.grid(column=0, row=1, columnspan=2, padx=5, pady=15)

window.mainloop()
