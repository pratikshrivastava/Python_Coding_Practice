
'''
Climbing stairs.
taking step 1, 2 or 3 at a time.

find the ways in which we can climb "n" stairs,

1 stair (1) 1 way
2 stair (1 1, 2 )2 ways
3 stair (1 1 1, 1 2, 2 1, 3) 4 ways

4 stair (1 1 1 1, 1 1 2, 1 2 1, 2 1 1, 2 2 , 1 3, 3 1)

so f(n) = f(n-1) + f(n-2) + f(n-3)
'''

ways = {}
def waystoClimb(stairs):
    ways[1] = 1
    ways[2] = 2
    ways[3] = 4

    '''
    if stairs == 1:
        return 1
    elif stairs == 2:
        return 2
    elif stairs == 3:
        return 4
    '''
    for i in range(4, stairs+1):
        ways[i] = ways[i-1]+ways[i-2] + ways[i-3]
        #return ways(stairs - 1) + ways(stairs - 2) + ways(stairs - 3)

    return ways[stairs]

print(waystoClimb(15))
