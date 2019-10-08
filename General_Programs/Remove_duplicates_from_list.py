def remove_duplicates(num_list):
  list1 = []
  for number in num_list:
    if number not in list1:
      list1.append(number)
  return list1


print remove_duplicates([1,2,3,4,4,5,5,6,6])