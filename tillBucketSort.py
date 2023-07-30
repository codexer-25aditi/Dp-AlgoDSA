import math
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

def InsertionSort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
        arr[j+1]=key
    return arr

def BucketSort(arr):
    n=round(math.sqrt(len(arr)))
    maxie=max(arr)
    custom=[]
    for i in range(n):
        custom.append([])
    for i in range(len(arr)):
        num=math.ceil((arr[i]*n)/maxie)
        custom[num-1].append(arr[i])
    result=[]
    for i in range(len(custom)):
        custom[i]=InsertionSort(custom[i])
        result=result+custom[i]
    return result


def merge(customList, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = customList[l + i]

    for j in range(0, n2):
        R[j] = customList[m + 1 + j]

    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            customList[k] = L[i]
            i += 1
        else:
            customList[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        customList[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        customList[k] = R[j]
        j += 1
        k += 1


def mergeSort(customList, l, r):
    if l < r:
        m = (l + (r - 1)) // 2
        mergeSort(customList, l, m)
        mergeSort(customList, m + 1, r)
        merge(customList, l, m, r)
    return customList



arr=list(map(int,input().split()))
print(SelectionSort(arr))
print(BubbleSort(arr))
print(InsertionSort(arr))
print(BucketSort(arr))
print(mergeSort(arr,0,len(arr)-1))


