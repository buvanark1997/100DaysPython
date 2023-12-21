import tkinter
#Pre-installed
window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# label
my_label = tkinter.Label(text="I am a label", font=("Arial",24,"bold"))
my_label.pack()
my_label["text"]="New label for the window"


def button_clicked():
    print("i am clicked")
    new_text = input.get()
    my_label["text"] = new_text

# Button
button = tkinter.Button(text="Click me",command=button_clicked)
button.pack()


# Entry (input field)
def on_change(e):
    print(e.widget.get())

input = tkinter.Entry(width=50)
# input.bind("<Return>", on_change) -- to bind event to entry
input.pack()










# to keep the window live. it always should be end of the window
window.mainloop()