import sys
input = ""
for line in sys.stdin:
    input = line
    break

print(input[0],end="") #print the first letter of input
for i in range(len(input)): #if the letter is -, print the next letter
    if input[i]=='-':
        print(input[i+1],end="")