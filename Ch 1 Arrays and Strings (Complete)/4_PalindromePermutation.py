from time import time

def palindromePermutation(string):
    string = string.lower()
    chars = {}
    for c in string:
        if c.isalpha():
            if not c in chars:
                chars[c] = 1
            else:
                chars[c] += 1
                if chars[c] > 2:
                    return False
    unique_chars = 0
    for i in chars.values():
        if i == 1:
            unique_chars += 1
            if unique_chars > 1:
                return False
    return True

def palindromePermutation2(string):
    string = string.lower()
    bit_flag = 0
    for c in string:
        if c.isalpha():
            bit = ord(c) - ord(' ')
            if bit >= 0:
                bit_flag ^= (1 << bit)
    return not(bit_flag & (bit_flag-1))

test1 = 'Lc8rjxLmpUJ1LYaiQWf6ZVepm27lzDWUcwcLEm73MqeJsj6nWOUHRxa75kxN5G0FPvscHOvFkIAeWfvIDFgkR4fNrbmLCmD9PUMN'
test2 = 'nvL6dZkUe8Vl4cQGelYEpurvjfhziwHNYFZZznwdKrwbNoteI9e9iPl0njJM7sj5QflQJ1L28PhdVmQMGGtFt0EAPgKo2cCOupNM'
test3 = s1 = ''.join([chr((i % 26) + 97) for i in range(512)])

print('First algorithm using hash map')
t0 = time()
print(palindromePermutation('racecar'))
print(palindromePermutation('areccra'))
print(palindromePermutation('derp'))
print(palindromePermutation('poop'))
print(palindromePermutation('opop'))
print(palindromePermutation('taco cat'))
print(palindromePermutation(test1 + test2 + test3))
t1 = time()
print('Time: ', (t1-t0))
print()
print('Second algorithm using bit mask')
t0 = time()
print(palindromePermutation2('racecar'))
print(palindromePermutation2('areccra'))
print(palindromePermutation2('derp'))
print(palindromePermutation2('poop'))
print(palindromePermutation2('opop'))
print(palindromePermutation2('taco cat'))
print(palindromePermutation2(test1 + test2 + test3))
t1 = time()
print('Time: ', (t1-t0))
