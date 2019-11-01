# pythin -E test.py
import datetime

x = datetime.datetime.now()
print(x)

print("Hello")

name = "unknown"

def welcomePlayer():
  global name
  name = "ben"
  print("Are you " + name + "?")
  
welcomePlayer()


str = "ghyBEN"
print(str.lower())
print(str.upper())

print(str.replace("g", "J"))

print(str)

def myFunc(number):
  return lambda b : b * number


myDoubler = myFunc(2)
myTripler = myFunc(3)

print(myDoubler(8))
print(myTripler(11))
print(myTripler(10))
 
 
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)
 
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.welcome()



username = input("Enter username:")
print("Username is: " + username)




if "BEN" == username.upper() :
  print("Awesome name!")