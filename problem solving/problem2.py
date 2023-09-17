def reverse_word(string):
    words = string.split()
    reversed_words = [word[::-1] for word in words]
        
    reversed_string = ' '.join(reversed_words)
    
    return reversed_string

input_string = input('enter any sentence :')

output = reverse_word(input_string)

print(output)