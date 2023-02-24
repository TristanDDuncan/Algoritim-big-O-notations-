


# # O(1) Time complexity
# def odd_even(number):
#     if number % 2 == 0:
#         return "even"
#     else:
#         return "odd"

# print(odd_even(9))



# Task 2
# Given a list of numbers, determine if each item in the list is lower than 100.
# The function should take in the list as a parameter and return a boolean value 
# (False if there are any numbers greater than or equal to 100, True if all numbers are less than 100).
# Leave a comment above the function stating the time complexity.
# Send a screenshot of your solution and time complexity comment to your personal instructors chat.
# O(n)
# def numbers(list_numbers):
#     for number in list_numbers:
#         if number >= 100:
#             return False
#         elif number <= 100:
#             return True
# list_numbers = [65,565,55,32,676,5534,34,99,43,44]
# print(numbers(list_numbers))

# list_numbers = [100,999,89,789]
# print(numbers(list_numbers))

# Given a list of names, determine if any names are contained in the list more than once.
# The function should take in the list as a parameter and return a boolean value
#  (True if there are any repeated names, False if there are no repeats).
# Leave a comment above the function stating the time complexity.
# Send a screenshot of your solution and time complexity comment to your personal instructors chat.
# O(n)
# def list_of_names(names: list):
#     unique_name = []
#     for name in names:
#         if name not in unique_name:
#             unique_name.append(name)
#     if len(names) == len(unique_name):
#         return False
#     else:
#         return True

# result = list_of_names(["jon","nini",'cale'])
# print (result)

# result = list_of_names(["jon","nini",'cale','jon'])
# print (result)




# Task 4: Sort List
# Given a list of numbers, manually sort the list into ascending order 
# (may not use built in .sort() method).
# Suggested strategy:
# Starting with the first two numbers, compare them to see which is larger. 
# Place the lower number to the left and the higher number to the right.
# Iterate through the list, checking each pair of numbers one at a time.
# Repeat from the start until the entire list is sorted.

def sort_list(num_list: list) -> list:
    for j in range(len(num_list)-1):
        for i in range(len(num_list)-1):
            current_num = num_list[i]
            next_num = num_list[i+1]
            if current_num > next_num:
                num_list[i] - next_num
                num_list[i+1] = current_num 
    return num_list


sorted_list = sort_list([5,3,7,2,6,1,4])
print(sorted_list)