from tkinter import *
root = Tk()
root.title("Scrollbar Widget")
#ITEMS
list = ["Shirt","Bag","Toy","Books","Fruits",
        "Vegetables","Jeans","Headphones",
        "Watch","Dress","Snaks","Dry fruits",
        'Mobile','Headphones','Shoes']
#Function CALls on Button Click
def add():
    w = Lb.get(ACTIVE)
    cart.insert(END,w)
    Scr.set(10,400)
    print("Item {} Added to Your Cart".format(w))

#Item Listbox
Lb = Listbox(root)
Lb.pack(side=LEFT, expand=1,fill=X)

cart = Listbox(root)
cart.pack(side=RIGHT, expand=1,fill=X)

# TKINTER SCROLLBAR
Scr = Scrollbar(root,troughcolor='red',jump=1,width=32)
Scr.pack(side=LEFT,fill=Y)

Btn= Button(root,text="ADD TO CART ->",fg='white',bg='green',command=add).pack(side=RIGHT)
for i in list:
    Lb.insert(END ,i)

#CONFIG SCROLLBAR WITH WIDGET
Lb.config(yscrollcommand=Scr.set)
Scr.config(command=Lb.yview)

# OUTPUT SCREEN
mainloop()
