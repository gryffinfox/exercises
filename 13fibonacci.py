# https://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html

# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
# Take this opportunity to think about how you can use functions. 
# Make sure to ask the user to enter the number of numbers in the sequence to generate.
# (Hint: The Fibonnaci seqence is a sequence of numbers where 
# the next number in the sequence is the sum of the previous two numbers in the sequence. 
# The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)


def generate_fibonacci_sequence(length_of_sequence):

    """Return fibonacci sequence of length given by user."""

    counter = 2
    fibonacci = [1, 1]

    if counter == length_of_sequence:
        return fibonacci
    
    elif counter > length_of_sequence:
        return 'Input bigger number.'

        
    while counter < length_of_sequence:
        fibonacci.append(fibonacci[-2] + fibonacci[-1])
        counter +=1

    return fibonacci


length_of_sequence = int(input('How many Fibonacci numbers should I print? '))
print(generate_fibonacci_sequence(length_of_sequence))
