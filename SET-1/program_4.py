# Write a program to print the Fibonacci series up to the number 34. (Example: 0,1,1,2,3,5,8, 13,... The Fibonacci series starts with 0 and 1, and the succeeding numbers of the series are arrived at by adding the previous 2 numbers.) 

fib1 = 0
fib2 = 1
print(str(fib1) +" "+ str(fib2),end=" ")
for i in range(3,35):
    fib3 = fib1 + fib2
    print(str(fib3) ,end=" ")
    fib1 = fib2
    fib2 = fib3