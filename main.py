from src.masks import get_mask_account, get_mask_card_number

print(get_mask_card_number("1234567812345678"))

print(get_mask_account("123456"))

# result = [x for num in range(20) for x in [num, num] if num % 2 == 0]
# print(result)

# squares = [x*x for x in [1, 2, 3, 4, 5]]
# print(squares)

# mash_index = [i for i, (x,y) in enumerate([(1,2), (2,2), (99,22), (3,3), (2,2)]) if x == y]
# print(mash_index)


# result = (x * x for x in range(1, 11) if x % 2 == 0)
# print(sum(result))

# print(*(x for x in "Hello 89 World!" if x.isupper()))

# evens = (x**3 for x in range(11) if x % 2 == 0)
# print(list(evens))

# def sum_of_squares(lst):
#     return sum(x**2 for x in lst if x > 0)
# print(sum_of_squares([1,2,3,4,5]))

# vowels = (x for x in "hello" if x in ['g', 'h', 'l', 'w', 'p'])
# print(list(vowels))

# name = range(1, 101)
# file_all = list(filter(lambda x: x % 3 == 0 or x % 5 ==0, name))
# avent = sum(file_all) / len(file_all)
# print(avent)


# from itertools import chain
#
# list_1 = [1, 2, 3, 4]
# list_2 = [10, 2, 3, 7]
# list_3 = [6, 8, 9, 5]
#
# numbers = list(set(chain(list_1, list_2, list_3)))
# print(numbers)

# people = [
#     {"name": "Alice", "age": 25},
#     {"name": "Bob", "age": 30},
#     {"name": "Charlie", "age": 35},
#     {"name": "David", "age": 30},
#     {"name": "Eve", "age": 25},
# ]
#
# filter_people = list(filter(lambda x: x["age"] == 30, people))
# print(filter_people)

# def square_generator(nums):
#     for num in nums:
#         yield num ** 2
# print(list(square_generator(range(10))))

# import random
#
# def random_number_generator(start, stop):
#     while True:
#         yield random.randint(start, stop)
# print(next(random_number_generator(1, 10)))







