from ast import Num
from math import factorial
from traceback import print_tb


Num = int(input("number:"))
factorial =1
if Num<0:
    print("must be positive")
elif Num == 0:
    print("factorial = 1")
else:
    for i in range(1, Num + 1):
        factorial = factorial*i
print(factorial)
