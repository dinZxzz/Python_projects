import re
 
def mobileno_code(mobile_number):
    output = re.compile(r'^(\+91)(\s*|[\-])[7-9][0-9]{9}$')
    return bool(output.match(mobile_number))
 
mobile_numbers = ['+91 9876543210', '+91-9876543210', '+91 1234567890', '12345678901', '123456789a']
for mobile_number in mobile_numbers:
    if mobileno_code(mobile_number):
        print(f"{mobile_number} is a valid mobile number")
    else:
        print(f"{mobile_number} is an invalid mobile number")