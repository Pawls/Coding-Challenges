def oneAway(s1, s2):
    if s1 == s2:
        return True
    if len(s1) >= len(s2):
        s1 = list(s1)
        s2 = list(s2)
    else:
        temp = s1
        s1 = list(s2)
        s2 = list(temp)
        
    for i in range(len(s1)):
        if i > len(s2)-1:
            s2.append('')
        if s1[i] == s2[i]:
            continue
        else:
            # Check replace
            temp = s1.copy()
            if len(s1) == len(s2):
                temp[i] = s2[i]
                return temp == s2
            
            # Check delete            
            if len(s1) > len(s2):
                del temp[i]
                return temp == s2

            # Check insert
            temp = s2.copy()
            temp.insert(i, s1[i])
            return temp == s1


while(1):
    print(oneAway(input(),input()))
