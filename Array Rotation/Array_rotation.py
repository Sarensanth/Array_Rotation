def rotation(array,i,j):
    while i<j:
        array[i],array[j]=array[j],array[i]
        i+=1
        j-=1

array=list(map(int,input().split()))
k=int(input())
size=len(array)
if k>size:
    k=k%size
rotation(array,0,size-1)
rotation(array,0,k-1)
rotation(array,k,size-1)
print(array)