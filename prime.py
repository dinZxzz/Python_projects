range1 = int(input('enter your starting number:'))
range2 = int(input('enter the last number:'))
list=[]

flag = False
for num in range (range1,range2 +1):
    if num >1:
        for i in range(2,num):
            if (num%i==0):
                flag =True
                break
        else:
            list.append(num)

   
print('the prime numbers are:')
print(list)
    