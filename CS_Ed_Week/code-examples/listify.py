def listify(input_string):
  temp_list = []
  for x in input_string:
    temp_list.append(x)
  return temp_list

"""Tests"""
print(listify("Hello")) # ['H', 'e', 'l', 'l', 'o']
print(listify("Work")) # ['W', 'o', 'r', 'k']
print(listify("No")) # ['N', 'o']
