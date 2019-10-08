# Class to perform calculations
class FutureCalc():
    
    def __init__(self,r=1,n=1):
        self.r = r
        self.n = n
        
    def first_option(self,principal):
        result = principal *((1+self.r)**self.n)
        return result
    
    def second_option(self,annuity):
        result = annuity*((((1+self.r)**self.n)-1)/self.r)
        return result
    
    def third_option(self,annuity):
        result = annuity*((((1+self.r)**self.n)-1)/self.r)*(1+self.r)
        return result
    
    def fourth_option(self,name):
        return ("Thank you to use {} future calculation system!".format(name))
    
#Function to check if the option selected is between 1 and 4
def selection_check(selection):
    return selection in range(1,4)

#Function to do the calculation if the nnumber is selected between 1 and 3
def calc(selection):
    if selection == 1:
        r = float(input("Enter the interest rate: "))
        n =float(input("Enter the period: "))
        principal = float(input("Enter the original principal: "))
        mycalc = FutureCalc(r,n)
        print (mycalc.first_option(principal))
    elif selection == 2:
        r = float(input("Enter the interest rate: "))
        n =float(input("Enter the period: "))
        annuity = float(input("Enter the annuity amount: "))
        mycalc = FutureCalc(r,n)
        print (mycalc.second_option(annuity))
    elif selection == 3:
        r = float(input("Enter the interest rate: "))
        n =float(input("Enter the period: "))
        annuity = float(input("Enter the annuity amount: "))
        mycalc = FutureCalc(r,n)
        print (mycalc.third_option(annuity))

#Function to exit if 4 is selected
def exit_calc(name):
    mycalc = FutureCalc()
    print (mycalc.fourth_option(name))
    
#Loops to check conditions
def result(name):
    cont = True
    cont1 = True
    
    while cont is True:
        while cont1 is True:
            selection = int(input("Select a number: "))
            if selection_check(selection):
                calc(selection)
            elif selection == 4:
                exit_calc(name)
                cont1 = False
                break
            cont = False
    else:
        cont = True

#Main Code
name = input(" Welcome to the Future Calculator system! Please enter you name: ")
result(name)
     