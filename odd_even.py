# Odd or even exercise from https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
number = int(input('Give me any number: '))

if number % 2 == 0:
    if number % 4 == 0:
        print('Number', number, 'is even and multiple of 4.')
    else:
        print('Number', number, 'is even.')
else:
    print('Number', number, 'is odd.')
    


    
