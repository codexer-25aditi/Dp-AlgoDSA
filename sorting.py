def SelectionSort(arr):
    for i in range(len(arr)):
        min_in=i
        for j in range(i+1,len(arr)):
            if arr[min_in]>arr[j]:
                min_in=j
        arr[i],arr[min_in]=arr[min_in],arr[i]

    return arr
def BubbleSort(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr

arr=list(map(int,input().split()))
print(SelectionSort(arr))
print(BubbleSort(arr))
