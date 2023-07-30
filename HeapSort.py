def heapify(arr,n,i):
    smallest=i
    l=2*i+1
    r=2*i+2
    if l<n and arr[l]<arr[smallest]:
        smallest=l
    if r<n and arr[r]<arr[smallest]:
        smallest=r
    if smallest!=i:
        arr[i],arr[smallest]=arr[smallest],arr[i]
        heapify(arr,n,smallest)


def heapSort(arr):
    n=len(arr)
    for i in range(int(n/2)-1,-1,-1):
        heapify(arr,n,i)
    for i in range(n-1,0,-1):
        arr[0],arr[i]=arr[i],arr[0]
        heapify(arr,i,0)

    return arr[::-1]

arr=list(map(int,input().split()))
print(heapSort(arr))

