#Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.


import numpy as np

# x = [1, 2, 3, 4, 5, 6, 7, 8]
# y = [0, 2, 1, 3, 7, 10, 11, 19]

poly1 = np.poly1d([1,2,3],2)

poly2 = np.poly1d([4,8,7],6)

print(poly1)

print(poly2)

my_file = open('poly1.txt', "w+")
my_file.write(str(poly1))
my_file.close()

my_file = open('poly2.txt', "w+")
my_file.write(str(poly2))
my_file.close()


sum=np.polyadd(poly1,poly2)
print(sum)

my_file = open('sum.txt', "w+")
my_file.write(str(sum))
my_file.close()