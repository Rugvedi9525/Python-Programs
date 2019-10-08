#Method 1 - Isolating all the digits in a integer and then getting a sum
def digit_sum_method_one(n):
  print (n)
  result = 0
  while n > 0:
    digit = n % 10
    result = digit + result 
    n = n // 10
  print (result)

#Method 2 - Converting the number into String
def digit_sum_method_two(n):
  lst = [] 
  conv_str = str(n) 
  for digit in conv_str:
    lst.append(int(digit))
  print sum(lst)
  
#Method 3 - (Counter method)

def digit_sum_method_three(n):
  conv_str = str(n)
  total = 0
  for digit in conv_str:
    total += int(digit)
  print total
