#Lab 9 - Recursive Selection Sort
#Cameron Ridderikhoff
#March 23, 2017
import time
def recursiveSS(numList, insertPos):
    if insertPos<1:
        return numList
    high=0
    i=0
    while i<=insertPos:
        if numList[i]>numList[high]:#number is bigger than the highest we've found so far
            high=i
        i+=1    
    #high is now the index of the largest number in the portion of the list we are looking at
    temp=numList[insertPos]
    numList[insertPos]=numList[high]
    numList[high]=temp
    return recursiveSS(numList, insertPos-1)

def selectionSort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax=0
        for location in range(1,fillslot+1):
            if alist[location]>alist[positionOfMax]:
                positionOfMax = location
    
        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp

inputList = [300, 293, 286, 279, 272, 265, 258, 251, 244, 237, 230, 223, 216, 209, 202, 195, 188, 181, 174, 167, 160, 153, 146, 139, 132, 125, 118, 111, 104, 97, 90, 83, 76, 69, 62, 55, 48, 41, 34, 27, 20, 13, 6, 0]

sortTime=time.time()
print(recursiveSS(inputList, len(inputList)-1))
sortTime=time.time()-sortTime
print(sortTime)

inputList = [300, 293, 286, 279, 272, 265, 258, 251, 244, 237, 230, 223, 216, 209, 202, 195, 188, 181, 174, 167, 160, 153, 146, 139, 132, 125, 118, 111, 104, 97, 90, 83, 76, 69, 62, 55, 48, 41, 34, 27, 20, 13, 6, 0]
sortTime=time.time()
selectionSort(inputList)
sortTime=time.time()-sortTime
print(sortTime)