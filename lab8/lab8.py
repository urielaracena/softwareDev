"""
Uriel Aracena
April 20, Python Introduction
"""

# single comment. this line will NOT run.

print ('\n ------ Example 1: string characters ------')
print ("\tGood morning! \nthis is my first \"Python\" code!")



print ('\n ------ Example 2: data type ------')
print (f"Data type of 3.56= {type (3.56)}")
print (f"Data type of -25 = {type(-25)}")
print (f"Data type of 'Hello World!' = {type ('Hello World!')}")
print (f"Data type of character '$' = {type('$')}")
print (f"Data type of False = {type(False)}")



print ('\n ------ Example 3: Variable ------')
# declare variables
number1=25.5
number2=-12
username="Peter Pan"
add_numbers = number1 + number2
is_raining = True

#Prompt results
print (f"{username}, the sum of {number1} and {number2} is {add_numbers}")
print (f"is it raining today? = {is_raining}")



print ('\n ------ Example 4: Assigning values to multiple variables ------')
#declare multiple variables
item1, item2, item3 = "apples", 25, False
print (f"item 1 = {item1}, item 2 = {item2}, item 3 = {item3}")

#declare multiple variables with the same value
score1 = score2 = score3 = 88
print (f"score 1 = {score1}, score 2 = {score2}, score 3 = {score3}")
 


print ('\n ------ Example 5: Input command ------')
print ("Enter username: ")
username = input()
print(f"Collected username = {username}")

# cast from string to integer
luckynumber = int(input("Enter a lucky number: "))
print (f"lucky number = {luckynumber}")

# double the lucky number. 
dblucky = luckynumber*2
print(f"Doubled of lucky = {dblucky}")

# cast integer (or float) to string
triplenumber = str(dblucky) * 3
print(f"tripled the casted number = {triplenumber}")

# cast integer to bool value
# 0 = False, any another number = True
completed_task = -20
print (f"completed task = {bool(completed_task)}")



print ('\n ------ Example 6: Arithmetic operators ------')
num1 = 25
num2 = 9

print (f"the sum of {num1} and {num2} is \t                  {num1 + num2}")
print (f"the different between {num1} and {num2} is \t       {num1 - num2}")
print (f"the product of {num1} and {num2} is \t              {num1 * num2}")
print (f"the quotient of {num1} and {num2} is \t             {num1 / num2}")
print (f"the modulus(remainder) of {num1} and {num2} is \t   {num1 % num2}")
print (f"the integer of quotient {num1} and {num2} is \t     {num1 // num2}")
print (f"the result of base {num2} to the power of 3 is \t   {num2**3}")



print ('\n ------ Example 7: Finding the hypotenuse  ------')
# declare and assign values
x = float(input("Enter side 1: "))
y = float(input("Enter side 2: "))

# calculate the hypotenuse
hyp = (x**2 + y**2)**0.5

# prompt result
print (f"the hypotenuse of {x:0.1f} and {y:0.1f} is {hyp:0.3f} ")



print ('\n ------ Example 8: Assignment operators  ------')
n = 20
print (f"number = {n}")

# assignment operator +
n +=3
print (f"number + 3 = {n}")

# assignment operator -
n -=4
print (f"updated - number = {n}")

# assignment operator *
n *= 2
print (f"updated * number = {n}")

# assignment operator /
n /= 3
print (f"updated / number = {n}")

# assignment operator //
n //= 2
print (f"updated // number = {n}")

# assignment operator **
n **= 2
print (f"updated ** number = {n}")

# assignment operator %
n %= 5
print (f"updated % number = {n}")



print ('\n ------ Example 9: Comparison operators  ------')
n1 = 10
n2 = 3
n3 = 7

compare1 = n1==n2
compare2 = n1==(n2+n3)
print (f"is n1 equal n2?                      {compare1}")
print (f"is n1 = n2+n3?                       {compare2}")
  
compare3 = n1>n2
compare4 = n2<=n3
print (f"is n1 greater than n2?               {compare3}")
print (f"is n2 less than or equal to n3?      {compare4}")



print ('\n ------ Example 10: String indexing  ------')
username = "peterpan123"

# positive index
print (f"the fifth character = {username[4]}")

# negative index
print (f"the fifth character = {username [-5]}")



