from time import time

def isUnique1(string):
    if len(string) > 128:
        return False
    string = string.lower()
    occurances = {} 
    for c in string:
        if c in occurances:
            return False
        else:
            occurances[c] = 1
    return True

def isUnique2(string):
    if len(string) > 128:
        return False
    string = string.lower()
    for i in range(0, len(string)-1):
        for j in range(i+1, len(string)):
            if ord(string[i]) ^ ord(string[j]) == 0:
                return False
    return True

def isUnique3(string):
    if len(string) > 128:
        return False
    string = string.lower()
    flags = 0
    for i in range(0, len(string)):
        bit = ord(string[i]) - ord(' ')
        if bit >= 0:
            if flags & (1 << bit):
                return False
            flags |= 1 << bit 
    return True

def isUnique4(string):
    if len(string) > 128:
        return False
    s2 = set(string.lower())
    return len(string) == len(s2)

test1 = 'Lc8rjxLmpUJ1LYaiQWf6ZVepm27lzDWUcwcLEm73MqeJsj6nWOUHRxa75kxN5G0FPvscHOvFkIAeWfvIDFgkR4fNrbmLCmD9PUMN'

print('First function using a dict')
t0 = time()
#print(isUnique1(input('Input a string to test for character uniqueness: ')))
print(isUnique1(test1))
t1 = time()
print('Time: ', (t1-t0))

print('\nSecond function using XOR operator')
t0 = time()
#print(isUnique2(input('Input a string to test for character uniqueness: ')))
print(isUnique2(test1))
t1 = time()
print('Time: ', (t1-t0))

print('\nThird function using bit flags')
t0 = time()
#print(isUnique3(input('Input a string to test for character uniqueness: ')))
print(isUnique3(test1))
t1 = time()
print('Time: ', (t1-t0))

print('\nFourth function converts to a set and compares length change')
t0 = time()
#print(isUnique4(input('String: ')))
print(isUnique4(test1))
t1 = time()
print('Time: ', (t1-t0))
