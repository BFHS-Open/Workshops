def Listify(input_string):
  temp_list = []
  for x in input_string:
    temp_list.append(x)
  return temp_list

"""Tests"""
print(Listify("Hello")) # ['H', 'e', 'l', 'l', 'o']
print(Listify("Work")) # ['W', 'o', 'r', 'k']
print(Listify("No")) # ['N', 'o']
