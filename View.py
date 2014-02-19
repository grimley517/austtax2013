

import tkinter as tk
import Controller as ctrl

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
	
	@classmethod
	def goBtnPressed(self):
		super.goBtnPressed(self)
	
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
		
		self.goBtn = tk.Button(self.f1, 
							Text = 'go', 
							command=self.goBtnPressed())
		self.goBtn.pack()
		
	def frame2(self):
		'''
		frame 2 is the second frame.  it sits to the right of frame 1, 
		
		This frame contains the frequency for the salary.  
		ie whether the salary entered is annual, fornightly etc...
		'''
		
		self.f2 = tk.Frame(self)#again start with the frame
		self.f2.pack(side = 'left', anchor = 'ne')
		self.radops = ctrl.controller.radops(self)
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
	def frame4(self):
		''' Frame 4 contains the output text'''
		
#root = tk.Tk()
#app = Application(master=root)
#app.mainloop()