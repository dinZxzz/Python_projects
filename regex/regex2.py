import re
input_str = 'remov1ing num23bers in the s5trin9g'
input = re.sub('\d+','',input_str)
print(input)