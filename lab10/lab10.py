""" Uriel Aracena April 25, Loops """

print('\n ------ Example 1: for loop as a counter  ------')
# print hello from 0 to 4
for x in range(0, 5):
    print(f"Hello = {x}")

print('\n ------ Example 2: for loop in a list  ------')
fruits = ['apples', 'oranges', 'kiwis', 'pineapple']
for eachfruitindex in range(0, len(fruits)):
    print(f"fruit with index {eachfruitindex} = {fruits[eachfruitindex]}")

for eachfruit in fruits:
    print(eachfruit)

print('\n ------ Example 3: for loop with different increment  ------')
for num in range(2, 30, 3):
    print(num)

print('\n ------ Example 4: for loop with different decrement  ------')
for num in range(10, 0, -2):
    print(num)

print('\n ------ Example 5: for loop through a string  ------')
username = "yes123"
for x in username:
    print(x)

print('\n ------ Example 6: nested conditional statement  ------')
# for loop to check how many negative numbers are in the list
numbers = [5, -2, 0, 8, 9, -1]
x = 0
for eachnumber in numbers:
    if eachnumber < 0:
        x += 1

print(f"There is {x} negative numbers")

print('\n ------ Example 7: nested conditional statement: operation  ------')
# for loop to add odd numbers
sumodd = 0
for eachnumber in numbers:
    if eachnumber % 2 != 0:  # This correctly identifies all odd numbers (positive and negative)
        sumodd += eachnumber

print(f"The sum of all odd numbers is = {sumodd}")

print('\n ------ Example 8: break statement in a loop  ------')
# for loop to print from 0 to 10, and terminate the loop when it reaches to 5
for n in range(0, 10):
    if n == 5:
        print('counter reaches to 5')
        break
    else:
        print(n)

print('\n ------ Example 9: continue statement in a loop  ------')
# for loop to add numbers from 0 to 10, except number 5
sumall = 0
for n in range(10):
    if n == 5:
        continue
    
    sumall += n
    print(n)
    print(f"\tsum = {sumall}")

print('\n ------ Example 10: else statement in a for loop  ------')
for n in range(6):
    if (n == 3):
        break
    print(n)
else:
    print("loop completed!")

print('\n ------ Example 11: while loop as a counter  ------')
n = 0
while n < 6:
    print(n)
    n += 1

print('\n ------ Example 12: while loop as a checkpoint  ------')
sum1 = 0
while (True):
    try:
        number_input = input("Enter a number between -5 and 5 (or 'q' to quit): ")
        
        # Allow the user to exit the loop by typing 'q'
        if number_input.lower() == 'q':
            break
            
        number = int(number_input)
        if number < -5 or number > 5:   # if not (-5 <= number <= 5)
            print("Number out of range, exiting loop.")
            break
        sum1 += number
    except ValueError:
        print("Invalid input. Please enter a valid integer or 'q' to quit.")
        continue

print(f"The total sum is = {sum1}")

print('\n ------ Example 13: while loop as counting operator  ------')
numbers = [2, 0, -5, 1, 8, -6, 7, -3]
index = 0
len_numbers = len(numbers)
evencount = 0
while index < len_numbers:
    if numbers[index] % 2 == 0 and numbers[index] != 0:
        evencount += 1
    index += 1
else:
    print(f"There is/are {evencount} even numbers")

# Lab10 Exercise
print('\n ------ Lab10 Exercise   ------')

colors = ['red', 'orange', 'olive', 'magenta', 'green']
color_match = False

try:
    check_color = input("Enter a color to check: ").strip().lower()

    for color in colors:
        if check_color == color:
            color_match = True
            print(f"{check_color} color is in the list")
            break
    else:
        print(f"{check_color} color is not in the list")
except Exception as e:
    print(f"An error occurred: {e}")
    print("Please run the program again and provide valid input.")