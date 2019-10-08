#My solution:
#VOILA!


def median_one(num_list):
  num_list.sort()
  if len(num_list)%2==0:
    b= num_list[(len(num_list)/2)-1]
    a= num_list[(len(num_list)/2)]
    med=(a+b)/2.0
    return med
  else:
     return num_list[((len(num_list)-1)/2)]
    
print median_one([1,2,3,4,5])

#Codacademy solution!
def median_two(lst):
    sorted_list = sorted(lst)
    if len(sorted_list) % 2 != 0:
        #odd number of elements
        index = len(sorted_list)//2 
        return sorted_list[index]
    elif len(sorted_list) % 2 == 0:
        #even no. of elements
        index_1 = len(sorted_list)/2 - 1
        index_2 = len(sorted_list)/2
        mean = (sorted_list[index_1] + sorted_list[index_2])/2.0
        return mean
   
print median_two([2, 4, 5, 9])