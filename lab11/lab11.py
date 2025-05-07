'''
Uriel Aracena
April 27, Python applications
'''
from lab11_functions import *
import math

print("\n------- Example 1: Python dictionary -------")
# create a dictionary
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
# print a complete dictionary
print(car)
# to access items in a dictionary we use [], where [] goes the key's name
print(f"The year of the car is = {car['year']}")
# update the value of the key
car["year"] = 1980
print(f"The year of the car was updated to = {car['year']}")
print("The year of the car was updated to = ", car["year"])
# add key:value pair
car['color'] = 'red'
print(car)
print("\nLoop through each key in the dictionary")
for k in car:
    print(k)
print("\nLoop through each value in the dictionary")
for k in car:
    print(car[k])
print("\nLoop through each pair in the dictionary")
for k in car:
    print(f"{k} has value = {car[k]}")

print("\n------- Example 2: Python dictionary application -------")
# given the following list, create a dictionary that will count the number of times that a word appears in the string.
# create a dictionary that will organize the words as the keys, and the number of occurrence of the word as the value of the key.
phrase = "to be or not to be"
print(f"original phrase = {phrase}")
# create the dictionary
word_count_dict = {}
phrase_split = phrase.split()
print(f"splitted phrase = {phrase_split}")
# loop to each word in the list
for word in phrase_split:
    if word in word_count_dict:
        word_count_dict[word] += 1
    else:
        word_count_dict[word] = 1
# print result
print("Result of dictionary: ")
for w in word_count_dict:
    print(f"'{w}' = {word_count_dict[w]}")

print("\n------- Example 3: Function that doesnt return values -------")
# call functions 'greeting'
greeting()

print("\n------- Example 4: Function with parameters -------")
# call f() 'printusername'
printusername('name')

print("\n------- Example 5: Function with default parameters -------")
# call f() 'printusername'
user_country("Martha", "Chile")
user_country("Anna")
user_country("", "France")

print("\n------- Example 6: Function with return value -------")
# call f() 'product'
num1 = 2
num2 = -6
prod1 = product(num1, num2)
print(f"The product of {num1} and {num2} is = {prod1}")
# Adding correct example:
prod2 = product(3, 5)
print(f"The product of 3 and 5 is = {prod2}")

print("\n------- Example 7: Boolean function-------")
# call f() 'multiple3'
checknum1 = multiple3(num1)
checknum2 = multiple3(num2)
print(f"Is {num1} multiple of 3? {checknum1}")
print(f"Is {num2} multiple of 3? {checknum2}")

print("\n------- Example 8: Composition function -------")
# MODIFIED: Instead of using user input, we'll use predefined values
def mock_sumnumbers(count):
    """Simulate sumnumbers function without requiring input"""
    sum = 0
    for i in range(count):
        # Using predefined values 3, 5, 7 instead of asking for input
        sample_values = [3, 5, 7]
        value = sample_values[i % len(sample_values)]
        print(f"Using value: {value} (predefined for testing)")
        sum += value
    return sum

# Use mock function instead of the original
sumall = mock_sumnumbers(3)
printresult(sumall)

print("\n------- Example 9: Built-in function -------")
r = 2
a = areacircle(r)
areaprint(a, r)

print("\n------- Example 10: Try-except -------")
r1 = ratio_hour(0)
r2 = ratio_hour(3)
# r3 = ratio_hour("Peter")  # This will cause a ValueError

print("\n------- Example 11: Classes -------")
# create an instance of the class
user1 = Myclass()
print(f"An instance of the class = {user1}")
# call the class' property
user1id = user1.id
print(f"user 1 id = {user1id}")
# call the class' method
user1msg = user1.msg()
print(f"user 1 message = {user1msg}")

print("\n------- Example 12: Instantiation of classes -------")
# create an instance of the class
paircomplexnumber = Complexnumber(2, 3)
# call the instance object 'r' of the class
real = paircomplexnumber.r
print(f"The real part is {real}")

print("\n------- Example 13: Classes application-------")
# create an instance of the class
car1 = Car("Tesla", "S", "2023")
# call property 'odometer_reading'
car_reading = car1.odometer_reading
print(f"Car miles reading = {car_reading}")
# call method 'get_car_descripition'
print(car1.get_car_descripition())
# call method 'read_odometer'
print(car1.read_odometer())
# update the odometer to mileage = 10
car1.update_odometer(10)
print(car1.read_odometer())
car1.update_odometer(5)
print(car1.read_odometer())
# add 20 miles to the odometer
car1.increment_odometer(20)
print(car1.read_odometer())
car1.increment_odometer(-5)
print(car1.read_odometer())
car1.increment_odometer(8)
print(car1.read_odometer())

"""
Uriel Aracena
Lab 11 Exercise, Class' in Python (extra points)
"""

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grade = {}
    
    def add_grade(self, subject, grade):
        self.grade[subject] = float(grade)
        print(f"Added {subject} grade: {grade}")
    
    def get_average_grade(self):
        if len(self.grade) == 0:
            return 0.0
        
        total = 0
        for subject in self.grade:
            total += self.grade[subject]
        
        return total / len(self.grade)

print("\n----- Testing Student Class -----")

# Create first student
student1 = Student("John Smith", 20)
print(f"Student created: {student1.name}, {student1.age} years old")

# Adding grades
student1.add_grade("Math", 85)
student1.add_grade("Science", 90.5)
student1.add_grade("English", 78)

# Print grades
print(f"\n{student1.name}'s grades:")
for subject in student1.grade:
    print(f"{subject}: {student1.grade[subject]}")

# Get average
avg = student1.get_average_grade()
print(f"\nAverage grade: {avg:.1f}")

# Create second student
student2 = Student("Maria Garcia", 19)
print(f"\nStudent created: {student2.name}, {student2.age} years old")

# Adding different grades
student2.add_grade("Math", 92)
student2.add_grade("Physics", 88)
student2.add_grade("Computer Science", 95)
student2.add_grade("History", 79.5)

# Print grades
print(f"\n{student2.name}'s grades:")
for subject in student2.grade:
    print(f"{subject}: {student2.grade[subject]}")

# Get average
avg2 = student2.get_average_grade()
print(f"\nAverage grade: {avg2:.1f}")

# Testing empty grades case
student3 = Student("Alex Brown", 21)
print(f"\nStudent created: {student3.name}, {student3.age} years old")
print(f"Average with no grades: {student3.get_average_grade()}")