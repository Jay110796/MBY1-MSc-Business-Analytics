# MS5114 - Advanced Programming for Business Analytics
# Individual Assignment No : 2
# Student Name : Jayakarthi Boovendran
# Student ID: 19230487

#####################################################################################################################
#####################################################################################################################


# 1. Answer the following questions.

# What is a class?
print('1. OOPs Concepts in Python')
print('Class:')
print(' - A Class is a representation of an "Entity" or Object.')
print(' - In simple terms, a class is a template that defines the attributes (properties) and functionalities of an object (entity)')
print(' - For instance,  consider a "Pen" as the entity here. The class Pen will have attributes like colour,modelnumber and company.')
print(' - Where, the methods would be "write(),scratch(),break().."')


# What is an instance?
print('')
print('Instance:')
print(' - An instance is an object that belongs to a Class. Or, An "Object" is an unique instance to a class')
print(' - These objects can access the attributes and methods of the class to which they belong')
print(' - For instance, "ball-point" is an object to the Class Pen')

# What is encapsulation?
print('')
print('Encapsulation:')
print(' - The process of binding together the data and functions into a single entity is called Encapsulation.')
print(' - The primary objective of encapsulation is to enable data hiding and abstraction.')

# What is inheritance?
print('')
print('Inheritance:')
print(' - Inheritance is mechanism by which a class can inherit or extend the properties from another class')
print(" - Inheritance enables 'reusability' of a class's properties and methods")

# What is multiple inheritance?
print('')
print('Multiple Inheritance:')
print(' - Muliple Inheritance is a mechanism by which a class inherits propeties from more than one base class or parent class')


# What is polymorphism?
print('')
print('Polymorphism:')
print(' - Polymorphism is the ability to redefine the same methods for derived classes')
print(' - It facilitates loose coupling and flexibility as the same interface is used for different objects,data-types or classes')


#####################################################################################################################
#####################################################################################################################

# 2. Rectangle class
# Write a Python class named Rectangle constructed by a length and width and a method which will compute the area
# of a rectangle.

class Rectangle(object):
   def __init__(self,length,width):         #Constructor - initializes the class attributes 'length' and 'width'
       self.length=length
       self.width=width
   def compute_area(self):                  #Method to compute area of the rectangle using the initialised attributes
       return (self.length*self.width)
   pass

#####################################################################################################################
#####################################################################################################################
# 3. Person class
# Rewrite the Person class below so that a person’s age is calculated for the first time when a new person instance is
# created, and recalculated (when it is requested) if the day has changed since the last time that it was calculated.

import datetime  # we will use this for date objects

class Person:

    def __init__(self, name, surname, birthdate, address, telephone, email): #Constructor that initialises attributes of the class (Person's details)
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.address = address
        self.telephone = telephone
        self.email = email
        self.last_Compute_age=''                                    # Initialy 'age' is set empty
        self.last_Computed_On=datetime.date(1970, 1, 1)             # last_Computed_On is initialised to 1/1/1970 (i.e, any date other than today's)
            
    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year
        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1                                                # Computes value for age
        self.last_Compute_age=age                                       
        self.last_Computed_On=today                                 # Stores the computed age to last_Compute_age
        return self.last_Compute_age                                # Stores the computed date to last_Compute_on

    
    def compute_age(self):                                          # Method that checks if 'age' needs to be calculated newly 
        if datetime.date.today()>self.last_Computed_On:             # If last_Compute_on date is expired (i.e, not today)
            if self.last_Computed_On==datetime.date(1970, 1, 1):
                print(' - Calculating Age for the first time')
            else:
                print(' - Initiating Recalculation! Last Computed on :'+self.last_Computed_On.strftime('%m/%d/%Y'))
            return self.age();                                      # Recalculates age
        else:
            print(' - Returning previously computed age!')
            return self.last_Compute_age                            # Returns previously stored value of last_Compute_age



    def setlastComputedDate(self):     # For testing purpose,setlastComputedDate() sets the last_Compute_on date to yesterday's date
        yesterday = datetime.date.today() - datetime.timedelta(days = 1) # That is last_Compute_on is made to expire on purpose
        self.last_Computed_On=yesterday
        print(' - Setting last_Computed_On date to: '+self.last_Computed_On.strftime('%m/%d/%Y')) #so that age is recalculated.


