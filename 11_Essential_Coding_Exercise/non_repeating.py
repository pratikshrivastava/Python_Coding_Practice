# Implement your function below.
def non_repeating(given_string):
    char_count = {}

    for char in given_string:
        if char  in char_count:
            char_count[char] +=1
        else:
            char_count[char] = 1

    #print(char_count)
    for char in given_string:
        if char_count[char] ==1:
            #print(char_count[char])
            return char
    return None

# NOTE: The following input values will be used for testing your solution.

non_repeating("abcab") # should return 'c'
non_repeating("abab") # should return None
non_repeating("aabbbc") # should return 'c'
non_repeating("aabbdbc") # should return 'd'


# NOTE: The following input values will be used for testing your solution.
non_repeating("abcab") # should return 'c'
non_repeating("abab") # should return None
non_repeating("aabbbc") # should return 'c'
non_repeating("aabbdbc") # should return 'd'


test_list = ["abcab", "abab","aabbbc", "aabbdbc" ,"abcab", "abab" ,"aabbbc", "aabbdbc"]

for ll in test_list:
    print(ll, non_repeating(ll))
