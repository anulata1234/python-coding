# Python3 program to rotate an array by  
# d elements  
# Function to left rotate arr[] of size n by d*/

def leftRotate(arr, d, n): 
    for i in range(d): 
        leftRotatebyOne(arr, n) 
    return(arr)
  
# Function to left Rotate arr[] of size n by 1*/  
def leftRotatebyOne(arr, n): 
    temp = arr[0] 
    for i in range(n-1): 
        arr[i] = arr[i + 1] 
    arr[n-1] = temp 
          

arr=leftRotate([1,2,3,4,5], 3, 5)
print(arr)
