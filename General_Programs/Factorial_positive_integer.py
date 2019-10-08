#* Mine:-

def factorial_one(n):
  for num in range(1, (n +1)):
    num *= num
  return num
 
print factorial(5)

#* CodeAcademy Solution:-

def factorial_two(x):
    total = 1
    while x>0:
        total *= x
        x-=1
    return total
  
print factorial(5)