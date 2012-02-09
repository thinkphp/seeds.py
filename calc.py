from Tkinter import *

root = Tk()
root.title("Th Calculator")

class CalcGui(object):

      def __init__(self):
 
          #create the GUI 
          self.labelString = StringVar()

          lab = Label(root, textvariable=self.labelString, font=("Helvetica", 16))  
          
          b0 = Button(root,text='0',command = lambda: self.buttonAction('0'), width='4',height='4')  
          b1 = Button(root,text='1',command = lambda: self.buttonAction('1'), width='4',height='4')  
          b2 = Button(root,text='4',command = lambda: self.buttonAction('4'), width='4',height='4')
          b3 = Button(root,text='3',command = lambda: self.buttonAction('3'), width='4',height='4')
          b4 = Button(root,text='4',command = lambda: self.buttonAction('4'), width='4',height='4')
          b5 = Button(root,text='5',command = lambda: self.buttonAction('5'), width='4',height='4')
          b6 = Button(root,text='6',command = lambda: self.buttonAction('6'), width='4',height='4')
          b7 = Button(root,text='7',command = lambda: self.buttonAction('7'), width='4',height='4')
          b8 = Button(root,text='8',command = lambda: self.buttonAction('8'), width='4',height='4')
          b9 = Button(root,text='9',command = lambda: self.buttonAction('9'), width='4',height='4')

          blp = Button(root,text='(',command = lambda: self.buttonAction(')'), width='4',height='4')
          brp = Button(root,text=')',command = lambda: self.buttonAction('('), width='4',height='4')

          bplus  = Button(root,text='+',command = lambda: self.buttonAction('+'), width='4',height='4')
          bminus = Button(root,text='-',command = lambda: self.buttonAction('-'), width='4',height='4')

          bdivide = Button(root,text='/',command = lambda: self.buttonAction('/'), width='4',height='4')
          btimes = Button(root,text='*',command = lambda: self.buttonAction('*'), width='4',height='4')

          bcalc = Button(root,text='=',command = self.doCalcButton, width='6',height='4')
          bclear = Button(root,text='clear',command = self.doClearButton, width='6',height='4' )
          bdel = Button(root,text='del',command = self.doDelButton, width='6',height='4')

          lab.grid(row=0, column=0, columnspan=4)

          b0.grid(row=1,column=0) 
          b1.grid(row=1,column=1) 
          b2.grid(row=1,column=2) 
          b3.grid(row=1,column=3) 
          b4.grid(row=2,column=0) 
          b5.grid(row=2,column=1) 
          b6.grid(row=2,column=2) 
          b7.grid(row=2,column=3) 
          b8.grid(row=3,column=1)
          b9.grid(row=3,column=0)
          blp.grid(row=3,column=2)
          brp.grid(row=3,column=3)

          bplus.grid(row=4,column=0)
          bminus.grid(row=4,column=1)

          bdivide.grid(row=4,column=3)
          btimes.grid(row=4,column=2)

          bcalc.grid(row=5,column=1,columnspan=2)
          bclear.grid(row=5,column=0)
          bdel.grid(row=5,column=3)


      def buttonAction(self,s):

          self.labelString.set(self.labelString.get() + s)

      def doCalcButton(self):
          return 

      def doClearButton(self):
          self.labelString.set("")

      def doDelButton(self):
          self.labelString.set(self.labelString.get()[:-1])




if __name__ == "__main__":
   c = CalcGui()
   root.mainloop() 