from time import time

def checkPermutation(s1, s2):
    s2 = list(s2)
    if len(s1) == len(s2):
        for c in s1:
            if c in s2:
                s2.remove(c)
            else:
                return False
        return len(s2) == 0
    return False

def checkPermutation2(s1, s2):
    if len(s1) == len(s2):
        d = {}
        for c in s1:
            if not c in d:
                d[c] = 1
            else:
                d[c] += 1
        
        for c in s2:
            if c in d:
                d[c] -= 1
                if d[c] == 0:
                    del d[c]
            else:
                return False
        return len(d) == 0
    return False

def checkPermutation3(s1, s2):
    s1 = sorted(s1)
    s2 = sorted(s2)
    return s1 == s2

test1 = 'Lc8rjxLmpUJ1LYaiQWf6ZVepm27lzDWUcwcLEm73MqeJsj6nWOUHRxa75kxN5G0FPvscHOvFkIAeWfvIDFgkR4fNrbmLCmD9PUMN'
test2 = 'nvL6dZkUe8Vl4cQGelYEpurvjfhziwHNYFZZznwdKrwbNoteI9e9iPl0njJM7sj5QflQJ1L28PhdVmQMGGtFt0EAPgKo2cCOupNM'

t0 = time()
print(checkPermutation('abcd', 'bdac'))
print(checkPermutation('abcd', 'dcba'))
print(checkPermutation('abcd', 'eabc'))
print(checkPermutation('abcd', 'bdace'))
print(checkPermutation('abcde', 'bdac'))
print(checkPermutation(test1, test2))
t1 = time()
print('Time: ', (t1-t0))
print()
t0 = time()
print(checkPermutation2('abcd', 'bdac'))
print(checkPermutation2('abcd', 'dcba'))
print(checkPermutation2('abcd', 'eabc'))
print(checkPermutation2('abcd', 'bdace'))
print(checkPermutation2('abcde', 'bdac'))
print(checkPermutation2(test1, test2))
t1 = time()
print('Time: ', (t1-t0))
print()
t0 = time()
print(checkPermutation3('abcd', 'bdac'))
print(checkPermutation3('abcd', 'dcba'))
print(checkPermutation3('abcd', 'eabc'))
print(checkPermutation3('abcd', 'bdace'))
print(checkPermutation3('abcde', 'bdac'))
print(checkPermutation3(test1, test2))
t1 = time()
print('Time: ', (t1-t0))
