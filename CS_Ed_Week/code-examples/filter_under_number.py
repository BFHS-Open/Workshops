def filter_under_number(input_number, input_list):
  temp_list = []
  for x in input_list:
    if x < input_number:
      temp_list.append(x)
  return temp_list

"""Tests"""
print(filter_under_number(5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) # [1, 2, 3, 4]
print(filter_under_number(-2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) # []
print(filter_under_number(12, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
