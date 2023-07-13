def bubble_sort(List):
    n=len(List)
    for i in range(0,n-1):
        for j in range(0,n-1):
            if List[j]>List[j+1]:
                temp=List[j]
                List[j]=List[j+1]
                List[j+1]=temp
    return List

List=[19,23,45,67,12,32,43,25,67]
print("The unsorted array is:" ,List)
print("The sorted array is:" ,bubble_sort(List))
