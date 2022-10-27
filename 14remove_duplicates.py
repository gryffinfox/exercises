# https://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html

# Write a program (function!)
# that takes a list and returns a new list that contains
# all the elements of the first list minus all the duplicates.


def remove_duplicates(list):

    """Take list and save all the unique characters in a new list."""

    n = []
    for x in list:
        if x in n:
            continue
        else:
            n.append(x)

    return n


def make_set(list):
    """Take list and save all the unique characters in a new list."""
    return set(list)


print(remove_duplicates([1, 5, 2, 3, 6, 6, 6, 8, 12, 9, 9]))
print(remove_duplicates([1, 1, 1, 1]))

print(make_set([1, 5, 2, 3, 6, 6, 6, 8, 12, 9, 9]))
print(make_set([1, 1, 1, 1]))
