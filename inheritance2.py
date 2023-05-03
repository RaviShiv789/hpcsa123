from Inheritance import Person
# from Inheritance import Person,Sister
class Uncle(Person):
    def __init__(self,name,place_of_residence,buisness):
        super().__init__(name,place_of_residence)
        self.buisness=buisness
    
    def person_info(self):
        super().person_info()
        print("Buisness details are: ",self.buisness) 
        
# Child class 2
class Sister(Person):
    def __init__ (self,name,place_of_residence,exam_subjects):
        super().__init__(name,place_of_residence)
        self.exam_subjects=exam_subjects
    
    def person_info(self):
        super().person_info()
        print("Exam subjects are : ",self.exam_subjects)
        
def main():
# Create object of Uncle
    Uncle1 = Uncle('Jessa', 'USA','Diamonds')
# # # access data
    Uncle1.person_info()

    sis = Sister("Chandan","Patna","Textile")
    sis.person_info()
    
main() 

























