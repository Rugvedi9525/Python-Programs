#Binary Search Algorithm

def binary_search(sorted_array, element):
    low = 0
    high = len(sorted_array)-1
    

    while low <= high:
        mid = int((low + high) / 2) #Rounds of  the result
        guess = sorted_array[mid]
        if guess == element:
            return mid
        elif guess > element:
            high = mid - 1
        elif guess < element:
            low = mid + 1
    return None


lst = [1,2,3,4,5]
element = 5
binary_search(lst,element)