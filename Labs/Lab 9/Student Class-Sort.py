#Lab 9 - Student Class/Sort
#Cameron Ridderikhoff
#March 23, 2017

class Student:
    def __init__(self, ID, name, mark):
        self.ID=ID
        self.name=name
        self.mark=mark
        
    def compare(self, other):
        if self.ID>=other.ID:
            return self
        else:
            return other
        
    def __str__(self):
        return str(self.ID)+" "+self.name+" "+str(self.mark)

def sort(studentList):
    #implementing quick bubble
    i=0
    swapped=True
    while i<len(studentList)-1 and swapped:
        swapped=False
        for j in range(len(studentList)-1):
            if studentList[j].compare(studentList[j+1])==studentList[j]:
                swapped=True
                temp=studentList[j+1]
                studentList[j+1]=studentList[j]
                studentList[j]=temp
        i+=1
    return studentList

s1=Student(1292467, "George Daniel", 89)
s2=Student(1398976, "Amir Jahani", 76)
s3=Student(1392567, "Sarah Kylo", 90)
s4=Student(1368989, "Breanne Lipton", 82)
s5=Student(1409916, "Robert George", 95)
s6=Student(1367814, "Xialing Liu", 86)
s7=Student(1407756, "Mary Simon", 35)
s8=Student(1428867, "Georgina Moore", 88)
s9=Student(1491228, "Brian Johnson", 42)
s10=Student(1398875, "Samuel Picard", 55)
sList=[s1,s2,s3,s4,s5,s6,s7,s8,s9,s10]
        
(sort(sList))
for s in sList:
    print(s)