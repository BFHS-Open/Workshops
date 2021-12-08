def Listify(input_string):
  temp_list = []
  for x in range(len(input_string)):
    temp_list.append(input_string[x])
  return temp_list

print(Listify("Hello"))
