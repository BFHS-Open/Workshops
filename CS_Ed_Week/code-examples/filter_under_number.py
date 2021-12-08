def Filter_Under_Number(input_number, input_list):
  temp_list = []
  for x in range(len(input_list)):
    if input_list[x] < input_number:
      temp_list.append(input_list[x])
  return temp_list

print(Filter_Under_Number(5, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
