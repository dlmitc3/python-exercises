# Exercises

# Create a file named function_exercises.py for this exercise. 
# After creating each function specified below, write the necessary 
# code in order to test your function.

# 1) Define a function named is_two. 
#    It should accept one input and return True if the passed 
#    input is either the number or the string 2, False otherwise.

def is_two(num):

     if num in [2 , '2']:
         return True
     else:
         return False

         


# 2) Define a function named is_vowel. 
#    It should return True if the passed string is a vowel, False otherwise.

def is_vowel(letter):

    if letter.upper() in ['A', 'E', 'I', 'O', 'U']:
        return True
    else:
        return False


# 3) Define a function named is_consonant. 
#    It should return True if the passed string is a consonant, False otherwise. 
#    Use your is_vowel function to accomplish this.

def is_consonant(i):

    if i.upper() in ['A', 'E', 'I', 'O', 'U']:
        return False
    else:
        return True



# 4) Define a function that accepts a string that is a word. 
#    The function should capitalize the first letter of the word if the word starts with a consonant.

def is_word(x):

    if x[0] not in 'aeiou':
        return x.capitalize()
    else:
        print('does not start with consonant or not a word')
        return x 



# 5) Define a function named calculate_tip. 
#    It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

def calculated_tip(tip_percent, bill):
    amount_to_tip = tip_percent * bill
    return amount_to_tip


# 6) Define a function named apply_discount. 
#    It should accept a original price, and a discount percentage, and return the price after the discount is applied.

def apply_discount(price, discount):
    amount_discounted = price * discount
    price_post_discount = price - amount_discounted
    return price_post_discount



# 7) Define a function named handle_commas. 
#    It should accept a string that is a number that contains commas in it as input, and return a number as output.

def handle_commas(x):
    no_commas = x.replace(',', '')
    if no_commas.isdigit():
        return int(no_commas)
    else:
        print('No letters !')



# 8) Define a function named get_letter_grade. 
#    It should accept a number and return the letter grade associated with that number (A-F).

def get_letter_grade(x):
    if x in range(0, 60):
        return 'F'
    elif x in range(60, 67):
        return 'D'
    elif x in range(67, 80):
        return 'C'
    elif x in range(80, 88):
        return 'B'
    elif x in range(88, 100):
        return 'A'
    else:
        print('I dont know what to do...')  



# 9) Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

def remove_vowels(x):
    r_vow = ''
    for char in x:
        if char in ('aeiou'):
            continue
        else:
            r_vow += char
    return r_vow


# 10) Define a function named normalize_name. 
#   It should accept a string and return a valid python identifier, that is:
    # anything that is not a valid python identifier should be removed
    # leading and trailing whitespace should be removed
    # everything should be lowercase
    # spaces should be replaced with underscores
    # for example:
        # Name will become name
        # First Name will become first_name
        # % Completed will become completed


all_char = ' abcdefghijklmnopqrstuvwxyz_1234567890'
 
def normalize_name(x):
    norm_x = ''
    prime_x = x.strip().lower()
    for char in prime_x:
        if char not in all_char:
            continue
        else:
            norm_x += char
    return norm_x.strip().replace(' ', '_')



# 11) Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
    # cumulative_sum([1, 1, 1]) returns [1, 2, 3]
    # cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

def cumulative_sum(x):
    for n in range(1, len(x)):
        x[n] += sum(x[n - 1:n])
        return x



list = [1, 2, 3, 4]
cumulative_sum(list)


# Additional Exercise

# Once you've completed the above exercises, follow the directions from https://gist.github.com/zgulde/ec8ed80ad8216905cda83d5645c60886 in order to thouroughly comment your code to explain your code.

# our sayhello defines a single parameter, name that is a string, 
# and will return a string value
def sayhello(name):
    ''''  Block of comment explaning what this function does
    '''
    # Check to see if the passed argument is equal to our cohort name
    if name.lower() == "jamison":
        # Craft the message to complete only is statment is True
        message = "Goodmorning Jamison cohort!!! Have a great day!"
    else:
        # hello message will complete only if statemenb does not meet pass argument
        message = f"Hello, {name}!"
    # Regardless of the contents, we'll return the message variable from the function
    return message
# input data used to check if statment passes argument

# Bonus

# 1) Create a function named twelveto24. 
# It should accept a string in the format 10:45am or 4:30pm and return a string 
# that is the representation of the time in a 24-hour format. 


def convert(string):

    if string[-2:] == "AM" and string[:2] == "12":
        return "00" + string[2:-2]

    elif string[-2:] == "AM":
        return string[:-2]

    elif string[-2:] == "PM" and string[:2] == "12":
        return string[:-2]
        
    else:
        return str(int(string[:2]) + 12) + string[2:8]

#driver code
print("12-hour Format time:: ", time)
print("24-hour Format time ::",convert(time))


# Bonus write a function that does the opposite.

def convert(string):

    if string[-2:] == "AM" and string[:2] == "12":
        return "00" + string[2:-2]

    elif string[-2:] == "AM":
        return string[:-2]

    elif string[-2:] == "PM" and string[:2] == "12":
        return string[:-2]
        
    else:
        return str(int(string[:2]) - 12) + string[2:8]

#driver code
print("12-hour Format time:: ", convert(time))
print("24-hour Format time ::",time)


# 2) Create a function named col_index. 
# It should accept a spreadsheet column name, and return the index number of the column.
    # col_index('A') returns 1
    # col_index('B') returns 2
    # col_index('AA') returns 27


# defined a single parameter, named col_index, and will return a string value
def col_index(i):

 # Converting string to integer values, only if condition are met. else returning 
 # a not found paramater and exiting program
    if i.upper() == 'A':
        return 'column number is: 1'
    elif i.upper() == 'B':
        return 'column number is: 2'
    elif i.upper() in 'AA':
        return 'column number is: 27'
    else:
        return ('column name and index not found')

# input data used to check if statment passes argument


def col2num(col):
    num = 0
    for c in col:
        if c in string.ascii_letters:
            num = num * 26 + (ord(c.upper()) - ord('A')) + 1
    return num



if __name__ == "__main__":
    col2num (input('number is equal to:  '))
    col_index (input('spreadsheet column name:'   ))
    is_two (input('Only enter the number 2, "otherwise answer will be False"'  ))
    is_vowel (input (str('Enter vowel only!')))
    is_consonant (input (str('Enter Consonant only!')))
    is_word(input(str('Enter a word:')))
    calculated_tip(.25, 40)
    apply_discount(50, .4)
    handle_commas(input('Enter a large number:'))
    get_letter_grade(int(input('Enter your grade')))
    time = input("Input time in a 24-hour format: hh:mm:ss AM or PM"  )
    time = input("Input time in a 12-hour format: hh:mm:ss AM or PM"  )
    sayhello (input(str("What is your class name:  ")))
    normalize_name(input('Enter your full name:'))
    remove_vowels(input('Enter a word:'))
