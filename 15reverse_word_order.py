# https://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html

# Write a function that asks the user for a long string containing multiple words. 
# Print back to the user the same string, except with the words in backwards order. 
# For example, say I type the string:


def reverse_phrase(phrase):
    """ Take phrase as input and return it in reverse order."""
    
    split_phrase = phrase.split(' ')
    reversed_phrase = list(reversed(split_phrase))
    return ' '.join(reversed_phrase)

phrase = input('Give me a sentence with multiple words. ')
print(reverse_phrase(phrase))