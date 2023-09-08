from tkinter import*
root=Tk()
root.geometry('700x700')
root.title('label widget image')
photo=tk.PhotoImage(file='img1.png')
image_label=Label(
    root,
	image=photo,
	text='python',
	compound='top').pack()
root.mainloop()	
	
	
