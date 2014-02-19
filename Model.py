'''
this is the model for the application.  

It is here that the processing is done.
'''



class model():
    def SalModes(self):
        Salary_Modes = [("Annually", 1), ("Fortnightly",26), ("weekly", 52) ]
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