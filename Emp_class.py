# class Employee():
    
#     #class variable
#     depart_name='DHPCSA'
     
#      #class method
#     @classmethod
#     def department_name(cls,depart_name):
#         cls.dept_name=depart_name
  
           
#     #instance variables
#     def __init__(self,in_emp_id,in_emp_salary,in_mgr_id):
#         self.emp_id=in_emp_id
#         self.emp_salary=in_emp_salary
#         self.mgr_id=in_mgr_id
    
#     def display_emp_details(self):
#         print("Emp ID is: ",self.emp_id)
#         print("Emp Salary is: ", self.emp_salary)
#         print("MGR ID is: ", self.mgr_id)
#         print("Department Name is : ", self.depart_name)  #access class variable inside constructor using self
#         print("Department Name is : ", Employee.depart_name)  #access using class name
        
        
#     @staticmethod    
#     def field_expertise():
#         print("Field Expertise are: Cloud, Python, Networking, Linux")
        
# def main():
#         e=Employee(1,5000,100)
#         print(type(e))
        
#         e.display_emp_details()
#         e.field_expertise()
#        # #Employee.department_name(depart_name='DHPCSA')
#        # #print("Depatment is: ",Employee.dept_name,Employee.depart_name)
        
    
# main()

# #,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
# import random

# class Airlines():
    
#     #ch_dep_city="Varanasi"
#     source_list=['Pune','Patna','Noida','Mumbai','Ayodhya']
#     destination_list=['Delhi','Kolkata','Madurai','Chennai','KanyaKumari']
#     fare_list=[100,200,300,400,500]
#     seat_list=['12f','13g','14j','15e','16y']
#     flight_list=['fl1340','fl1234','el090','gg9898']
#     @classmethod
#     def change_departure_city(cls,c_s_city,c_d_city,c_f_city,c_se_city,c_fl_city):
#         cls.ch_des_city=c_d_city
#         cls.ch_sor_city=c_s_city
#         cls.ch_fare=c_f_city
#         cls.ch_seat=c_se_city
#         cls.ch_flight=c_fl_city
    
#     def __init__(self,in_name,in_source,in_destination,in_fare,in_seat_no,in_flight_no):
#         self.passenger_name=in_name
#         self.p_source=in_source
#         self.p_destination=in_destination
#         self.p_fare=in_fare
#         self.p_seat=in_seat_no
#         self.p_flight_no=in_flight_no

#     def ticket_details(self):
#         print("your Ticket")
#         print("Passenger Name is: ", self.passenger_name)
#         print("Source of Passenger is: ", self.p_source)
#         print("Destination of Passenger is: ", self.p_destination)
#         print("Fare of Passenger is: ",self.p_fare)
#         print("Seat no of Passenger is: ", self.p_seat)
#         print("Flight no of Passenger is :", self.p_flight_no)
#         #print("New Destination is: ",Airlines.ch_dep_city)
#         print("\n")
    
   
        
        
# def main():
    
#     print("\n")
    
#     # n1=str(input("Enter the passenger Name: "))
#     # s1=str(input("Enter the Source: "))
#     # d1=str(input("Enter Destination: "))
#     # f1=int(input("Enter Fare: "))
#     # se1=str(input("Enter seat no: "))
#     # fl1=str(input("Enter the Flight no: "))
#     # print("\n")
    
#     # airline1=Airlines(n1,s1,d1,f1,se1,fl1)
#     # airline1.ticket_details()
#     # Des1=str(input("Enter new Destination: "))
#     # Airlines.change_departure_city(Des1)
#     sor1=random.choice(Airlines.source_list)
#     Des1=random.choice(Airlines.destination_list)
#     far1=random.choice(Airlines.fare_list)
#     seat1=random.choice(Airlines.seat_list)
#     flight1=random.choice(Airlines.flight_list)
#     airline3=Airlines('Vikas',sor1,Des1,far1,seat1,flight1) 
#     airline3.ticket_details()
    
#     #new_d=
#     # Airlines.change_departure_city(str(input("Enter new Destination: ")))
     
#     # airline2=Airlines('Subhashit','Pune','Mumbai',6000,'13E','FL1011')
#     # airline2.ticket_details()
# main()       
    

#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

class Airlines():
    def __init__(self,in_name,in_source,in_destination,in_fare,in_seat,in_flight_no):
      self.p_name=in_name
      self.p_source=in_source
      self.p_destination=in_destination
      self.p_fare=in_fare
      self.p_seat=in_seat
      self.p_flight_no=in_flight_no
      
    def tickets_details(self):
        print("print the passenger name ", self.p_name)
        print("print the passenger source " ,self.p_source)
        print("print the passenger destination ", self.p_destination)
        print("print the passenger fare " ,self.p_fare)
        print("print the passenger seat number ", self.p_seat)
        print("print the passenger flight number " ,self.p_flight_no)
        print("\n")
        
def main():
    airline1=Airlines('vikas','pune','varanasi','5000','12F','ER123')
    airline1.tickets_details
main()































        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        