#####################################################################################################################
#####################################################################################################################

# 4. Deck class
# Create a deck of cards class. Internally, the deck of cards should use another class, a card class. Your requirements are:
# The Deck class should have a deal method to deal a single card from the deck
# After a card is dealt, it is removed from the deck.
# There should be a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them
# randomly.
# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)

import random
class Card:
    def Create_Cards(self):                                                 #Method to create deck of 52 cards
        self.Suits={'Hearts', 'Diamonds', 'Clubs', 'Spades'}
        self.Values={'A','2','3','4','5','6','7','8','9','10','J','Q','K'}
        self.Cards=list()
        for suit in self.Suits:
            for value in self.Values:
                self.Cards.append(str(suit+'-'+value))
        return self.Cards                                                   #Returns the deck of cards
    pass

class Deck:
    def __init__(self):
        self.Cards=Card.Create_Cards(self)                      # Calls Create_Cards() method of 'Card' class and assigns back the returned deck of cards
        self.DealtCards=[]

    def deal(self):
        Chosen_card = random.choice(self.Cards)  # To randomly choose a single card from the deck
        self.Cards.remove(Chosen_card)           # Removes the choosen card from the deck
        self.DealtCards.append(Chosen_card)      # adds to dealt card to the 'DealtCards' list so that it can be assigned back on shuffle
        print(' - '+Chosen_card+' has been delt with! | Total No. of Cards:'+str(len(self.Cards)))

    def Shuffle(self):
        #self.Cards=Card.Create_Cards(self)
        for card in self.DealtCards:             # Assigns the dealt cards back to the deck
            self.Cards.append(card)
        print(' - Shuffling Cards..')
        random.shuffle(self.Cards)               #shuffles the deck
        print(' - Total No. of Cards after shuffling:'+str(len(self.Cards)))
        return self.Cards
    pass


#####################################################################################################################
#####################################################################################################################

# 5. Inheritance
# From the class Employee below create:


class Employee:
    def __init__(self, id_employee, name):
        self.id_employee = id_employee
        self.name = name


# a. a class SalaryEmployee that inherits from Employee adding a weekly_salary as an initiation attribute
# together with id, name
# For example: the construction of an object of the class SalaryEmployee will be like:
# salary_Andy = SalaryEmployee(1, 'Andy Smith', 500)
# id_employee, name, weekly_salary
# create a calculate_payroll method that returns the payment (i.e. weekly salary value)

class SalaryEmployee(Employee): # class SalaryEmployee inherits the properties of class Employee
    def __init__(self,Employee, weekly_salary):   
        self.id_employee=Employee.id_employee
        self.name=Employee.name
        self.weekly_salary=weekly_salary
        pass

    def calculate_payroll(self): # method that returns weekly salary 
        return self.weekly_salary
        pass


# b. a class HourlyEmployee
# the objective of this class if to calculate the payroll based in two attributes: hours_worked and hour_rate
# to that, this class will inherit from Employee and receive the as attribute the values hours_worked and hour_rate
# OBS: you need to create a calculate_payroll method for this class that takes into consideration the hours_worked and
# hour_rate to calculate the payment
class HourlyEmployee(Employee): # class HourlyEmployee inherits the properties of class Employee
    def __init__(self,Employee,hours_worked , hourly_rate ):  #Constructor to initialise the attributes of the class
        self.id = Employee.id_employee
        self.name = Employee.name
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
        pass
    
    def calculate_payroll(self): # method to calculate salary based on hourly rate and hours worked
        return self.hours_worked * self.hourly_rate
    pass


