n = int(input('Enter the number of people:'))
time = int(input('Enter the number of time to pass:'))

current = 1
forward = True

for _ in range(time):
    
    if forward:
        current +=1
    else:
        current -=1
    
    
    if current == n+1:
        forward =False
        current = n
    elif current == 0:
        forward = True
        current = 1
        
print(current)


