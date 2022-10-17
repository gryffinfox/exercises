# Character Input from https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
name = input('Hello, what is your name?')
age = int(input('Tell me, how old are you?'))
message = "Dear {}, you will turn 100 in {} years.\n".format(name, 100 - age)
print(message)
#print(f"Dear {name}, you will turn 100 in {100-age} years.\n")
number = int(input('Type any number.'))
print(message * number)