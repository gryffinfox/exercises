import random
# https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html

# Compare two lists and return unique elements that are in common between lists.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

matched_elements = []
for element in a:
    if element in b:
        matched_elements.append(element)
    else:
        continue
    unique_elements = set(matched_elements)

print(unique_elements)

# Randomly generate two lists
sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
c = []
d = []
def generate_random_numbers(name_of_list):
    """ Generate ten random elements. """
    name_of_list = random.choices(sample, k=10)
    return name_of_list

print(generate_random_numbers(c))
print(generate_random_numbers(d))
print(c)
print(d)

# Generate random numbers from given list
e = random.choices(sample, k=10)
print(e)