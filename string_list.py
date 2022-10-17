# https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
# Ask user for string input and check if it's palindrome.

#phrase = input('Hello, give me any sentence: ')

def find_palindrome(phrase):
    
    replace_spaces = list(phrase.replace(' ', ''))
    print(replace_spaces)
    reverse_phrase = list(reversed(replace_spaces))
    print(reverse_phrase)

    if replace_spaces == reverse_phrase:
        return 'This sentence is a palindrome.'
    else:
        return 'This is a normal sentence.'


print(find_palindrome('jelenovi pivo nelej'))
print(find_palindrome('Jelenovi pivo nelej'))
print(find_palindrome('blablabla'))
print(find_palindrome('123321'))
print(find_palindrome('Eliza je mandragora'))
            
