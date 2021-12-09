def repeat_string(input_number, input_string):
  temp_list = []
  for x in range(input_number):
    temp_list.append(input_string)
  return temp_list

"""Tests"""
print(repeat_string(5, "Hello")) # ['Hello', 'Hello', 'Hello', 'Hello', 'Hello']
