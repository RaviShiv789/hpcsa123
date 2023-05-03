#Parent class 1
class Person:
    def __init__(self,name, place_of_residence) :
       self.name=name
       self.place_of_residence=place_of_residence
       
    def person_info(self):
        print('Inside Person class')
        print('Name:', self.name, 'Residence:', self.place_of_residence)

# # Child class
# # from Inheritance import Person,Sister
# class Uncle(Person):
#     def Uncle_info(self,buisness):
#         print('Inside Uncle class')
#         print('Buisness of Uncle is: ', buisness)
        
# # Child class 2
# class Sister(Person):
#     def sister_info(self, exam_subjects):
#         print('Inside Sister class')
#         print('Exam subjects', exam_subjects)
# # Create object of Uncle
# Uncle1 = Uncle()
# # access data
# Uncle1.person_info('Jessa', 'USA')
# Uncle1.Uncle_info('Diamonds Buisness'"\n")


# sis = Sister()
# sis.person_info('Chandra','Patna')
# sis.sister_info('Maths')


