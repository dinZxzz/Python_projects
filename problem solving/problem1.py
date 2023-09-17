def result_calc(string):
    marks = string.split(',')
    results = []
    for mark in marks :
        mark = int(mark)
        if mark>=35:
            results.append('pass')
        elif mark < 100:
            results.append('Enter valid mark')
        else :
            results.append('fail')
            
    string_result = ',' .join(results)
    return string_result

student_mark = input('Enter your subject marks like this (33,47,67,89,90):')

output = result_calc(student_mark)
print(output)            
            