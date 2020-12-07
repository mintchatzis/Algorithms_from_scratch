'''Module containing binary_search function'''

#Function searching for element and returning its index in the given list, or -1 if not in list.
def binary_search(arr,el):

    #Main function, exposes 2 helping arguments that the wrapper function hid
    def search_main(arr,el,t,part):
        l = len(arr)
        i = l // 2
        if (part == "right"):
            t += i
        else:
            t -= (l-i)
    
        #Distribute cases to respective returns
        if (arr[i] == el):
                return t
        elif (l == 1):
                return -1
        else:
            if (el < arr[i]):
                return search_main(arr[:i],el,t,"left")
            else:
                return search_main(arr[i:],el,t,"right")
            
    return search_main(arr,el,0,"right")

if __name__ == "__main__":
    arr = [1,5,6,7,9,11,15,35,99,101]
    index = binary_search(arr,35)
    
    if (index == -1):
        print("Your element is not in list")
    else:
        print("Element exists in index: ", index)
    
    
        
        
        
        
        