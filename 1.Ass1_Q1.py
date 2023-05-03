#Accept two numbers from the user and print 




  # Accept two numbers from the user and print 
    #a) addition 
    #b) first number squared 2 
    #c) first number raised to number second number



a = int (input("Enter value of Number 1: "))
b = int (input("Enter value of Number 2: "))
sum =a+b
print ('Addition is : ',sum)

sq = a*a
print ('Square is : ', sq)

Power = a**b
print ('A to the power B : ',Power)



'''Define a variable named "raise_salary_percentage" and get the salary raise 
percentage from the user, Now apply the raise to an employee
with harcoded data Name= 'gaurav' existing_salary = 900 INR and 
print the incremented salary to the console'''


#New salary – Old Salary) / Old Salary * 100 = Hike percentage. 


Name='Gaurav'
Existing_salary = 900
raise_salary_percentage = int(input("Enter the raise percentage = "))
raised_salary = (raise_salary_percentage*Existing_salary+ 100*Existing_salary)/100
print("Revised salary = ", raised_salary)



'''Get the height from the user in cms and display the user height back to console
in foot/feet and inches'''


height_cms = float(input ('Enter the height in cms= '))
print(f"Height in cms = {height_cms} cms")

height_in_feet = int(height_cms//30.48)
height_in_inches = int((height_cms%30.48)/2.54)

print(f"The height is {(height_in_feet)} feet {height_in_inches} inches")






#Get the no of the dollars from the user apply the conversion of 1 dollar = 82 rupees and print the amount to the console in rupees

Number_of_dollars = int(input("Enter Number of Dollars: "))
print(f"In Dollars = {Number_of_dollars} $")
in_rupees = Number_of_dollars*82
rupees = print(f"In Rupees = {in_rupees} ₹")



#Take the source, destination, fare in INR, discount_rate percentage from the user and display the string ex: "fare from mumbai to pune is 300 INR with has a discount of 5%"
source=input("Enter the name of Source: ")
destination=input("Enter the name of Destination: ")
fare=int(input("Enter the fare: "))
discount=int(input("Enter the Discount percentage: "))
my_str= print(f"fare from {source} to {destination} is {fare- (fare*discount/100)} INR with discount of {discount}%")


# Accept String from user and output upper case of the input string 

my_str = input('Enter the string :')
print('Entered String is: ', my_str.upper())


