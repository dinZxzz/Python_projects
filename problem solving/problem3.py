def print_alphabet(input):
    for i in range (1,input+1):
        for j in range(input , i,-1):
            print(' ', end='')
        
        for j in range(1 , i):
            print(chr(64+j),end = '')
        for j in range(i, 0, -1):
            print(chr(64 + j), end="")
            
        print()
        
input = int(input('enter the number:'))

print_alphabet(input)