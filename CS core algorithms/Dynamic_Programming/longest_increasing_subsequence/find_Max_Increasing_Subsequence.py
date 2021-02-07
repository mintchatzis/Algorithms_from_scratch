'''Brute force solution here. DP solution pending for studying DP theory'''

def findLIS(arr,prev = -1e10,curr = 0):
    if curr == len(arr):
        return 0
        
    taken = 0
    if arr[curr] > prev:
        taken = 1 + findLIS(arr,arr[curr], curr + 1)
        
    nottaken = findLIS(arr,prev, curr+1)
    return max(taken,nottaken)

if __name__ == "__main__":
    
    tests = []
    allTestsPassed = True
    
    def test_1():
        arr = [1,4,3]
        exp = 2
        actual = findLIS(arr)
        assert actual == exp, f"{arr} failed. Actual: {actual} , Expected: {exp}"
    tests.append(test_1)
    
    def test_2():
        arr = [1,2,2,3,1,6]
        exp = 4
        actual = findLIS(arr)
        assert actual == exp, f"{arr} failed. Actual: {actual} , Expected: {exp}"
    tests.append(test_2)
    
    def test_3():
        arr = [3,4,4,5,2,3,4,5,6,7]
        exp = 6
        actual = findLIS(arr)
        assert actual == exp, f"{arr} failed. Actual: {actual} , Expected: {exp}"
    tests.append(test_3)
    
    
    #do tests
    for test in tests:
        try:
            test()
            print(f"test {test} passed")
        except Exception as e:
            allTestsPassed = False
            print(e)

    if allTestsPassed:
        print(f"All {len(tests)} tests passed.")





















