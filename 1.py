#Вычислить число c заданной точностью d

from decimal import Decimal
#a = Decimal('0.2')+Decimal('0.2')+Decimal('0.2')-Decimal('0.4')
#print (a)
import decimal
decimal.getcontext().prec=3
#a=3.1415926535897932384626433832795
a=Decimal(1) / Decimal(7)
print(a)