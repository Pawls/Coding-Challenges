from collections import OrderedDict

def merge_the_tools(s, k):
    s = list(s)
    for i in range(0,len(s),k):
        t = s[i:i+k]
        u = list(OrderedDict.fromkeys(t))
        print(''.join(u))

