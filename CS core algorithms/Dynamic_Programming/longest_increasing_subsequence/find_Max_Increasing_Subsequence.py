
def find_MLIS(arr):
    
    def inner_rec(arr,n,start=0):
        if start == n-1:
            return 1
        
        local_max =
        current = arr[start]
        for j in range(start+1,n):
            if arr[j] > current:
                subsequence_length = 1 + inner_rec(arr,n,j) 
            else:
                continue
    
    global_max = 1
    for i in range(n-1):
        #recurse and update global_max
        local_max = inner_rec(arr,len(arr))
        global_max = local_max if (local_max > global_max) else global_max
    
    return global_max



if __name__ == "__main__":
    
    tests = []
    allTestsPassed = True
    
    def test_1():
        arr = [1,4,3]
        exp = 2
        actual = findLIS(arr)
        assert actual == exp, f"{arr} failed. Actual: {actual} , Expected: {exp}"
    #tests.append(test_1)
    
    def test_2():
        arr = [1,2,2,3,1,6]
        exp = 4
        actual = findLIS(arr)
        assert actual == exp, f"{arr} failed. Actual: {actual} , Expected: {exp}"
    #tests.append(test_2)
    
    def test_3():
        arr = [3,4,4,5,2,3,4,5,6,7]
        exp = 6
        actual = findLIS(arr)
        assert actual == exp, f"{arr} failed. Actual: {actual} , Expected: {exp}"
    #tests.append(test_3)
    
    
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





