# c. a class CommissionEmployee
# the objective of this class if to calculate the payroll based in two attributes: weekly_salary and commission
# to that, this class will inherit from other class (which one do you think would be more appropriate?)
# and receive the values of weekly_salary and commission.
# OBS: you need to create a calculate_payroll method for this class that takes into consideration weekly_salary and
# commission to calculate the payment
class CommissionEmployee(SalaryEmployee): # class CommissionEmployee inherits the properties of class SalaryEmployee
    def __init__(self,SalaryEmployee, commission):
        self.weekly_salary = SalaryEmployee.weekly_salary
        self.commission = commission

    def calculate_payroll(self):  # method to calculate weekly salary with commission of the employee
        return self.weekly_salary + self.commission
    pass


# 6. polymorphism
# Create/cite an example of Polymorphism in Python

class Square:                             #Square class with calculate_area() method , takes on side as a parameter
    def __init__(self,side):
        self.side=side
         
    def calculate_area(self):
        return self.side * self.side

class Triangle:                           #Triangle class with calculate_area() method, same as the Square class
    def __init__(self,base,height):       #But takes in 2 arguments base and height
        self.base=base
        self.height=height
    
    def calculate_area(self):
        return 0.5 * self.base * self.height

#####################################################################################################################
#####################################################################################################################

if __name__ == '__main__':

    print('')
    print('2. Area of Rectangle:')
    length = float(input(" - Enter the length of Rectangle : "))                 # Reads value for length from user
    width = float(input(" - Enter the width of Rectangle : "))                   # Reads value for width from user
    rect = Rectangle(length,width)                                               # 'rect' - Object to the class Rectangle is declared and the values of 'length' and 'width' is assigned to the class attributes through a constructor
    print(" - Area of the Rectangle is :"+str(rect.compute_area())+" sq.units")  # The computed_area() method is invoked to calculate the area of the rectangle, the same is printed to the user
    print('')

    
    print('3. Age Calculator:')
    person = Person("Jay","Booven",datetime.date(1996, 7, 11),"Knocknacarra, Galway","0894970170","j.boovendran1@nuigalway.ie")  # Instantiation of Person Class 
    print(' - Computing Age...')
    print(' - Age:'+str(person.compute_age())) #Calls compute_age() method and prints the age
    print(' - Computing Age again...')
    print(' - Age:'+str(person.compute_age())) #Prints previously calculated value of age (i.e, age is not computed again)
    person.setlastComputedDate()               #For testing purpose, the last_Computed_date is modified
    print(' - Computing Age again...')
    print(' - Age:'+str(person.compute_age())) #Recalculates age as the last_computed_date is not today



    print('')
    print('4. Deck of  Cards:')
    deck=Deck();                        #Initialises the deck with Create_cards() method from Cards Class
    print(' - Picking a card...')
    deck.deal()                         #Ransdomly picks a cards and removes it from the deck
    print(' - Picking another card...')
    deck.deal()
    deck.Shuffle()                      #Shuffling the deck
    print(' - Picking a card after shuffle...')
    deck.deal()

    print('')
    print('5. Employee Pay Info:')
    employee=Employee('19230487','Jay');  #Initialising Employee Object
    salary = SalaryEmployee(employee,400); # Initialising SalaryEmployee Class by passing 'employee' object
    print('   Employee ID: '+salary.id_employee+' | Employee Name: '+salary.name);
    print(' - Weekly Salary (EUR)      : '+str(salary.calculate_payroll()))
    hourly_salary = HourlyEmployee(salary, 40, 10)   #Initialising HourlyEmployee Class by passing 'salary' object
    print(' - Pay @ hourly_rate (EUR)  : '+str(hourly_salary.calculate_payroll())+' [hours worked : '+str(hourly_salary.hours_worked)+' @'+str(hourly_salary.hourly_rate)+' EUR /hr]')
    c_salary =CommissionEmployee(salary,40)        #Initialising CommissionEmployee Class with 'salary' object
    print(' - Pay with commission (EUR): '+str(c_salary.calculate_payroll()))
    
    
    print('')
    print('6. Area Calculation using Polymorphism')
    square = Square(5)                               #Initialising Square Class
    triangle = Triangle(5,4)                         #Initialising Triangle Class
    print(" - Area of Square   : "+str(square.calculate_area())+' sq.units') # Invoking calculate_area() of both objects
    print(" - Area of Triangle : "+str(triangle.calculate_area())+' sq.units')

    pass
