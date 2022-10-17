# https://www.practicepython.org/exercise/2014/02/26/04-divisors.html

# Ask user for a number and print list of all the divisors of this number.
divisors = []
number = int(input('Give me any number: '))
for z in range(2, number):
    if number % z == 0:
        divisors.append(z)
    else:
        continue

print(divisors)
