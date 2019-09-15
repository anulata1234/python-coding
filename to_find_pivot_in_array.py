# pivot is a number from where the number order is not ascending or decending , in this case the number is 4

def findPivot(arr, low, high):
    # base cases 
    if high < low: 
        return -1
    if high == low: 
        return low 
      
    #low + (high - low)/2; 
    mid = int((low + high)/2) 
      
    if mid < high and arr[mid] > arr[mid + 1]: 
        return mid 
    if mid > low and arr[mid] < arr[mid - 1]: 
        return (mid-1) 
    if arr[low] >= arr[mid]: 
        return findPivot(arr, low, mid-1) 
    return findPivot(arr, mid + 1, high)



value = findPivot([4,2,3],0,2)
print(value)
