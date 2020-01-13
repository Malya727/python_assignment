# Write a Python script to convert all the following words from singular to plural: 
# a. Story -- Stories b. Emergency -- Emergencies c. Qualify – Qualifies d. Fly -- Flies 
# Hint: Replace the last occurrence of ‘y’ in the word with ‘ies’. 

inp = input("Enter String : ")

x = inp.replace(inp[-1] , "ies")

print(x)