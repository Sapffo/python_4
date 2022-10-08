#Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# list=[1,2,2,2,2,3,5,8,9,7,3,8,9,4]
# # list2=[]
# # for i in list:
# #     if i==i:
# #         del list[i]
# # print(filter (del list[i]),list))

# res=map(filter(lambda i: i==i, del list[i], list),list)
# print(res)

list=[1,2,2,2,2,3,5,8,9,7,3,8,9,4]
temp = [] 
for x in list: 
    if x not in temp: temp.append(x) 
    list = temp
print(temp)

