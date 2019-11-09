#Lab 10
#inversions.py
#Cameron Ridderikhoff
#Mar 30, 2017
def countInversions(alist):
    if len(alist)>1:
        mid=len(alist)//2
        left=alist[:mid]
        right=alist[mid:]
        leftInv=countInversions(left)
        rightInv=countInversions(right)
        
        totalInv=leftInv+rightInv
        
        i=0
        j=0
        k=0
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                alist[k]=left[i]
                i+=1
                k+=1
            else:#left>right
                alist[k]=right[j]
                j+=1
                k+=1
                totalInv+=len(left[i:])
        while i<len(left):
            alist[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            alist[k]=right[j]
            j+=1
            k+=1
            
        return totalInv
    else:
        return 0

my_list = [5, 1, 2, 4]
inversions = countInversions(my_list)
print(my_list)
print(inversions)
my_list = [1, 2, 10, 4, 5, 8, 7]
inversions = countInversions(my_list)
print(my_list)
print(inversions)
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
inversions = countInversions(my_list)
print(my_list)
print(inversions)
my_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
inversions = countInversions(my_list)
print(my_list)
print(inversions)