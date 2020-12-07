from random import randint

def sort(arr):
    l = len(arr)
    if (l == 1 or l == 0):
        return arr
    
    ipivot = randint(0,l-1)
    pivot = arr[ipivot]
    
    left = []
    right = []
    
    for el in arr:
        if el < pivot:
            left.append(el)
        elif el > pivot:
            right.append(el)
    
    left = sort(left)
    right = sort(right)

    return left + [pivot] + right
    
    
    
if __name__ == '__main__':
    
    arr = [3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]
    
    if (sort(arr) == sorted(arr)):
        print("great success")