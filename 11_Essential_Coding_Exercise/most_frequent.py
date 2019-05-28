# Implement your function below.
def most_frequent(given_list):
    freq = {}
    max_item, count = -1,-1

    if len(given_list) < 1:
        return None

    for item in given_list:

        if item in freq:
            freq[item] +=1
        else:
            freq[item] = 1

        if freq[item]>count:
            max_item = item
            count = freq[item]

    return max_item

# NOTE: The following input values will be used for testing your solution.
# most_frequent(list1) should return 1
list1 = [1, 3, 1, 3, 2, 1]
# most_frequent(list2) should return 3
list2 = [3, 3, 1, 3, 2, 1]
# most_frequent(list3) should return None
list3 = []
# most_frequent(list4) should return 0
list4 = [0]
# most_frequent(list5) should return -1
list5 = [0, -1, 10, 10, -1, 10, -1, -1, -1, 1]


test_list = [list1, list2, list3, list4, list5]

for ll in test_list:
    #print(lists, list2a)
    print(most_frequent(ll))
