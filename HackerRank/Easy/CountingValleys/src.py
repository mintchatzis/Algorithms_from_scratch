def countingValleys(steps, path):
    
    lst = list(path)
    numLst = [1 if x == 'U' else -1 for x in lst]

    altitude = [0]
    for step in numLst:
        new_alt = altitude[-1] + step
        altitude.append(new_alt)
    
    count_val = 0
    pattern = [0,-1]

    for i in range(len(altitude)):
        if  altitude[i:i + len(pattern)] == pattern:
            count_val += 1
    
    return count_val