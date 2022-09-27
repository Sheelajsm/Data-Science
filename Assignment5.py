1)Define a property that must have the same value for every class instance (object)

class Student:
    School_name = "Jnakashi Vidya Mandir"
    def __init__(self,name,standard,section):
        self.name = name
        self.standard = standard
        self.section = section
        
Stud1 = Student("Shush",7,"C")
Stud2 = Student("Mann",5,"E")
Stud3 = Student("Milly",1,"A")  


print(Student.School_name)
print(Stud1.name,Stud1.standard,Stud1.section)
print(Stud2.name,Stud2.standard,Stud2.section)
print(Stud3.name,Stud3.standard,Stud3.section)     


O/P:
Jnakashi Vidya Mandir
Shush 7 C
Mann 5 E
Milly 1 A



2) Create Class Vehicle, and inherit the class for creating.Use of atleast 4 Instace Variables and 
   2 Class Variables and 3 Methods

class Vehicle:
    def __init__(self):
        self.SchoolBus = "SJV1"
        self.OfficeCab = "Swift"
        self.Truck = " "
        
    def add_new_vehicle(self,v):
        self.Truck = v
    
        
class new_vehicle(Vehicle):

    def __init__(self):
        super().__init__()
        self.Tractor = "Thar"
        
              
V1 = Vehicle()      
NV1 = new_vehicle()
V1.add_new_vehicle("Mahindra")


print(V1.Truck)
print(NV1.SchoolBus,NV1.OfficeCab)
print(NV1.Tractor)

O/P:
Mahindra
SJV1 Swift
Thar


3)Create Class Vehicle, and inherit the class for creating
	School Bus
	Office Cab
	Truck and
	Tractor
    
class Vehicle:

    def __init__(self,w,c,s):
        self.wheels = w
        self.color = c
        self.seats = s

SchoolBus = Vehicle(6,"Yellow",45)
OfficeCab = Vehicle(4,"white",5)

class new_vehicle(Vehicle):
    def __init__(self,w,c,s)

Truck = Vehicle(18,"Brown", 2)
Tractor = Vehicle(4,"Red",1)

print(SchoolBus.wheels,SchoolBus.color, SchoolBus.seats)
print(OfficeCab.wheels,OfficeCab.color, OfficeCab.seats)
print(Truck.wheels,Truck.color, Truck.seats)
print(Tractor.wheels,Tractor.color, Tractor.seats)


O/P:
6 Yellow 45
4 white 5
18 Brown 2
4 Red 1


#def hello_decorator(func):
        #def inner1():
            #func()
        #return inner1
        
    #def add():
        #print("output = {}".format("Swift","Mahindra")
        
    #x = hello_decorator(add)
    #x()