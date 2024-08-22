#remove duplicate element from array or list using python

def convertIntoTuple(list):
    listTuple=()
    for i in range(len(list)):
        element=(list[i],)
        listTuple+=element
    return listTuple    

def removeDuplicateElement(list):
    if len(list)<=1:
        return "error: list must have at least two values ! please try again"
    convertedList=convertIntoTuple(list)
    action=True
    index=0
    while action and index<len(list):
        if convertedList.count(list[index])>1:
            list.pop(index)
            action=False
        index=index+1
        action=True
    return list

li=[]
size=int(input("enter the size of array or list = "))

for i in range(size):
    print("enter ",i," th value =")
    elemnt=int(input())
    li.append(elemnt)
copyList=[]
copyList=removeDuplicateElement(li)
print(copyList)