''' Uriel Aracena April 27, Functions '''
import math

# ex3
def greeting():
    print("Welcome to functions!")

# ex4 f() with parameter 'username'
def printusername(username):
    print(f"Welcome to functions {username}")

# ex5 f() with default parameters
def user_country(username="(unknown)", country='unknown country'):
    print(f"{username} is living in {country}")

# ex6 f() that returns a value (product)
def product(n1, n2):
    return n1 * n2

# ex7 boolean f() that checks if a # is a multiple
def multiple3(n):
    if n % 3 == 0 and n != 0:
        return True
    else:
        return False

# ex8 composition f() (collect, validate, return a #)
def collectnum():
    n = float(input("Enter a number between 1 and 9 (inclusive): "))
    # validate numb
    while not(1 <= n <= 9):
        n = float(input("Re-enter a number again: "))
    return n

# f() that adds 'totalnumbers' amount of numbers and returns the sum of the numbers
def sumnumbers(totalnumbers):
    sum = 0
    for n in range(totalnumbers):
        sum += collectnum()  # composition f()
    return sum

# f() to print result
def printresult(totalsum):
    print(f"Sum of all numbers is = {totalsum}")

# ex9 built-in f() (calc and rtn area of a circle)
# formula = radius^2 * pi
def areacircle(radius):
    a = math.pow(radius, 2) * math.pi
    return round(a, 2)

# f() to print result
def areaprint(area, radius):
    print(f"The area of a circle with {radius} radius is {area}")

# ex10 try-except
# f() that returns a ratio (hours)
def ratio_hour(hour):
    try:
        dayhour = 24
        r = hour / dayhour
    except ZeroDivisionError:
        print("undefined")
        print("Number can't be divided by 0")
        return 0
    except ValueError:
        print("undefined")
        print("Number was not provided")
        return 0
    except:
        print("undefined")
        print("There was an error in the division")
        return 0
    else:
        print("defined")
        return r
    finally:
        print("------Process completed-------")

# ex11 classes
# defining a class name 'Myclass'
class Myclass:
    # property (attribute)
    id = 12345
    
    # method (func.)
    def msg(self):
        return "Welcome to Python Classes"

# ex12 __init__
class Complexnumber:
    # instantiating class
    def __init__(self, realnumber, imgnumber):
        self.r = realnumber
        self.i = imgnumber

# ex13
class Car:
    # init of the class
    def __init__(self, make, model, year):
        self.carmake = make
        self.carmodel = model
        self.caryear = year
    
    # set property 'odometer'
    odometer_reading = 0
    
    # method to return descriptive of the car
    def get_car_descripition(self):
        return f"{self.carmake} with model {self.carmodel} was made on {self.caryear}"
    
    # method to read odometer
    def read_odometer(self):
        return f"This car has {self.odometer_reading} miles on it"
    
    # method to update odometer
    def update_odometer(self, mileage):
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Odometer cant roll back")
    
    # method to add miles to odometer
    def increment_odometer(self, miles):
        if miles > 0:
            self.odometer_reading += miles
        else:
            print("Cant add negative miles")