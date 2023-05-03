import re

string1 = 'gaurav1234@gmail.com'
string2 = 'pratik190900234@gmail.com'
string3 = '2009_rocking_person@yahoo.com'
string4 = 'GodFather2022@yahoo.com'
string5 = 'Brocklesner_89_WWE@yahoo.com'
string6 = 'TheRock_WWE@yahoo.com'
string7 = 'JohnCena_WWE@yahoo.com'
string8 = 'Undertaker_Roman_reigns@outlook.com'
string9 = '6789764666@rediffmail.com'
string10 = 'Kane#6789@gmail.com'

my_list = [string1,string2,string3,string4,string5,string6,string7,string8,string9,string10]


# 1) provide me the list of emails that do have special characters of #~`! => .*#.*
pattern= '.*#.*'
# 2) provide me the list of emails that start with numbers => ^[0-9]+.*
pattern= '^[0-9]+.*'
# 3) provide me the list of emails that start with numbers followed by an underscore => ^\d+_.*
pattern= '^\d+_.*'
# 4) provide me the list of emails that start with numbers followed by an underscore or small case characters => ^\d+[_a-z].* or ^\d+.*
pattern= '^\d+[_a-z].*'
# 5) provide me the list of emails that start with numbers followed by an underscore or small case characters or large case characters => ^\d+[_a-z].*
pattern= '^\d+[_a-z].*'
# 6) Provide me list of emails with only numbers before the @ => \d+[@]
pattern= '\d+[@]'
# 7) Provide me list of emails with numbers anywhere before the @ => \d+
pattern= '.*\d+.*'


print(f"Following are the email ids matching the pattern {pattern}")
for elem in my_list:
    test_string = elem
    result = re.search(pattern, test_string)  
    if result:
        print("Email Id :" , result.group(0))



