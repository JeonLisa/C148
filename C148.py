from tkinter import *
import random
root=Tk()
root.title("Items In My Picnic Bag")
root.geometry("500x500")
root.configure(background="light pink")
label_item=Label(root)
label_Stuff=Label(root)
label_Num=Label(root)
Items=["tata plushie","basket ball","shin ramen","phone","lightstick","Clothes","food"]
Num=[2,5,6,7,4,3,2,8,1]
label_item["text"]="Listed Items"+str(Items)
label_Num["text"]="Number List"+str(Num)
def SelectItem():
    random_num=random.sample(range(0,7),1)
    label_Stuff["text"]="Put Item Number "+str(random_num)+" In The Picnic Bag "
    Sorted_List=Num.sort()
    label_Num["text"]="Sorted List"+str(Sorted_List)
btn=Button(root,text="Choose Item From The List",command=SelectItem)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)
label_item.place(relx=0.5,rely=0.3,anchor=CENTER)
label_Stuff.place(relx=0.5,rely=0.7,anchor=CENTER)
root.mainloop()