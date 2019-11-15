import tkinter as tk

def test_function():
	a = variable.get()
	b = variable1.get()
	print("This is the entry :", a)
	print("Other is the entry :", b)

root = tk.Tk()

canvas = tk.Canvas(root,height='500',width='600')
canvas.pack()

background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(root,image=background_image)
background_label.place(relwidth=1,relheight=1)


frame = tk.Frame(root, bg = '#80c1ff',bd=5)
frame.place(relx=0.5, rely=0.1,relwidth=0.75,relheight=0.1, anchor='n')

#dropdown
OptionList = [
"Please select one item",
"Aries",
"Taurus",
"Gemini",
"Cancer"
] 

variable = tk.StringVar(frame)
variable.set(OptionList[0])

opt = tk.OptionMenu(frame, variable, *OptionList)
opt.config(width=90, font=('Helvetica', 12))
opt.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)

labelTest = tk.Label(text="", font=('Helvetica', 12), fg='red')
labelTest.pack(side="top")

def callback(*args):
    labelTest.configure(text="The selected item is {}".format(variable.get()))
    # return variable.get()

variable.trace("w", callback)

frame1 = tk.Frame(root, bg = '#80c1ff',bd=5)
frame1.place(relx=0.5, rely=0.25,relwidth=0.75,relheight=0.1, anchor='n')

OptionList1 = [
"Please select one item",
"Aries",
"Taurus",
"Gemini",
"Cancer"
]

variable1 = tk.StringVar(frame1)
variable1.set(OptionList1[0])

opt1 = tk.OptionMenu(frame1, variable1, *OptionList1)
opt1.config(width=90, font=('Helvetica', 12))
opt1.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)

labelTest1 = tk.Label(text="", font=('Helvetica', 12), fg='red')
labelTest1.pack(side="top")

button = tk.Button(root,text="Submit",font=40,command=lambda: test_function())
button.place(relx=0.36,rely=0.4,relheight=0.07,relwidth=0.3)

# start the GUI 
root.mainloop() 
