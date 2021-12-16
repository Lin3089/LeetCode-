def quicksort(data,left.right):
    i = left
    j = right
    key = data[left]
    while i != j:
        while data[j] > key and i < j:#從右邊找比基準點小的
            j -= 1
        while data[i] <= key and i < j:#從左邊找比基準點大的
            i += 1
        if i < j:
            data[i],data[j] = data[j],data[i]
    data[left] = data[i]
    data[i] = key

    quicksort(data,left,i-1)
    quicksort(data,i+1,right)




