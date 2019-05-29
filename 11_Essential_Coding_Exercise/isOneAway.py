# Implement your function below.

def isOneAwayEqualLen(s1,s2):
    cnt = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            cnt+=1
        if cnt > 1:
            return False
    return True

def isOneAwayDiffLen(s1,s2):
    cnt, pt1, pt2 = 0,0,0

    max_len = max(len(s1),len(s2))

    while pt1 < len(s1) and pt2 <len(s2):
        if s1[pt1] != s2[pt2] and len(s1) > len(s2):
            pt1+=1
            cnt+=1
        elif s1[pt1] != s2[pt2] and len(s1) < len(s2):
            pt2+=1
            cnt+=1
        else:
            pt1+=1
            pt2+=1

        if cnt > 1:
            return False

    return True

def is_one_away(s1, s2):
    if abs(len(s1)-len(s2)) > 1:
        return False
    elif(len(s1) == len(s2)):
        return isOneAwayEqualLen(s1,s2)
    else:
        return isOneAwayDiffLen(s1,s2)

    return False

# NOTE: The following input values will be used for testing your solution.
is_one_away("abcde", "abcd")  # should return True
is_one_away("abde", "abcde")  # should return True
is_one_away("a", "a")  # should return True
is_one_away("abcdef", "abqdef")  # should return True
is_one_away("abcdef", "abccef")  # should return True
is_one_away("abcdef", "abcde")  # should return True
is_one_away("aaa", "abc")  # should return False
is_one_away("abcde", "abc")  # should return False
is_one_away("abc", "abcde")  # should return False
is_one_away("abc", "bcc")  # should return False


print(is_one_away("abcdef", "abcdf"))
