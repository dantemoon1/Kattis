import sys
lines = []

def solve(start,end): #solve function
    #print('start ',start,' ',lines[start])
    #print('end ',end,' ',lines[end-1])
    unique = []
    sublist = lines[start:end]
    #print(sublist)
    for x in sublist: #create a list of unique cities
        if x not in unique:
            unique.append(x)
    print(len(unique)) #print the number of unique cities
    
    

for line in sys.stdin: #process input
    lines.append(line.strip())

del(lines[0]) #delete the number of test cases from input
del(lines[0]) #delete the number of cities for first example
lines.append('9') 
#print(lines)

start=0
for i in range(len(lines)):
    if lines[i].isnumeric():
        solve(start,i)
        start=i+1