# Write a Python script to read the current date from the user. If the user enters the date as
# 12-31-2016 (mm-dd-yyyy), replace all the occurrences of “-“ with “/”. On the other hand, if
# the user enters the date as 12/31/2016 (mm/dd/yyyy), replace all occurrences of “/” with
# “-“.

inp = input("Enter Date seperated by - or / Format :")

if '-' in inp:
    res = inp.replace('-' , '/')
elif '/' in inp:
    res = inp.replace('/' , '-')

print(f"Date is Replaced Format {res}")