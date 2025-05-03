"""
Uriel Aracena
April 24, Conditional Statements
"""

print('\n ------ Example 1 and 2: if and else statement ------')
age = 20
agecode = 123

if age >= 21:
    print("You are an adult!")
    agecode = 200
else:
    print("You are under 21!")
    agecode = 100

print(f"After the 'if' statement, agecode = {agecode}")


print('\n ------ Example 3: multiple statement ------')
age = 20
if 0 <= age < 21:
    print("You are minor")
elif 21 <= age < 65:
    print("You are an adult")
elif 65 <= age <= 130:
    print("You are a senior")
else:
    print("Unable to read age")


print('\n ------ Example 4: and operator ------')
temp = 80
humi = 100

if 70 <= temp <= 90 and humi < 80:
    print("The weather is pleasant")
else:
    print("The weather is not ideal")


print('\n ------ Example 5: or operator ------')
day = "Monday"
is_holiday = False

if day == "Saturday" or day == "Sunday" or is_holiday:
    print("You can relax today")
else:
    print("It is a workday")


print('\n ------ Example 6: nested conditional statement ------')
try:
    number = int(input("Enter a number: "))
    if number >= 0:
        if number == 0:
            print("The number is zero")
        else:
            print(f"{number} is positive")
    else:
        print(f"{number} is negative")
except ValueError:
    print("Invalid input. Please enter a valid integer.")


print('\n ------ Example 7: username validation  ------')
# Username validation. Username must have 3+ characters
username = input("Enter a username: ")
username = username.strip()
len_username = len(username)

if len_username >= 3:
    print(f"{username} has 3+ characters")
    index_whitespace = username.find(" ")
    if index_whitespace == -1:
        print(f"{username} is valid")
    else:
        print(f"Username cannot have whitespace")
else:
    print(f"{username} is invalid. Username must have 3+ characters")


print('\n ------ Example 8: match-case statement   ------')
response_code = 400

match response_code:
    case 400:
        print(f"Code = {response_code}. Server cannot understand")
    case 401 | 403:
        print(f"Code = {response_code}. Server refused to send back")
    case 404:
        print(f"Code = {response_code}. Server can't find")
    case _:
        print("Invalid code")


# Lab9 Exercise
print('\n ------ Lab9 Exercise   ------')

try:
    grade1 = float(input("Enter first grade: "))
    grade2 = float(input("Enter second grade: "))
    
    # Basic validation for grades
    if not (0 <= grade1 <= 100) or not (0 <= grade2 <= 100):
        print("Invalid grades. Grades must be between 0 and 100.")
    else:
        average = (grade1 + grade2) / 2
        
        if 90 <= average <= 100:
            GPA = "A"
        elif 70 <= average < 90:
            GPA = "B"
        elif 60 <= average < 70:
            GPA = "C"
        elif 0 <= average < 60:
            GPA = "FAIL!"
        else:
            GPA = "UNDEFINED!"
            print("GPA = UNDEFINED!")
            
        print(f"For the average of {average:.2f}, your GPA is {GPA}")
        
except ValueError:
    print("Invalid input. Please enter valid numerical grades.")