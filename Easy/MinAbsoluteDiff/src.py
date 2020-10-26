def minimumAbsoluteDifference(a):
    
    minDiff = abs(a[0]-a[1])
    a.sort()
    n = len(a)

    for i in range(n-1):
        absDiff = abs(a[i]-a[i+1])
        if(absDiff < minDiff):
            minDiff = absDiff
    return minDiff
