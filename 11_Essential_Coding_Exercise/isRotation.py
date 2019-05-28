# Implement your function below.
def is_rotation(list1, list2):
    p1,p2 = 0,0
    if len(list1) != len(list2):
        return False

    for i, elem in enumerate(list2):
        if elem == list1[0]:
            p2 = i
            break

    for i, elem in enumerate(list1):
        ptr = (i + p2 ) % len(list1)
        #print(ptr)

        if elem != list2[ptr]:
            return False
    return True

# NOTE: The following input values will be used for testing your solution.
list1 = [1, 2, 3, 4, 5, 6, 7]
list2a = [4, 5, 6, 7, 8, 1, 2, 3]
# is_rotation(list1, list2a) should return False.
list2b = [4, 5, 6, 7, 1, 2, 3]
# is_rotation(list1, list2b) should return True.
list2c = [4, 5, 6, 9, 1, 2, 3]
# is_rotation(list1, list2c) should return False.
list2d = [4, 6, 5, 7, 1, 2, 3]
# is_rotation(list1, list2d) should return False.
list2e = [4, 5, 6, 7, 0, 2, 3]
# is_rotation(list1, list2e) should return False.
list2f = [1, 2, 3, 4, 5, 6, 7]
# is_rotation(list1, list2f) should return True.
list2g = [7, 1, 2, 3, 4, 5, 6]
# is_rotation(list1, list2g) should return True.

#test_list = [list(list2+str(chr(i)))  for i in range(97,104)]

test_list = [list2a, list2b, list2c, list2d, list2e, list2f, list2g]

for lists in test_list:
    #print(lists, list2a)
    print(is_rotation(list1, list(lists)))
