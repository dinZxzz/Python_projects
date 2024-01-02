import re
input_str = 'removing unwanted  spaces   in the string  '
input = re.sub('\s+',' ',input_str)
print(input)