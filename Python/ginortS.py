def custom_sort(ch):
    if ch.isnumeric():
        if not int(ch)&1:
            return 4
        return 3
    elif ch.islower():
        return 1
    elif ch.isupper():
        return 2

S = list(input())
S.sort()
S.sort(key = custom_sort)
    
print("".join(S))
