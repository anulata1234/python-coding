def binary_search(arr, key, low , high):
    # finding out the mid index in an array.
    mid = (low+high)//2
    
    if low>high:
        return -1
    if low==high:
        return low
    
    if key==arr[mid]:
        return(arr.index(arr[mid]))
       
    elif key>arr[mid]:
        return binary_search(arr, key, mid+1, high)

    elif key<arr[mid]:
        return binary_search(arr, key, low, mid-1)
        
        
value = binary_search([1,2,3,4,5,6,7,8,9],4, 0, 8)
print(value)
