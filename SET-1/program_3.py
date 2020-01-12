# Write a program to accept a number “n” from the user; find the sum of the series 1/23+1/33+1/43....... +1/n3 

import math
sum_of_series = 0
n = int(input("Enter Range : "))

for i in range(2 , n+1):
    sum_of_series = sum_of_series + (1 / (math.pow(2,3)))

print(sum_of_series)

