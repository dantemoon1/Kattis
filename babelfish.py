import sys

#read input from stdin and store the first word of each line in a dictionary with the second word as the key
input = {}
flag = False
lines = []
for line in sys.stdin:
    if(line=="\n"):
        #print('found ittt')
        flag = True
    if(flag==False):
        line = line.strip().split()
        input[line[1]] = line[0]
    if(flag):
        lines.append(line.strip())

lines = lines[1:]
print(lines)

for item in lines:
    if item in input:
        print(input[item])
    else:
        print("eh")
    
