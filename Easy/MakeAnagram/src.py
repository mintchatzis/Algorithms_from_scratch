# Complete the makeAnagram function below.
def makeAnagram(a, b):

    setA = createSetOfLetters(a)
    setB = createSetOfLetters(b)
    commonAB = setA & setB
    symmDiffA = (setA - setB) 
    symmDiffB = (setB - setA)

    dictA = {}
    dictB = {}

    for letter in setA:
        dictA[letter] = 0
    for letter in setB:
        dictB[letter] = 0
    
    for letter in a:
        dictA[letter] += 1
    for letter in b:
        dictB[letter] += 1 
        
    minDelete = 0

    for letter in symmDiffA:
        minDelete += dictA[letter]
    for letter in symmDiffB:
        minDelete += dictB[letter]

    for letter in commonAB:
        minDelete += abs(dictA[letter] - dictB[letter])
    
    return(minDelete)


