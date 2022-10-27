# https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html

# Take a number from user and determin if it's a prime number.


any_number = int(input('Give me any number: '))
for z in range(2, any_number):
    if any_number % z == 0:
        print('{} is not a prime number'.format(any_number))
        break
    else:
        continue
else:
    print('{} is a prime number. :)'.format(any_number))

