def rotation(array,k):
    size=len(array)
    if k>size:
        k=k%size
    
    i=0
    j=size-1
    while i<j:
        array[i],array[j]=array[j],array[i]
        i+=1
        j-=1

    i=0
    j=k-1
    while i<j:
        array[i],array[j]=array[j],array[i]
        i+=1
        j-=1

    i=k
    j=size-1
    while i<j:
        array[i],array[j]=array[j],array[i]
        i+=1
        j-=1

    return array

array=list(map(int,input().split()))
k=int(input())
print(rotation(array,k))
