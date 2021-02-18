# values_range = range(10) # by default if range is given only one option then the it will stat from zero and end at the option it is passed, step is equal to 1 by default

# print(values_range)

# values_list = list(values_range) # a range must be converted to a list to see its values

# print(values_list)

# values_range = range(15, 30, 3) # range

# print(values_range)

# values_list = list(values_range)

# print(values_list)

# ## REVERSED

# reversed_list = list(reversed(values_list)) # reversed takes a list and flips it making the first item become the last and the last item become the first. This function returns a reverse object by default and needs to be converted into a list to view it's items.
# print(reversed_list)

# # ROUND

# x = 10.33343
# rounded_value = round(x)
# print(rounded_value)

# rounded_value = round(x, 4) # round take a number and the number of decimal places required and rounds it off according to the decimal places.
# print(rounded_value)

# sorted builtin function

values = [2,6,1,9,2,2,4,5]

sorted_values = sorted(values) # takes an unsorted range of values and sorts in ascending order. To sort in descending order the argument reversed can also be passed as set to true.
print(sorted_values)

sorted_values = sorted(values, reverse=True)
print(sorted_values)

# sum built in function

print(sum([2,6,1,9,2,2,4,5]))
print(sum([50,50]))


# dict built in function

# students = dict(ade = ["ade", 30, 105], john = ["john", 25, 147], jake = ["jake", 40, 160])
# print(students)

# my_stuff= dict()
# print(my_stuff)
# # "adamu"
# # 10000
# # [1000,1000,1000]

# # sets are unordered and do not allow repitition they can be used to get unique values in a list of numbers.
# print(values)
# print(set(values))

# MAP TAKES A LIST OF VALUES AND ALSO A FUNCTION AND THEN TRIES TO DO THE FUNCTION ON EACH OF THE VALUES OF THE LIST OF VALUES

# names = ["Jonah", "Kunle", "Saheed", "Lekan"]

# def make_upper(name):
#     return "Mr. " + name.upper()

# upper_case_names = map(make_upper, names) # CONVERT ALL NAMES IN LIST TO UPPER CASE AND ADD MR TO THEM
# print(list(upper_case_names))

# names = ["Jonah", "Kunle", "Saheed", "Lekan"]

# def make_upper(name):
#     return sorted(name.upper())

# upper_case_names = map(make_upper, names)
# print(list(upper_case_names))

# numbers = [1,2,3,4,5,6,7,8,9]

# def square_nums(number):
#     return number * number

# squared_nums = map(square_nums, numbers)
# print(list(squared_nums))

# ages = [23, 44, 20, 38, 19, 15]

# def square_nums(number):
#     return 2021 - number

# squared_nums = map(square_nums, ages)
# print(list(squared_nums))

