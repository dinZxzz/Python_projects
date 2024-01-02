import re
input = ['dinesh1234@gmail.com','dinesh2345@gmail,com','@dinesh005@gmail.com']
def email(mail):
    pattern = re.compile(r'^[a-zA-Z0-9-_]+@[a-zA-Z0-9-_]+\.[a-z]{3}')
    return bool(pattern.match(mail))
for mail in input:
    if email(mail):
        print(f'{mail} is the valid email') 
    else:
        print(f'{mail} is not valid email')