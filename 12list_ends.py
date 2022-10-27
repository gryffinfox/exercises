# https://www.practicepython.org/exercise/2014/04/25/12-list-ends.html

# Write a function that takes a list of numbers and
# makes a new list of the first and last elements of the given list


def first_last(list):
    """Take list as input and return first and last element"""

    while True:
        try:
            return [list[0], list[-1]]

        except IndexError:
            return "Your list is empty."


print(first_last([5, 10, 15, 20, 25]))
print(first_last([]))
print(first_last([22, 11, 55, 33]))
print(first_last([1]))
