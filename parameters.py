
def default(name='Dinesh Kumar' , dept='IT'):
    '''This is default parameter,it will return name and department of the student'''
   
    info = print(f'Name:{name}')
    info= print(f'Dept:{dept}')
    return info

default()


def keyword_par(age,year,clg_name):
    ''' This is a keyword parameter, it does not reutrn'''
    print(f'age:{age}')
    print(f'Year:{year}')
    print(f'College Name:{clg_name}')
keyword_par(age=21,clg_name='UCEV',year='4th')



def position_par(place,mob_no):
    '''This is position parameter,
        it returns place and mobile number'''
    home_town = print(f'Home Town:{place}')
    mobile_no = print(f'Contact No:{mob_no}')
    return home_town,mobile_no
position_par('Villupuram',9998887776)



def kwargs_par(**subject):
    '''this is the arbitary key word argument(kwargs)'''
    
    for key, value in subject.items():
        sub = key
        marks = value
        print(f'{sub} : {marks}')

print('________________________________\n')


print('Marks Obtained:\n')

kwargs_par(Maths = 76,English =87,science = 90,Tamil=95,social=97 )

print('')


def args_par(*average):
    '''This is the args argument.'''
    mark = 0
    for i in average:
        mark+=i
    average = mark/len(average)
    print(f'Percentage : {average}')

args_par(76,87,90,95,97)
        