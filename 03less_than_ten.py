# https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html
# Print all the elements that are less than 5
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for z in a:
    if z < 5:
        print(z)
    else:
        continue

# First extra - save numbers in a new list and print the list
b = []
for y in a:
    if y < 5:
        b.append(y)
    else:
        continue
print(b)

# Second extra - print everything on one line
for x in a:
    if x < 5:
        print(x, end = ' ')
    else:
        continue

# Third extra - Ask user for input and return all the elements that are smaller than the given number
number = int(input('\nGive me any number: '))

for w in a:
    if w < number:
        print(w, end = ' ')
    else:
        continue