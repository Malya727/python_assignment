# Write a program to accept a number “n” from the user; then display the series  1,3,5,7,9,...,n and find the sum of the numbers in this series. 
inp = 0

while((inp % 2) == 0):
    inp = int(input("Enter a odd number to specify the range :"))

li = []
print("The Series is :")
for i in range(1,inp+1,2):
    li.append(i)
    print(i,end=" ")
print(" ")
print("Sum of Series is :" +str(sum(li)))