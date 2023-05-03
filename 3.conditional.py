rows = int(input("Enter the number of rows: "))

# It is used to print the space
k = 2 * rows - 2
# Outer loop to print number of rows
for i in range(0, rows):
    # Inner loop is used to print number of space
    for j in range(0, k):
        print(end=" ")
    # Decrement in k after each iteration
    k = k - 1
    # This inner loop is used to print stars
    for j in range(0, i + 1):
        print("$ ", end="")
    print("")

# Downward triangle Pyramid
# It is used to print the space
k = rows - 2
# Output for downward triangle pyramid
for i in range(rows, -1, -1):
    # inner loop will print the spaces
    for j in range(k, 0, -1):
        print(end=" ")
    # Increment in k after each iteration
    k = k + 1
    # This inner loop will print number of stars
    for j in range(0, i + 1):
        print("$ ", end="")
    print("")




#FIZZ buzz
def fizz_buzz():
    number = int(input("Enter a number to start with: "))
    while True:
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)
        play_again = input("Do you want to continue? (y/n)").lower()
        if play_again != 'y':
            break
        number += 1

fizz_buzz()






##Calculator


def my_cal(a,b):
    while True:
        choice=int(input ("Please select your choice: "))
        if choice==1:
           print(f'The sum= {a+b}')
        elif choice==2:
            print(f'The Square= {a*a}')
        elif choice==3:
            print(f'The Eponent={a**b}')
        elif choice==4:
            break
        else:
            print("Enter Valid Choice")
     
print("****************** MENU ************************\n1: Addition\n2: Square\n3: Exponentation\n4: Exit\n")
a,b=int(input("Enter first number: ")),int(input("Enter second number: "))
my_cal(a,b)






n=int(input("Enter the number: "))
x=sum(range(1,n+1))
print(x)



# 3) Take a number from the user and print all Odd numbers from 1 to that number
initial_value = 1
end_value = int(input("Enter the number: "))
for num in range(initial_value, end_value+1):
    if num % 2 != 0:
        print(num)



# 2) Take a number from the user and print all prime numbers from 1 to that number

start = 1
n = int(input("Enter the number:"))
for num in range(start, n+1):
    if (num > 1):
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)






# 4) Take a number from the user and print all Even numbers from 1 to that number
initial_value = 1
end_value = int(input("Enter the number: "))
for num in range(initial_value, end_value):
    if num % 2 == 0:
        print(num)







# # Solve the following using either while/do while loops
# 1) Take a number from the user and print sum from 1 to that number
summ = 0
num = int(input("Enter the number: "))

while (num > 0):
    summ += num
    num -= 1

print('the sum', summ)










# Addition/Squaring/exponenation should be done as part of single function named 
# "my_calculator"
# which takes in type of operation, number1,number2 as input 
# and outputs the answer based on the operation

def my_addition(num_1,num_2):
    sum=num_1+num_2
    return sum
       
def my_square(num_1):
    square=num_1*num_1
    return square

def my_exponent(num_1,num_2):
    expo=num_1**num_2
    return expo

while True:
    print('1. Addition')
    print('2. Square')
    print('3. Exponent')
    print('4. Exit')
    
    choice=int(input('Enter your desired choice: '))

    if choice==1:
        num_1=int(input('Enter first number: '))
        num_2=int(input('Enter the second number: '))       
        print(f'The sum= {my_addition(num_1,num_2)}')
        
        
    
    elif choice==2:
        num_1=int(input('Enter the number: '))
        my_square(num_1)
        print(f'The square= {my_square(num_1)}')
  
    elif choice==3:
        num_1=int(input('Enter first number: '))
        num_2=int(input('Enter the second number: ')) 
        print(f'The exponent= {my_exponent(num_1,num_2)}')
        
    elif choice==4:
        break
    else:
        print('Enter Correct Option')





# 5)Take a number from the user and print fibonacci sequence till that number

End_number = int(input("ENTER THE END VALUE: "))
# Initial Value:
num_1, num_2 = -1, 1
#count = 0

while True:
    num_3 = num_1+num_2
    if num_3>End_number:
        break
    print(num_3,end=" ")
    num_1 = num_2
    num_2 = num_3
    #count += 1
    


#print first 10 natural number
i=1
while i<10:
    print(i)
    i +=1

#taking input from user
x=int(input('Enter Initial Value: '))    
counter=int(input('Enter Initial Value: '))    
j=x
while j<counter:
    print(j)
    j +=1
    




