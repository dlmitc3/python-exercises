#1) Conditional Basics

#A) prompt the user for a day of the week, print out whether the day is Monday or not

day = input('day_of_the_week?'  )

if day.lower() in ['monday', 'mon']:
    print('Happy Monday')
else:
    print('Today is not Monday')

#B)prompt the user for a day of the week, print out whether the day is a weekday or a weekend

day = input("day_of_the_week? ")
if day.lower().startswith("s"):
    print(f"{day} is a Weekend")
else: 
    print(f"{day} is a Weekday")

#C)create variables and make up values for
#the number of hours worked in one week
#the hourly rate
#how much the week's paycheck will be

#write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours
 
hr = input('Hours Worked? ')
hr = int(hr)
rate = input('hourly Rate? ')
rate = int(rate)
week_pay = hr * rate
if hr > 40:
    print((rate * 40)+(1.5 * rate * (hr - 40)))
else:
    print(week_pay)

#2) Loop Baiscs 

#A)While Loops

#Create an integer variable i with a value of 5.
#Create a while loop that runs so long as i is less than or equal to 15
#Each loop iteration, output the current value of i, then increment i by one.

i = 5
while i <= 15:
    print(i)
    i += 1

#Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.

i = 0
while i <= 100:
    print(i)
    i += 2

#Alter your loop to count backwards by 5's from 100 to -10.
 
i = 100
while i >= -10:
    print(i)
    i += -5

#Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:
 
i = 2
while i < 1000000:
    print(i)
    i = i ** 2

#B)For Loops

#Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.
 
num = input('Number? ')
num = int(num)
for i in range(1, 11):
    print(num, 'x', i, '=', num*i)

#Create a for loop that uses print to create the output shown below.

for number in range(10):
    print(str(number) * number)

#C)Break and Continue

#Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement
     
num = input ('Please enter only odd number 1, 50' )

while True:
    if (num.isdigit = False or int(num) > 50 or int(num) < 1 or int(num) % 2 == 0):
        print('invald input')
        num = input('Please enter only odd number 1, 50'):
    else
        break   

num = int(num)

print('number to skip is:' num)

for i in range(1,50):
    if i % 2 == 0:
        continue
    elif i == num:
        print('Yikes, please skip', i)
    else:
        print('Here is odd number', i)    

 #D)
     
# The input function can be used to prompt for input and use that input in your python code. 
# Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
# (Hints: first make sure that the value the user entered is a valid number, 
# also note that the input function returns a string, so you'll need to convert this to a numeric type.)

def print_count_to_number(start_at, end_at, increment):
    count_out = [print(num) for num in range(start_at, end_at, increment)]


def count_to_user_number():
    user_input = input('positive integer output: ')
    
    while True:
        if user_input.isdigit() == False:
            print(f'{user_input} not a positive integer')
            break

        user_int = int(user_input)
        
        if user_int > 0:
            print_count_to_number(0, user_int+1, 1)
            
        user_input = input('please provied a positive integer: ')

        
count_to_user_number()


#E) 
# Write a program that prompts the user for a positive integer. 
# Next write a loop that prints out the numbers from the number the user entered down to 1. 

is_not_digit = True
while is_not_digit:
    count_from = input('Countdown for liftoff:\n')
    if count_from.isdigit():
        count_from = int(count_from)
    if count_from >= 0:
        is_not_digit = False

for n in range(count_from, 0, -1):
    print(n)


# 3) Fizzbuzz

#One of the most common interview questions for entry-level programmers is the FizzBuzz test. 
#Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.

# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

for n in range(1, 101, 1):
    if n % 5 == 0 and n % 3 == 0:
        print('FizzBuzz')
    elif n % 5 == 0:
        print('Buzz')
    elif n % 3 == 0:
        print('Fizz')
    else:
        print(n)

# 4) Display a table of powers.

# Prompt the user to enter an integer.
# Display a table of squares and cubes from 1 to the value entered.
# Ask if the user wants to continue.
# Assume that the user will enter valid data.
# Only continue if the user agrees to.

