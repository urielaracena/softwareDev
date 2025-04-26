"""
Uriel Aracena
April 24, Conditional Statments
"""

print ('\n ------ Example 1 and 2: if and else statement ------')
age = 20
agecode = 123

if age>=21:
    print("you are an adult!")
    agecode = 200
else:
    print("you are under 21!")
    agecode = 100

print(f"after the 'if' statement, agecode = {agecode}")



print ('\n ------ Example 3: multiple statement ------')
age = 20
if 0<= age < 21:
    print("You are minor")
elif 21<= age < 65:
    print("You are an adult")
elif 65<= age <= 130:
    print("You are a senior")
else:
    print("Unable to read age")



print ('\n ------ Example 4: and operator ------')

temp = 80
humi = 100

if 70<= temp <=90 and humi <80:
    print("the weather is pleasant")
else:
    print("the weather is not ideal")



print ('\n ------ Example 5: or operator ------')
day = "Monday"
is_holiday = False

if day == "Saturday" or day == "Sunday" or is_holiday:
    print("you can relax today")
else:
    print("it is a workday")



print ('\n ------ Example 6: nested conditional statement ------')
number = int(input("enter a number:"))
if number>=0:
    if number==0:
        print("the number is zero")

    else:
        print(f"{number} is positive")
else:
    print(f"{number} is negative")


print ('\n ------ Example 7: username validation  ------')
#username validation. username must have 3+ characters

username = input("Enter a username: ")
username = username.strip()
len_username = len(username)

if len_username >= 3:
    print (f"{username} has 3+ characters")
    index_whitespace = username.find(" ")
    if index_whitespace == -1:
        print(f"{username} is valid")
    else:
        print (f"username cannot have whitespace")
else:
    print(f"{username} is invalid. user name must have 3+ characters")



print ('\n ------ Example 8: match-case statement   ------')
response_code = 400

match response_code:
    case 400:
        print (f"code = {response_code}. server cannot understand")
    case 401 | 403:
        print (f"code = {response_code}. server refused to send back")
    case 404:
        print (f"code = {response_code}. server can't find")
    case _ :
        print ("invalid code")



#Lab9 Exercise
print ('\n ------ Lab9 Exercise   ------')

grade1 = float(input("Enter first grade: "))
grade2 = float(input("Enter second grade: "))

average = (grade1 + grade2) / 2

if 90 <= average <= 100:
    GPA = "A"

elif 70 <= average <= 89.99:
    GPA = "B"

elif 60 <= average <= 69.99:
    GPA = "C"

elif 0 <= average <= 59.99:
    GPA = "FAIL!"

else:
    print ("GPA = UNDEFINED!")

print (f"For the average of {average}, your GPA is {GPA}")