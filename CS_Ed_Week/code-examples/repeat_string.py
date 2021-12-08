def Repeat_String(input_number, input_string):
  temp_list = []
  for x in range(input_number):
    temp_list.append(input_string)
  return temp_list

print(Repeat_String(5, "Hello"))
