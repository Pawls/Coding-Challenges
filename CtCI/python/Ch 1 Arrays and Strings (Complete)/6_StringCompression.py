def stringCompress(string):
    ls = list(string)
    if len(string) > 0:
        prev_char = ls[0]
        count = 1
        i = 1
        while i < len(ls):
            this_char = ls[i]
            if this_char == prev_char:
                del ls[i]
                count += 1
            else:
                ls.insert(i, str(count))            
                prev_char = ls[i+1]
                i += 2
                count = 1
        else:
            ls.append(str(count))
    return ''.join(ls) if len(string) > len(ls) else string

while(1):
    print(stringCompress(input()))
