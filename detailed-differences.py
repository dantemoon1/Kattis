import sys

def solve(a,b):
    print(a) #print the first string
    print(b) #print the second string
    for i in range(len(a)): 
        if a[i] == b[i]: #if the letters are the same, print a .
            print('.',end="")
        else: #otherwise print a *
            print('*',end="")

lines = []
count = -1
for line in sys.stdin: #prepare the input
    count+=1
    lines.append(line.strip())
    num = lines[0]
    if(count==int(num)*2):
        break

i = 1
while(i<len(lines)-1): #loop through all the test cases and pass each to solve()
    solve(lines[i],lines[i+1])
    i+=2
    if(i!=len(lines)-1): #print a newline at the end
        print('\n')

