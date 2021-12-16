def binary_search(arr,x):
   
    if len(arr)<0:
        return False
    else:
        mid = len(arr)//2
        if x==arr[mid]:
            return True
        else:
            if x < arr[mid]:
                return(binary_search(arr[:mid],x))
            elif x > arr[mid]:
                return(binary_search(arr[mid:],x))
       
arr = [1,2,3,4,5]
print(binary_search(arr,5))

   
    



