#1
import tkinter as tk  

window = tk.Tk()  

greeting = tk.Label(text="Hello, Tkinter")  

greeting.pack()  

window.mainloop()  

  

 

 

  

 

 
#2
import tkinter as tk  

window = tk.Tk()  

greeting = tk.Label(text="Hello, Tkinter"',fg="red"')  

greeting.pack()  

window.mainloop()  

  

 

 

  

 

 

  

 

 
#3
import tkinter as tk  

window = tk.Tk()  

x= tk.Label(  

text="Hello,Hi",  

fg="white",  

width=25,  

height=5,  

bg="blue"  

)  

 

 

x.pack  

window.mainloop()  

  

 

 

  

 

 

  

 

 
#4
import tkinter as tk  

window = tk.Tk()  

b= tk.Button(  

text="Submit",  

width=25,  

height=5,  

bg="blue",  

fg="yellow"  

)  

b.pack()  

window.mainloop() 

 
#5
import tkinter as tk 

 

 

root = tk.Tk() 

 

 

v = tk.IntVar() 

 

 

tk.Label(root,  

        text="""Choose a  

programming language:""", 

        justify = tk.LEFT, 

        padx = 20).pack() 

tk.Radiobutton(root,  

              text="Python", 

              padx = 20,  

              variable=v,  

              value=1).pack(anchor=tk.W) 

tk.Radiobutton(root,  

              text="Perl", 

              padx = 20,  

              variable=v,  

              value=2).pack(anchor=tk.W) 

 

 

root.mainloop( 

 
