from tkinter import *  
  
  
def inc():  
    summ1.configure(text=f"Ответ: {int(txt.get()) + int(txt2.get())}")  

def dec():  
    summ2.configure(text=f"Ответ: {int(txt3.get()) - int(txt4.get())}") 
    
def umn():  
    summ3.configure(text=f"Ответ: {int(txt5.get()) * int(txt6.get())}") 
    
def de():  
    if(int(txt2.get()) != 0):
        summ5.configure(text=f"Ответ: {int(txt7.get()) / int(txt8.get())}") 
    else:
        summ5.configure(text=f"Ответ: Error")
    
def dez():  
    if(int(txt2.get()) != 0):
        summ6.configure(text=f"Ответ: {int(txt9.get()) //int(txt10.get())}") 
    else:
        summ6.configure(text=f"Ответ: Error")
    
def deost():  
    if(int(txt2.get()) != 0):
        summ7.configure(text=f"Ответ: {int(txt11.get()) % int(txt12.get())}") 
    else:
        summ7.configure(text=f"Ответ: Error")
    
def step():  
    summ8.configure(text=f"Ответ: {int(txt13.get()) ** int(txt14.get())}")         
    
  
window = Tk()  
window.title("Добро пожаловать в приложение PythonRu")  
window.geometry('800x850') 


lbl = Label(window, text='плюс') 
lbl.grid(column=1, row=1)     
  
txt = Entry(window, width=10)  
txt.grid(column=1, row=2)  
  
txt2 = Entry(window, width=10)  
txt2.grid(column=1, row=3)  

summ1 = Label(window, text="ответ:") 
summ1.grid(column=1, row=5)
    
btn = Button(window, text="Ответ", command=inc)  
btn.grid(column=5, row=5)  


lbl = Label(window, text='минус') 
lbl.grid(column=1, row=7)     

txt3 = Entry(window, width=10)  
txt3.grid(column=1, row=7)  
 
txt4 = Entry(window, width=10)  
txt4.grid(column=1, row=8)  

summ2 = Label(window, text="ответ:") 
summ2.grid(column=1, row=9)
    
btn = Button(window, text="Ответ", command=dec)  
btn.grid(column=5, row=9)  


lbl = Label(window, text='умножить') 
lbl.grid(column=1, row=10)     
  
txt5 = Entry(window, width=10)  
txt5.grid(column=1, row=11)  
  
txt6 = Entry(window, width=10)  
txt6.grid(column=1, row=12)  

summ3 = Label(window, text="ответ:") 
summ3.grid(column=1, row=13)
    
btn = Button(window, text="Ответ", command=umn)  
btn.grid(column=5, row=13)  




lbl = Label(window, text='поделить') 
lbl.grid(column=1, row=14)     

txt7 = Entry(window, width=10)  
txt7.grid(column=1, row=14+1)  
  
txt8 = Entry(window, width=10)  
txt8.grid(column=1, row=14+2)  

summ5 = Label(window, text="ответ:") 
summ5.grid(column=1, row=14+3)
    
btn = Button(window, text="Ответ", command=de)  
btn.grid(column=5, row=14+3)  




lbl = Label(window, text='делить без остатка') 
lbl.grid(column=1, row=18)     
 
txt9 = Entry(window, width=10)  
txt9.grid(column=1, row=18+1)  
  
txt10 = Entry(window, width=10)  
txt10.grid(column=1, row=18+2)  

summ6 = Label(window, text="ответ:") 
summ6.grid(column=1, row=18+3)
    
btn = Button(window, text="Ответ", command=dez)  
btn.grid(column=5, row=18+3)  




lbl = Label(window, text='делить с остатком') 
lbl.grid(column=1, row=23)     

txt11 = Entry(window, width=10)  
txt11.grid(column=1, row=23+1)  
 
txt12 = Entry(window, width=10)  
txt12.grid(column=1, row=23+2)  

summ7 = Label(window, text="ответ:") 
summ7.grid(column=1, row=23+3)
    
btn = Button(window, text="Ответ", command=deost)  
btn.grid(column=5, row=23+3)  




lbl = Label(window, text='степень') 
lbl.grid(column=1, row=29)     
  
txt13 = Entry(window, width=10)  
txt13.grid(column=1, row=29+1)  
  
txt14 = Entry(window, width=10)  
txt14.grid(column=1, row=29+2)  

summ8 = Label(window, text="ответ:") 
summ8.grid(column=1, row=29+3)
    
btn = Button(window, text="Ответ", command=step)  
btn.grid(column=5, row=29+3)  


window.mainloop()






#class Person:
 
    #def __init__(self, name, age):
        #self.name = name  
        #self.age = age    
          
 
 
#class Tom(Person):

    #def say_hello(self):
            #print("Hello")      
    
 
#people = Tom("Tom", 22)
 
#people.say_hello()
#print(people.name)    
#print(people.age)      


#people.age = 37
#print(people.age)  









#import random
#import tkinter
#import tkinter.filedialog
#import json

#file = open('file.txt', 'w+')

#a = []
#b = 0

#i=0
#while(i < 10):
    #rand = random.randint(0, 100)
    #b = b + rand
    #a.append(rand)
    #i = i+ 1
    
#print(a)




#file.write(f'{a}')
#file.close()

#filePath = tkinter.filedialog.askopenfilename(title="Выберите файл", filetypes=[("Text files","*.txt"), ("All files", "*.*")])
#file = open(filePath, 'r')

#content = file.read()
#content = json.loads(content)

#print(content)
#print(sum(content) / len(content))