number = input ("What number would you like to go up to? ")

number = int(number) 
#squared = int(number) * int(number) 
#cubed = int(number) * int(number) * int(number)

print('n','sq','cb' )
for i in range(1, number+1):    
    squared = int(i) * int(i) 
    cubed = int(i) * int(i) * int(i)

    print(i, squared, cubed)


# Bonus: Research python's format string specifiers to align the table

# 5) Convert given number grades into letter grades.

    # Prompt the user for a numerical grade from 0 to 100.
    # Display the corresponding letter grade.
    # Prompt the user to continue.
    # Assume that the user will enter valid integers for the grades.
    # The application should only continue if the user agrees to.
    # Grade Ranges:
        # A : 100 - 88
        # B : 87 - 80
        # C : 79 - 67
        # D : 66 - 60
        # F : 59 - 0

run_loop = True
while run_loop:

    grade = input ("please input numerical grade between 1, 100"  )

    grade = int(grade)

    if grade >= 88:
        print(f'{grade} is an A --congradulations!!')
    elif grade >= 80:
        print(f'{grade} is an B --keep up the good work!')
    elif grade >= 67:
        print(f'{grade} is an C --nice work!')
    elif grade >= 60:
        print(f'{grade} is an D --try harder next time!')
    else:
        print(f'{grade} is an F --Failed, try again!')

    user_choice = input(" Do you want to continue?   type 'y' for YES,  or  'n' for NO")

    run_loop = user_choice.lower() in ['y', 'yes']

print("Thanks for using this app")


# Bonus

#Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+).

run_loop = True
while run_loop:

    grade = input ("please input numerical grade between 1, 100"  )

    grade = int(grade)

    if grade >= 98:
        print(f'{grade} is an A+ --congradulations!!')
    elif grade >= 93:
        print(f'{grade} is an A --keep up the good work!') 
    elif grade >= 90:
        print(f'{grade} is an A- --good work!')     
    elif grade >= 89:
        print(f'{grade} is an B+ --keep it up!')
    elif grade >= 83:
        print(f'{grade} is an B --nice work!')
    elif grade >= 80:
        print(f'{grade} is an B- --try harder next time!')
    elif grade >= 79:
        print(f'{grade} is an C+ --good work!')     
    elif grade >= 73:
        print(f'{grade} is an C --keep up the good work!')
    elif grade >= 70:
        print(f'{grade} is an C- --nice work!')
    elif grade >= 69:
        print(f'{grade} is an D+ --try harder next time!')
    elif grade >= 63:
        print(f'{grade} is an D --good work!')     
    elif grade >= 60:
        print(f'{grade} is an D- --work harder next time!')
    else:
        print(f'{grade} is an F --Failed, try again!')

    user_choice = input(" Do you want to continue?   type 'y' for YES,  or  'n' for NO")

    run_loop = user_choice.lower() in ['y', 'yes']

print("Thanks for using this app")


#6) Create a list of dictionaries where each dictionary represents a book that you have read. 
# Each dictionary in the list should have the keys title, author, and genre. 
# Loop through the list and print out information about each book.


dictionary = [{"yr": "year", "ge": "genre", "au": "author", "title": "key_title"}]

print(dictionary)


    {"ge": "genre" ["fiction", " autobiography", "fantacy"]},
    {"au": "author" ["Herman_Melville", "David_Wilson", "J.K.Rowling"]},
    {"title": "key_title" ["Moby-Dick", "Twelve Years a Slave", "Harry_Potter and The Philospher's Stone"]}]         

print(dictionary)

for i in dictionary:
    if i ["tpye"] == "categorical" of i["type"] == "boolean":
        print(f"{i["author"]} is not numeric, skipping")
        continue

print("thanks")

    # A) Prompt the user to enter a genre, then loop through your books 
    # list and print out the titles of all the books in that genre.
