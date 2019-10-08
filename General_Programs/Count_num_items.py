def count(sequence, item): 
  total = 0
  for s in sequence:
    if s == item:
    	total += 1
  return total

lst = [1,2,3,4,5,5,5,5,]
number = 5
count(lst, number)