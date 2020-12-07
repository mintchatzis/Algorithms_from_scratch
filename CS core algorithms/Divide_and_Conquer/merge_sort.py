#!/usr/bin/python

'''Self-explanatory, the famous divide and conquer merge sort algorithm.
   Tested using Python's "sorted" function.'''
def merge_sort(arr,f = lambda a,b: a <= b):
    #First define the merge operation
    def merge(left, right):
        '''Function that merges two sorted arrays of length l'''
        arr = []
        l = len(left) + len(right)
    
        for _ in range(l):
            if (left == [] and right ==[]):
                pass
            elif (left == []):
                arr.append(right.pop(0))
            elif (right == []):
                arr.append(left.pop(0))
            else:
                if(f(left[0],right[0])):
                    arr.append(left.pop(0))
                else:
                    arr.append(right.pop(0))
                
        return arr
    
    #Then construct the recursive divide and conquer function
    def sort(arr):    
        l = len(arr)
    
        if(l==1):
            return arr
        else:
            left = sort(arr[:l//2])
            right = sort(arr[l//2:])
        
        return merge(left,right)
    
    return sort(arr)


if __name__ == '__main__':

    def testPassed():
        from random import randint
        
        for _ in range(100):
            arr = [randint(0,50) for _ in range(50)]
    
            expected = sorted(arr)
            received = merge_sort(arr)
            
            assert (expected == received), str(arr)
    
    try:
        testPassed()
    except AssertionError as a:
        print("AssertionError found on list:  ", a)


          

            
        

