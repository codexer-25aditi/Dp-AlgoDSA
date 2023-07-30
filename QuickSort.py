def swap(arr,i,j):
    arr[i],arr[j]=arr[j],arr[i]
def pivot(arr,pivot,end):
    swapi=pivot
    for i in range(pivot+1,end+1):
        if arr[i]<arr[pivot]:
            swapi+=1
            swap(arr,swapi,i)
    swap(arr,swapi,pivot)
    return swapi


def quickSort(arr,left,right):
    if left<right:
        p=pivot(arr,left,right)
        quickSort(arr,left,p-1)
        quickSort(arr,p+1,right)
    return arr


arr=list(map(int,input().split()))
print(quickSort(arr,0,len(arr)-1))
