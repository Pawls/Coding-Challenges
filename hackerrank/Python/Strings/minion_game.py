def minion_game(s):
    vowels = ['A','E','I','O','U']
    kevin = stuart = 0
    length = len(s)
    
    for i,c in enumerate(s):
            if c in vowels:
                kevin += length - i
            else:
                stuart += length - i

    if stuart > kevin:
        print('Stuart',stuart)
    elif kevin > stuart:
        print('Kevin',kevin)
    else:
        print('Draw')

