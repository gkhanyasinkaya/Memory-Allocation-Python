#190709017
import sys

# opening files
input = sys.argv[1]
file = open(input,"r")
outputfile = open("output.txt","w")

# reading lines (there are always 2 lines in a file so:)
aList = file.readline().split(",")
bList = file.readline().split(",")
aList[-1] = aList[-1][:-1]    # to remove '\n' from last element.

# converting elements to integer
aList = [int(i) for i in aList]
bList = [int(i) for i in bList]

# because of a mistake that i made while i writing the all code that you can see
# i am changing the original list at every function...
# these copies for reseting the original list (line:78-79-84-85)
copy_aList=aList[:]
copy_bList=bList[:]

# returning max integer values of lists that has mix types (str and int)
def maxInt(List):
    a=0
    for i in List:
        if isinstance(i, int):
            if i>a:
                a=i
    return a
# for Best-Fit method to find min value that bigger than integer to fit
def GreaterMin(List,element):
    a = maxInt(List)
    for i in List:
        if isinstance(i,int):
            if element<=i and i<a:
                a=i
    return a

def First(item,memoryList):
    for i in memoryList:
        if isinstance(i, int):
            if item<i:
                memoryList[memoryList.index(i)] = i - item
                i = i - item
                memoryList.insert(memoryList.index(i), (str(item) + "*"))
                return (memoryList)
    return "-1"

def Best(element,memoryList):
    a = GreaterMin(memoryList,element)
    memoryList[memoryList.index(a)] = a - element
    a = a - element
    memoryList.insert(memoryList.index(a), (str(element) + "*"))
    return memoryList

def Worst(item,memoryList):
    max_val = maxInt(memoryList)
    if item <= max_val:
        memoryList[memoryList.index(max_val)] = max_val - item
        max_val = max_val - item
        memoryList.insert(memoryList.index(max_val),(str(item)+"*"))
        return (memoryList)
    else:
        return"-1"

def writeMet(aList,bList,methodname,file_name):
    for i in bList:
        aList = methodname(i, aList)
        aString = " ".join(str(j) for j in aList)
        if (aString == "- 1"):
            aString = "not allocated, must wait"
        file_name.write(str(i) + " => " + aString+"\n")

# writing output file

outputfile.write("First-Fit Memory Allocation\n-----------\n")
writeMet(aList,bList,First,outputfile)
aList=copy_aList[:]
bList=copy_bList[:]

outputfile.write("Best-Fit Memory Allocation\n-----------\n")
writeMet(aList,bList,Best,outputfile)
aList=copy_aList[:]
bList=copy_bList[:]

outputfile.write("Worst-Fit Memory Allocation\n-----------\n")
writeMet(aList,bList,Worst,outputfile)


file.close()
outputfile.close()