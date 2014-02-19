'''
This is the controller for oyur application.

This handles the whole program and links teh view with the model.
PS Sorry I have really bunged up ears today and can't hear much.  
Please email me questions!
'''

import View as view
import Model as model
class controller():
    def __init__(self):
        
        self.window = view.Application(self)
        self.window.mainloop()
        #This loads the View from the View Controller
        #Application is teh views name for its own class
        self.brain = model.model()
        #this loads the model from the model
        #window and brain now are variables which 
        #act to controll and send information to 
        #teh different parts of teh program
    def goBtnPressed(self):
        sal = self.window.salary
        freq = self.window.inFreq
        annual = self.brain.annualise(sal, freq)
        self.window.outString = str(annual)
    def radops():
        radopsList = self.brain.SalModes()
        return radopsList
app = controller()