def stringRotation(s1, s2):
    if len(s1) == len(s2):
        s2 += s2
        return s1 in s2
    return False

while(1):
    print(stringRotation(input(),input()))
