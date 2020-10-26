def repeatedString(s, n):

    str_len = len(s)
    rem = n % str_len
    times = n // str_len

    aInStr = 0
    for char in s:
        if char == 'a':
            aInStr += 1
    
    aRemaining = 0
    for i in range(rem):
        if s[i] == 'a':
            aRemaining += 1
    
    return times * aInStr + aRemaining