'''
We're given Araud affluence and and prices.
P I for I wonder.
And where I is the price of Araud of less.
'''

prices = {1:1,2:5,3:8,4:9,5:10,6:17,7:17,8:20}

R={}
def Revenue(len, prices):
    maxRevenue =-1
    if len ==0:
        R[0] = 0
        return 0

    for i in range(len):
        if i in R and i >0:
            revenue = prices[len-i] + R[i]
        else:
            revenue = prices[len-i] + Revenue(i, prices)

        #print(R,len)
        if revenue > maxRevenue:
            maxRevenue = revenue

    R[len] = maxRevenue

    return maxRevenue

#%%timeit
print(Revenue(5,prices))
