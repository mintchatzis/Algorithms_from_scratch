'''Alogirthm counting the number of inversions in a list given as input'''

from random import randint

def merge_count(left, right):
    '''Function that merges two sorted arrays of length l'''
    
    l = len(left) + len(right)
    count = 0
    arr = []
    
    for _ in range(l):
        if (left == [] and right ==[]):
            pass
        elif (left == []):
            arr.append(right.pop(0))
        elif (right == []):
            arr.append(left.pop(0))
        else:
            if(left[0] <= right[0]):
                arr.append(left.pop(0))
            else:
                arr.append(right.pop(0))
                count += len(left)
                
    return arr, count
        

def inv(arr, countIn):
    '''Function that counts inversions'''
    
    tempArr = []
    countOut = countIn
    l = len(arr)
    
    if(l==1):
        return arr, countIn
    else:
        left, countL = inv(arr[:l//2], countIn)
        right, countR = inv(arr[l//2:], countIn)
        tempArr, mergeCounts = merge_count(left,right)
        
    return tempArr, (countL + countR + mergeCounts)


if __name__ == '__main__':
    
    arr = []
    for i in range(100):
        arr.append(randint(0,100))
        
    inv_count = 0
    _,inv_count = inv(arr, inv_count)
    print("Number of inversions: ", inv_count )



    


            
        

