if __name__ == '__main__':
    N = int(input())
    result = []

    for _ in range(N):
        command,*args = input().split()
        if command == "print":
            print(result)
        else:
            exec("result."+command+"("+",".join(args)+")")
