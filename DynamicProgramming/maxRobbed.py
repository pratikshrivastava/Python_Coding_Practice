'''
Each house has a certain amount of money stashed and the only constraint stopping you from robbing each

of them is that adjacent houses meaning houses beside each other have security systems connected and

it will automatically contact the police if two adjacent houses were broken into in the same night.

So you're given a list of non-negative integers representing the amount of money of each house and you're

asked to determine the maximum amount of money you can rob tonight without alerting the police meaning

you cannot.

robVal = [1, 2, 3, 4, 5]

possible combination of robWoAlert = (1 3, 1 3 5, 2 4, 3 5)
maxRobVal = max(robWoAlert) => (1 3 5)

so for recursive solution.
steal from ith house or not.

if steal from i, then maxRobVal = robVal[i] + max(robWoAlert[i-2,i-3...1])
if doesn't steal from i then maxRobVal = robWoAlert[i-11]

R[1] = robVal[1]
'''
robVal = {1:1,2:2,3:3,4:4,5:5}
def maxRobWoAlert(noOfHouse, robVal):

    if noOfHouse ==0:
        return 0
    elif noOfHouse == 1:
        return robVal[1]
    elif noOfHouse == 2:
        return max(robVal[1], robVal[2])
    # if doesn't stole from i
    maxRobVal = -1
    maxRobVal = max(maxRobVal, maxRobWoAlert(noOfHouse-1, robVal))

    ## if stole from i.

    for j in range(noOfHouse-2, 0, -1):
        maxRobVal = max(maxRobVal, (robVal[noOfHouse]  + maxRobWoAlert(j,robVal)))

    return maxRobVal

for i in range(1,6):
    print('For i ={0}, maximum rob value = {1}'.format(i,maxRobWoAlert(i,robVal)))
