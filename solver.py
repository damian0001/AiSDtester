def x(v):
    x = v.copy()
    x.pop(0)
    x.pop(0)
    return x
    
def q1():
    temp=input().split()
    arr = list(map(float, temp))
    print(x(arr))
    return x(arr)
    
def q2():
    temp=input().split()
    q = list(map(int, temp))
    return q
    
def floor_2(x):
    if x%2==0:
        return x/2
    else: 
        return (x-1)/2
        
def insertion(arr):
    #N=int(str(arr[0]))
    for j in range (1,len(arr)):
        key=arr[j]
        i=j-1
        while i >= 0 and arr[i] > key:
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = key
        print(arr)
        
def insertion2(arr):
    for j in range (1,len(arr)):
        key=arr[j]
        i=j-1
        while i >= 0 and arr[i] > key:
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = key
    return arr
def bubble(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1, i, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
        print(arr)
    
def merge(arr, p, q, r):
    x1 = int(q - p + 1)
    x2 = int(r - q)
    arr1=[]
    arr2=[]
    for i in range(x1):
        arr1.append(arr[int(p + i)])
    for j in range(x2):
        arr2.append(arr[int(q + 1 + j)])
    i=int(0)
    j=int(0)
    a=int(p)
    while i < x1 and j < x2:
        if arr1[i] <= arr2[j]:
            arr[a] = arr1[i]
            i=i+1
            a=a+1
        else:
            arr[a] = arr2[j]
            j=j+1
            a=a+1
    while i < x1:
        arr[a] = arr1[i]
        i=i+1
        a=a+1
    while j < x2:
        arr[a] = arr2[j]
        j=j+1
        a=a+1

def merge_sort(arr, p, r):
    if p < r:
        q = floor_2(p + r)
        merge_sort(arr, p, q)
        merge_sort(arr, q+1, r)
        merge(arr, p, q, r)
        
def parriton(A, p, r):
    x=A[r]
    i=p-1
    for j in range (p,r):
        if A[j]<=x:
            i=i+1
            A[j], A[i] = A[i], A[j]
    A[r], A[i+1] = A[i+1], A[r]
    return i+1
        
def qsort(A, p, r):
    if p<r:
        q=parriton(A, p, r)
        qsort(A,p,q-1)
        qsort(A,q,r)
        
def bucket(A):
    n=len(A)
    B = [[] for _ in range(n)]
    for i in range(n):
        B_idx = int(A[i]*n)
        B[B_idx].append(arr[i])
    for i in range(n):
        B[i]=insertion2(B[i])
    print(B)
    C=[]
    for i in range(n):
        C=C+B[i]
        #print(C)
    return C
    
    

arr = q1()
while True:
    command = q2()
    if command == [-1, 0]:
        print("koniec")
        break
    elif command == [0, 0]:
        a=1
        print(arr.pop(0))
    elif command == [1, 0]:
        insertion(arr)
        print(arr)
        # insertion
    elif command == [2, 0]:
        bubble(arr)
        print(arr)
        # bubble
    elif command == [3, 0]:
        print(bucket(arr))
        #bubble
    elif command == [4, 0]:
        merge_sort(arr, 0, len(arr)-1)
        print(arr)
        # merge
    elif command == [5, 0]:
        qsort(arr, 0, len(arr)-1)
        print(arr)
        # qsort
