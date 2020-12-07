#!/usr/bin/python

''' Closest Pair '''

from merge_sort import merge_sort as sort
from math import sqrt


def dist(p1,p2):
    '''Function calculating distance between two points, given as tuples of (x,y)'''
    
    if p1 == None or p2 == None:
        return None
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]    
    return sqrt((y2 - y1)**2 + (x2 - x1)**2)

def bruteForce(points):
    '''Helper function for testing purposes that finds closest pair in O(n^2)'''
    p,q = points[0],points[1]
    l = len(points)
    dmin = dist(p,q)
    for i in range(l-1):
        for j in range(1, l - i):
            a = points[i]
            b = points[i+j]
            d = dist(a,b)
            if d < dmin:
                dmin = d
                p,q = a,b
    return p,q


def findClosestPair(points):
    '''Function that finds closest pair of points in 2D using divide and conquer in O(nlogn)'''

    def check_splitPair(left,right,py,p,q):
        d = dist(p,q)
        mid = right[0]
        left_bound = mid[0] - d
        right_bound = mid[0] + d
        bounded_points = [x for x in py if (x[0] >= left_bound and x[0] <= right_bound and (x in left or x in right))]
        
        dmin = d
        lb = len(bounded_points)
        jRange = min(lb,7)
        for i in range(lb-1):
            for j in range(1,jRange - i):
                p1,p2 = bounded_points[i],bounded_points[i+j]
                dTemp = dist(p1,p2)
                if dTemp < dmin:
                    dmin = dTemp
                    p,q = p1,p2
        return p,q
                

    p_x = sort(points, lambda a,b: a[0] <= b[0])
    p_y = sort(points, lambda a,b: a[1] <= b[1])

    def inner_recurse(px,py):
        l = len(px)
        
        #base cases
        if (l == 1):
            return px[0],None
        if (l == 2):
            return px[0],px[1]
        
        left = px[:l//2]
        right = px[l//2:]
        p1L,p2L = inner_recurse(left,py)
        p1R,p2R = inner_recurse(right,py)
        
        #Find minimum distance between left and right partitions
        d_left = dist(p1L,p2L)
        d_right = dist(p1R,p2R)
        if d_left == None:
            p,q = p1R,p2R
        elif d_right == None:
            p,q = p1L,p2L
        else:
            p,q = (p1L,p2L) if dist(p1L,p2L) < dist(p1R,p2R) else (p1R,p2R)
        
        #update closest points by checking for split pairs
        p,q = check_splitPair(left,right,py,p,q)
        
        return p,q
    return inner_recurse(p_x,p_y)

#Testing
if __name__ == '__main__':
    
    from random import randint,sample
    from time import perf_counter
    
    
    point_pool = [(randint(-100,100),randint(-100,100)) for _ in range(200)]
    isCorrect = True
    for i in range(100):
        points = sample(point_pool,50)
        
        pExp,qExp = bruteForce(point_pool)
        pAct,qAct = findClosestPair(point_pool)
        
        if (pExp,qExp) != (pAct,qAct):
            isCorrect = False
            break
    
    #Simple performance check for experimental purposes
    '''
    points = [(randint(-100,100),randint(-100,100)) for _ in range(1000)]
    
    
    tBruteStart = perf_counter()
    for i in range(100):
        bruteForce(points)
    tBruteTot = perf_counter() - tBruteStart
    print("Brute force time taken: ", tBruteTot)
    
    tDivNConq_start = perf_counter()
    for i in range(100):
        findClosestPair(points)
    tDivNConq_tot = perf_counter() - tDivNConq_start
    print("Divide and Conquer time taken: ", tDivNConq_tot)        
    '''
    
    try:
        assert isCorrect
    except AssertionError as ae:
        print(ae)
    else:
        print("Congrats, your code passed the tests...")
      
    
