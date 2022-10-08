#Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.


# import random
# from random import randint
# k=2
# list_poly_rate=[randint(0,101) for i in range (10)]
# print(list_poly_rate)
# i=list_poly_rate


# def poly(x):
#     return lambda x:x*list_poly_rate[i],
# poly=list_poly_rate[(id)]

#for i in list_poly_rate:

# def polynomial(x):
#     return lambda x:( sum (i*x**k) for i, i  in list_poly_rate )

# polynomial(lambda x:( sum (i*x**k) for i, i  in list_poly_rate ))

import numpy as np

import random
from random import randint

# p = np.poly1d([random.randint(0,101)for i in range (2)],5)
# print(p)

my_file = open('poly.txt', "w+")
my_file.write(str(np.poly1d([random.randint(0,10)for i in range (2)],4)))
my_file.close()

# path = 'poly.txt'
# data = open(path, 'w+')
# for line in data:
#     print(line)
# data.close()


