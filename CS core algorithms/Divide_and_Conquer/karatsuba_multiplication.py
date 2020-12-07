'''
    Karatsuba multiplication algorithm (for even numbers as inputs)
    input: 2 integers
    output: The result of their multiplication (integer too)
    
'''

def manual_multiply(x,y):
    if x == 0 or y == 0:
        return 0
    
    num = x
    for i in range(y - 1):
        x += num
    return x

def karatsuba(num1,num2):
    a = num1
    b = num2
    
    a = [int(x) for x in str(a)]
    b = [int(x) for x in str(b)]
    
    return karatsuba_main(a,b)

def karatsuba_main(x,y):
    n = len(x)
    
    if (n == 1):
        return manual_multiply(x[0],y[0])
    
    a = x[: n//2]
    b = x[n//2 :]
    c = y[: n//2]
    d = y[n//2 :]
    
    ac = karatsuba_main(a,c)
    bd = karatsuba_main(b,d)
    ad = karatsuba_main(a,d)
    bc = karatsuba_main(b,c)
    
    return (10**n * ac  +  10**(n//2) * (ad + bc)  +  bd)

if __name__ == '__main__':
    num1 = 3141592653589793238462643383279502884197169399375105820974944592
    num2 = 2718281828459045235360287471352662497757247093699959574966967628
    
    res = karatsuba(num1,num2)
    
    if(res == num1 * num2):
        print("test passed")
    
    
