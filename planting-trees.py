
import sys

trees = []
num_trees = input()
for line in sys.stdin:
    trees = line.strip().split()

for i in range(len(trees)):
    trees[i] = int(trees[i])

trees.sort()
trees = trees[::-1]

days = 0
for i in range(len(trees)):
    #print('days:',days)
    #print('trees[i]:',trees[i])
    #print('day number:',i)
    if(days<trees[i]+i): #then this tree will make it longer to grow #have to add i to keep track of all previous days
        #print('this one')
        days=trees[i]+i
    #print()

print(days+2) #have to add 2 to account for the extra day 