print ('\n ------ Example 11: String slice  ------')
# slice from the beginning to the 4th character
print (f"slice from beginning to 4th character =                    {username[:4]}")

# slice from the beginning to the end
print (f"slice from the 7th character to the end =                  {username[6:]}")

# slice from the 3rd to the 8th
print (f"slice from 3rd to the 8th =                                {username[2:7]}")

# slice from the 4th to the 6th character using negative index
print (f"slice from 4th to the 6th character using negative index = {username[-8:-5]}")



print ('\n ------ Example 12: Total characters in a string (len) ------')
print (f"the username has = {len(username)} characters")



print ('\n ------ Example 13: strip () method ------')
username = "peterpan123" 
print (f"The username = {username}. End of username")

username = username.strip()
print (f"The username after method strip = {username}. End of username")



print ('\n ------ Example 14: upper and lower method ------')
username = username.lower()
print (f"The username after method lower = {username}. End of username")

username = username.upper()
print (f"The username after method upper = {username}. End of username")



print ('\n ------ Example 15: replace method ------')
username = username.replace('p','%')
print (f"The username after method replace = {username}. End of username")



print ('\n ------ Example 16: split method ------')
msg = "Introduction to Python programming! Today we are learning string methods."
print (f"Message = {msg}")
print (f"The message after split method  = {msg.split('!')}")



print ('\n ------ Example 17: find method ------')
#find the letter "p"
index_p = msg.find('P')
print (f"index of letter P is = {index_p}")

#find the second letter 'P'
sec_index_P = msg.find('p', (index_p +1))
print (f"next index of letter P is = {sec_index_P}")

#find a non-existing letter 'y'
index_y = msg.find('y')
print (f"the index of letter y is = {index_y}")



print ('\n ------ Example 18: in, not in statement ------')
# check if the word 'we' is in the msg string
answer_we = 'we' in msg
print (f"is the word 'we' in the 'msg' string? = {answer_we}")
answer_today = "Today" not in msg
print (f"is the word 'Today' not in the 'msg' string? = {answer_today}")



print ('\n ------ Example 19: list indexing ------')
colors = ['orange', 'red', 'olive']
numbers = [6, 20, -9, 5, -12]
mixedlist = [False, 20, 'peter', True, -9]
emptylist = []
print (f"colors list = {colors}")
print (f"numbers list = {numbers}")
print (f"emptylist list = {emptylist}")
print (f"mixedlist = {mixedlist}")

print (f" 2nd colors = {colors[1]}")
print (f" 1nd number = {numbers[0]}")
# print (f"3rd value = {emptylist[2]}") # can't return empty character

print (f"last color = {colors[-1]}")
print (f"3rd last number = {numbers[-3]}")



print ('\n ------ Example 20: + * operator on list ------')
new_color = colors[0] + colors[-1]
print (f"the new colore is = {new_color}")

new_word = colors[1] + numbers[2]
print (f"the new word is = {new_word}")   # data type error 



print ('\n ------ Example 21: remove item from list ------')
#remove the last color
colors.pop(-2)
print (f"colors after pop = {colors}")


print ('\n ------ Example 22: adding item to the list ------')
# add items to the end of the list colors
colors.append('pink')
print (f"colors list after append = {colors}")

# add a new list to a list
colors.append(['blue', 'green'])
print (f"colors list after append = {colors}")

# add multiple items to a list
colors.append('red', 'black') 
print (f"colors list after append = {colors}") # argument error



print ('\n ------ Example 23: sort method ------')
colors = ['orange', 'red', 'Olive']
print (f"colors list = {colors}")
colors.sort()
print (f"color list sorted = {colors}")

bool_list = [True, True, False]
bool_list.sort()
print (f"bool list sorted = {bool_list}")


print ('\n ------ Example 24: count method ------')
count_true = bool_list.count(True)
print (f"there is {count_true} True values")
count_red = colors.count('red')
print (f"there is {count_red} red colors")



print ('\n ------ Example 25: length of the list ------')
length_colors = len(colors)
print (f"there is {length_colors} colors")



print ('\n ------ Example 26: index of an item in a list ------')
index_olive = colors.index('olive')
print(f"the index color olive is {index_olive}")

#index_green = colors.index('green') #error
#print(f"the index color green is {index_green}") #error