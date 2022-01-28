list1=[]
list2=[1,2,3]
list3=[1,2,3,['life', 'good']]

print(list1)
print(list2)
print(list3)

print(list2[2])
print(list3[2], list3[3][0][1])

list2[0]=99
print(list2)
list4=[11,22,33,44]
list4[1:3]=[55,77]
print(list4)
list4[1:3]=[55,77,88]
print(list4)
list4.sort(reverse=True)
print(list4)

