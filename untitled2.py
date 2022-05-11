# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 20:35:17 2021

@author: Vikas reddy
"""

root = Tk()
root.title("pattern matching")

e1 = Entry(root, width=35, borderwidth=5)
e1.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

e2= Entry(root, width=35, borderwidth=5)
e2.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

e3= Entry(root, width=35, borderwidth=5)
e3.grid(row=4, column=0, columnspan=3, padx=10, pady=10)
e3.insert(0,"output")
def func():
    e3.delete(0,END)
 
    kwtree = KeywordTree(case_insensitive=True)
    kwtree.add(pattern)
    kwtree.add('lacrosse')
    kwtree.add('mallorca')
    kwtree.add('mallorca bella')
    kwtree.add('orca')
    kwtree.finalize()
    results = kwtree.search_all(sequence)
    g=""
    for result in results:  
        g=g+result
    e3.insert(0,g)

def get_sequence():
    a=e1.get()
    b=e2.get()
    global sequence
    global pattern
    sequence= str(b)
    pattern=str(a) 
    func()
    # Define Buttons

button_1 = Button(root, text="enter the sequence", padx=40, pady=20, command=get_sequence)
#button_clear = Button(root, text="Clear", padx=79, pady=20, command=button_clear)
button_1.grid(row=3, column=0)



root.mainloop()