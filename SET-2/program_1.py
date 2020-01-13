# 1. Write a program to create an array of size 16; randomly generate numbers in the range 1 – 75  and store in this array. a. Sort the array elements in descending order. b. Print the list of prime numbers present in the array. 
from random import randint
li = []

def prime(num):
    for i in range(2,(num//2)):
        if num % i == 0:
            return False
    return True

pri = []

print("Generated Array is :")
for i in range(0,16):
    g = randint(1 , 75)
    li.append(g)
    if(prime(g)):
        pri.append(g)
print(li)

print("Prime Number in the give array is:")
print(pri)

li.sort(reverse=True)
print("Array in DESENDING order :")
print(li)