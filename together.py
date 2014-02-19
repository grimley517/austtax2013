import tkinter as tk


class model():
    '''
    this is the model for the application.  

    It is here that the processing is done.
    '''
    
    def SalModes(self):
        Salary_Modes = controller.radops(self)
        return (Salary_Modes)
    def annualise(self, salary, frequency):
        '''
        This converts a salary paid annually, fortnightly, or weekly into an annual salary.
        
        Check that frequency is a number responding to th number of times a year that the salary is paid
        '''
        
        return (salary * frequency)
    
    def findtax (self, annualSal):
        ''' 
        This function takes an annual salary and returns the tax payable on it.
        '''
        if annualSal < 18200:
            return 0
        elif annualSal < 37000:
            return (0.18 * (annualSal-18200))
        elif annualSal < 80000:
            return (3572 + 0.325 *(annualSal - 37000))
        elif annualSal < 180000:
            return (17547 + 0.37 *(annualSal - 80000))
        else:
            return (54547 + 0.45 *(annualSal - 180000))
    def findMC(self, salary):
        '''
        This function returns the Medicare Levy for a given gross sallary
        '''
        return (0.015 * salary)
    
    def netpay(self, salary, freq):
        '''
        this returns the Nett pay over a defined period for a gross salary
        '''
        result = salary - (self.findtax(salary)+ self.findMC(salary))
        result = result / freq
        return (result)
    def modeword(self, freq):
        modes = self.SalModes()
        for mode in modes:
            if mode[1]== freq:
                modeword = mode[0]
        return modeword
    def outString (self, salary, infreq, outfreq):
        txtinfreq = self.modeword(infreq)
        ostr = "Your {infre} salary is {Salary}/n".format(infre = txtinfreq, Salary = salary)
        annSal = self.annualise(salary, infreq)
        if infreq != 1:
            ostr = ostr + "your annual Salary is therefore {annSal}/n".format(annSal = annSal)
        totsfreq = self.modeword(outfreq)
        tax = self.findtax(salary)
        medicare = self.findMC(salary)
        pay = (annSal - (tax + medicare))/outfreq
        ostr += '''You will pay {tax}  and {medicare} per [outfreq}/n 
        this will leave you with {pay} per {outfreq}.'''.format(tax =tax, medicare =medicare, outfreq = totsfreq, pay = pay)
class Application(tk.Frame):
    '''
    This is the  view for our application.

    This handles the bit the user can see.
    '''
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.salary = tk.StringVar()
        self.inFreq = tk.IntVar()
        self.outFreq = tk.IntVar()
        self.outString = tk.StringVar()
        self.pack()
        self.outString.set("")
        self.createWidgets()

    def createWidgets(self):
        self.frame1()
        self.frame2()
        self.frame3()
        self.frame4()

    def say_hi(self):
        print("hi there, everyone!")
    def salary (self):
        return self.salary.get()
    
    def frame1(self):
        '''
        frame 1 is the first frame of the 4  it contains the input lable and a textbox.
        '''
        self.f1 = tk.Frame(self)
        self.f1.pack(side = 'left', anchor = 'nw')#make and pack the Frame first
        self.inLbl = tk.Label(self.f1)#put the label in
        self.inLbl["text"]= "please enter your Salary"
        self.inLbl.pack()
        
        self.inTB = tk.Entry(self.f1, textvariable = self.salary, )#Put the text Box in
        self.inTB.pack()
        
        self.goBtn = tk.Button(self.f1, text = "go", width = 12)
        self.goBtn.pack()
        
        
    def frame2(self):
        '''
        frame 2 is the second frame.  it sits to the right of frame 1, 
        
        This frame contains the frequency for the salary.  
        ie whether the salary entered is annual, fornightly etc...
        '''
        
        self.f2 = tk.Frame(self)#again start with the frame
        self.f2.pack(side = 'left', anchor = 'ne')
        self.radops = controller.radops(self)
        radbtns = []
        #we're going to make a number of buttons, put them in a list as long as radops.
        for i in range(len(self.radops)):
            radbtn= tk.Radiobutton(self.f2, 
                                       variable = self.inFreq, 
                                       value = self.radops[i][1], 
                                       text = self.radops[i][0]).pack(anchor = 'w')
            radbtns.append(radbtn)
    def frame3(self):
        ''' Frame 3 is the frame which contains the output frequency'''
        self.f3=tk.Frame(self)
        self.f3.pack(side = "bottom")
        radbtns = []
        #we're going to make a number of buttons, put them in a list as long as radops.
        for i in range(len(self.radops)):
            radbtn= tk.Radiobutton(self.f3, 
                                       variable = self.outFreq, 
                                       value = self.radops[i][1], 
                                       text = self.radops[i][0]).pack(anchor = 'w')
            radbtns.append(radbtn)
    def frame4(self):
        ''' Frame 4 contains the output text'''
        self.f4=tk.Frame(self)
        self.f4.pack(side = "bottom")
        self.outLbl = tk.Label(self.f4, text = self.outString)
        self.outLbl.pack()
        
    def answer(self, outStr):
        self.f4.destroy()
        self.outString.set(outStr)
        self.frame4()
class controller():
    '''
    This is the controller for our application.

    This handles the whole program and links the view with the model.
    
    Remember the view and model can't see or understand eachother, 
    the controller does the linking.
    '''

    def __init__(self, root):
        
        self.window = Application(root)
        self.window.mainloop()
        #This loads the View from the View Controller
        #Application is the views name for its own class
        self.brain = model()
        #this loads the model from the model
        #window and brain now are variables which 
        #act to controll and send information to 
        #the different parts of the program
        self.window.goBtn.config(command = self.goBtnPressed)
    def goBtnPressed(self):
        sal = self.window.salary
        infreq = self.window.inFreq
        outfreq = self.window.outFreq
        self.window.outString.set(self.brain.outString(sal, infreq, outfreq))
        print(self.window.outstring)
    def radops(self):
        radopsList = [("Annual", 1 ), ("Fortnightly",26), ("weekly", 52) ]
        return radopsList

root = tk.Tk()
app = controller(root)
#root.mainloop()

