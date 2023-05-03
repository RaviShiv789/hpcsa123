def my_set_store():
    print("\n Welcome to Our Set Store !!! ")
    print("Please enter a list Comma seperated dictionary elements that you would want to perform Operation Upon")
	
    setA= set()
    setB= set()

    for set_elem in input("Please enter comma seperated elements for the set A : ").split(","):
        setA.add(set_elem.strip())   

    for set_elem in input("Please enter comma seperated elements for the set B : ").split(","):
        setB.add(set_elem.strip())   


    while(True):
        print("\n*************** Menu **********************")
        print("Operations supported by our program are :")
        print("	1: Union")
        print("	2: Intersection ")
        print("	3: A-B")
        print("	4: B-A")
        print("	5: Take a element from user and Display if that element is a member of set B ")
        print("	6: Display number of elements in the set A")
        print(" 7: Display number of elements in the set B")
        print("	8: Add an element taken from the user to the set A")
        print("	9: Add multiple elements taken from the user to the set A")
        print("	10: Remove an element taken from the user from set A")
        print(" 11: Exit")

        choice = int(input("Please enter your choice "))

        if choice   ==1:
            set_union(setA,setB) 
        elif choice ==2:
            set_intersection(setA,setB)
        elif choice ==3:
            set_minus(setA,setB)
        elif choice ==4:
            set_minus(setB,setA)
        elif choice ==5:
            is_member_of_set(setB) 
        elif choice ==6:
            set_display(setA)
        elif choice ==7:
            set_display(setB)
        elif choice ==8:
            set_add_element(setA)
        elif choice ==9:
            set_add_elements(setA)
        elif choice ==10:
            set_remove_element(setA)
        elif choice ==11:
            break
        else:
            print("Invalid Input , Please Try Again !!!!  ")  
            
def set_union(setA,setB):
     print(setA.union(setB))
     
def set_intersection(setA,setB):
    print(setA.intersection(setB))
    
def set_minus(setA,setB):
    print(setA.difference(setB))
    
def set_minus(setB,setA):
    print(setB.difference(setA))
    
def is_member_of_set(setB) :
    print(setB)
    
def set_display(setA):
    print(setA)
    
def set_display(setB):
    print(setB)
    
def set_add_element(setA):
    setA.add(input("Please enter your choice "))
    
def set_add_elements(setA):
    setA.add(input("Please enter your choice "))
			
def set_remove_element(setA):
    setA.discard(input("Please enter your choice "))
    # need to check
my_set_store()			