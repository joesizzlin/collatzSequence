# The Collatz Sequence  Practice project

def collatz(number):                    # define function
    if number % 2 == 0:                 # if number is even, then divide by two, assign as 'result'
        result = number // 2            
    else:
        result = 3 * number + 1         # if number is odd, multiply number by 3 then add 1, assign as 'result'
            
    print(result)                       # print the assigned 'result' value
    return result                       # return value of result
    
    
# lets the user type in an integer that keeps calling collatz()on that number until the function returns the value 1
try:
    print('Enter a number:')            # Asks user to input a number
    number = int(input())               # Receives input from the user, converts from string to int with the int() function and assigns to variable 'number'
    while number != 1:                  # Keep calling collatz() until the function returns 1
        number = collatz(number)        # calls collatz function repeatedly while number is not equal to 1
    print('Done!')                      # prints "done" once the while loop is completed
except ValueError:                      # If there is a ValueError, like when the user types in a string, then print this message.
    print('I said I need an integer, bro')