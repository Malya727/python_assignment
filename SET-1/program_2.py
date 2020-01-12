# Write a program to accept a number from the user and find the sum of the digits of the number; repeat the operation till the sum gets to be a single digit number.
def sum_of_digits(inp):
    temp = inp
    res = 0
    while(temp != 0):
        rem = temp % 10
        res = res + rem
        temp = temp // 10
    return res

def len(inp):
    le = 0
    while(inp != 0):
        inp = inp // 10
        le = le + 1
    return le

inp = int(input("Enter a Number"))
res = sum_of_digits(inp)

while(len(res) != 1):
    res = sum_of_digits(res)

print(res)
