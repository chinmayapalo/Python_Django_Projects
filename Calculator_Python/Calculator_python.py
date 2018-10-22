from tkinter import *

def iCalc(source,side):
    storeobj = Frame(source, borderwidth=4, bd=4, bg="powder blue")
    storeobj.pack(side=side,expand=YES, fill = BOTH)
    return  storeobj;

def button(source,side, text, command=None):
    storeobj = Button(source,text= text, command=command)
    storeobj.pack(side=side,expand=YES, fill = BOTH)
    return  storeobj;

class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font','arial 20 bold')
        self.pack(expand=YES, fill=BOTH)
        self.master.title('calculator')


        display = StringVar()
        Entry(self,relief=RIDGE,
              textvariable=display,justify='right', bd=30,bg="powder blue").pack(side=TOP
                                                                                 ,expand=YES, fill=BOTH)
        for clearbut in (["CE"],["C"]):
            erase = iCalc(self,TOP)
            for ichar in clearbut:
                button(erase,LEFT,ichar,
                       lambda store=display,q=ichar: store.set(''))

        for numbat in ("789/","456*","123-","0.+"):
            FunctionNum = iCalc(self,TOP)
            for ichar in numbat:
                button(FunctionNum,LEFT,ichar,
                       lambda store=display,q=ichar: store.set(store.get()+q))

        Equalsbutton = iCalc(self,TOP)
        for iEquals in "=":
            if iEquals == '=':
                btnEquals = button(Equalsbutton,LEFT,iEquals)
                btnEquals.bind('<ButtonRelease-1>',
                               lambda  e,s=self,store=display: s.calc(store))



    def calc(self,display):
        try:
            display.set(eval(display.get()))
        except:
            display.set('error')






if __name__ == '__main__':
    app().mainloop()



