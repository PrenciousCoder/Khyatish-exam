


from typing import final


def createValidCSV(singleLine):
    list1=[]
    for i in range(0,len(singleLine)):
        temp=singleLine[i]
        list1.append(temp)
    print(list1)

    for j in range(0,len(list1)):
        if list1[j]==" ":
            list1[j]=";"
        elif list1[j]==".":
            list1[j]=","
    res = ''.join(list1)
    final_result=res+";"
    return final_result


    
print(createValidCSV("6.2 4.45"))