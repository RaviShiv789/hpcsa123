# factorial= 1

# num=10
# for i in range(1,num + 1):
#        factorial = factorial*i
# print("The factorial of",num,"is",factorial)

#

# cnt=1
# factorial= 1
# num=int(input("Enter the number for factorial"))
# while(cnt<=num):
#     factorial=factorial*cnt
#     cnt=cnt+1
#     if factorial < 2000:
#         print(factorial)
#     else:
#          print("Factorial is Failed" )    

#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

# def histogram(list_of_ints):
#     for num in list_of_ints:
#         print('*' * num) 
# histogram([4, 9, 7])

#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

# import re

# def is_palindrome(phrase):
#     # Convert the phrase to lowercase and remove non-alphanumeric characters
#     phrase = re.sub(r'[^A-Za-z0-9]', '', phrase.lower())
    
#     # Check if the phrase is a palindrome
#     return phrase == phrase[::-1]

# phrase = "Go hang a salami I'm a lasagna hog."
# if is_palindrome(phrase):
#     print("Yes, it's a palindrome!")
# else:
#     print("No, it's not a palindrome.")

#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

days_in_month = int(input("How many days are in the month? "))
start_day = int(input("What day of the week does the month start on? (0 for Monday, 1 for Tuesday, etc) "))

# Define a list of weekdays
weekdays = [" S", " M", " T ", " W ", "T ", "F", " S"]

# Print the calendar header
print(" ".join(weekdays))

# Print the first row of the calendar
current_day = 1
row = "   " * start_day
while len(row) < 21:
    row += " " + str(current_day).rjust(2)
    current_day += 1
print(row)

# Print the remaining rows of the calendar

while current_day <= days_in_month:
    row = ""
    for i in range(7):
        if current_day <= days_in_month:
            row += " " + str(current_day).rjust(2)
        else:
            row += "  "
        current_day += 1
    print(row)
    
    
 #,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,








































