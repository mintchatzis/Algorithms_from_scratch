#!/usr/bin/python

'''Find ith biggest number in the list given. For example, if given ith = len(list)/2
   it is going to find the median. Naive approach would first sort and then find
   the ith statistic. This approach finds the statistic faster while sorting by not
   traversing through the branch where the ith statistic cannot logically be.'''

def findIthStatistic(arr,ith):
        l = len(arr)
        if (l == 0):
            raise Exception("Function was called with list of length zero, \n which should theoretically never happen")
        
        pivot = arr[0]
    
        left = []
        right = []
        
        foundPivot = False
        for el in arr:
            if (el > pivot):
                right.append(el)
            elif (el < pivot):
                left.append(el)
            elif (el == pivot):
                if foundPivot :
                    left.append(el)
                else:
                    foundPivot = True
    
        lenL= len(left)
        if(ith <= lenL):
            return findIthStatistic(left,ith)
        elif(ith == lenL+1):
            return pivot
        else:
            return findIthStatistic(right,ith - lenL - 1)    
    
    
if __name__ == "__main__":
    from random import randint
    def testPassed():
        for i in range(100):
            arr = [randint(0,100) for _ in range(50)]
            ithStatistic = randint(1,len(arr))
    
            sortTested = sorted(arr)
            expected = sortTested[ithStatistic-1]
    
            received = findIthStatistic(arr,ithStatistic)
            
            assert (expected == received), str(arr)
    
    try:
        testPassed()
    except AssertionError as a:
        print("AssertionError found on list:  ", a)
    
    
    