# question 1.1 Take a number from the user and print sum from 1 to that number 
# number = int(input("enter the number :"))
# sum_number =0
# for i in range (1,number+1):
#     sum_number = sum_number+i
# print("the sum of 1 to",number,"is",sum_number)


    
# question 1.2) Take a number from the user and print all prime numbers from 1 to that number 
# number = int(input("enter the number : "))
# for i in range (1,number+1):
#     if (i>1):
#         for j in range (2,i):
#             if (i%j ==0):
#                 break
#         else :
#             print(i)

# or
            
            
# def is_prime(input_number):
#     for iteration_counter in range(2,input_number//2):
#         if input_number%iteration_counter == 0:
#             return False
#     return True
# print("passing 3 was : ", is_prime(3))
# print("passing 13 was : ", is_prime(13))
# print("passing 9 was : ", is_prime(9))
    
    
    # question 3 Take a number from the user and print all Odd numbers from 1 to that number 
# number = int(input("enter the number : "))
# for i in range (1,number+1):
#     if( i%2 != 0):
#         print (i,end=" ")
        
        # question 4 Take a number from the user and print all even numbers from 1 to that number 
        
# number = int(input("enter the number : "))
# for i in range (1,number+1):
#     if( i%2 == 0):
#         print (i,end=" ")


# question 5 5) Take a number from the user and print fibonacci sequence till that number
	# eg : fibonnaci sequence for 5 is 0,1,1,2,3,5

# number = int(input("enter the number :"))

# a=-1
# b=1
# for i in range (-1,number+1):
#     c=a+b
#     if(c>=number+1):
#         break
#     print(c,end=" ")
#     a=b
#     b=c