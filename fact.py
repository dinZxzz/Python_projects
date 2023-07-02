number= int(input('enter the number:'))
total = 1
if number < 0:
    print('invalid number')
elif number==0:
    print('the factorial for zero is 1')
    
elif number > 1:
    for i in range(1,number+1):
        total= total * i

print(f"the factorial for {number} is {total} ")

