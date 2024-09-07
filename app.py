'''
The concept of inheritance in python works similary to the world. 
a python class can inherit the behavours of another class reffered to as the superclass.
-> in a python a class can inherit the behaviours of another class reffered to as the superclass.


reduce repetitive code using inheritance.
SUBCLASS -> is a class that inherits from another class. child class.
SUPERCLASS -> a class that is inherited by another class. parent class.
super() is a built in python fucntion that allows us to manipulate the attributes and the methods os a superclass from the body of its subclass.
'''

# to avoid repetition we use inheritance which allows us to create afamily of classes with shared characteristics but all 
# have some unique attributes as well.
# for example when creating a website tthere are users but the user can be an admin, a student or an instructor. while they might have 
# some similarities, they have their differences as well. we then therefore need to create a classes of admin, student and instructor that 
# each of them can inherit some attributes or methods form the superclass or parent class.


'''
WHAT IS INHERITANCE.
this means that they acquire all od the attributes and behvaours of the parent alse called the superclass.
an obejct can directly access public inherite attributes and methods.
However since private attributes are only visible in the defining class the private inherited attribiutes must be accessed
through public inherited methods.
'''

# Basic inheritance 
# defining the superclass. we have  a class vehicle that will act as the parent, or superclass. we sill create child classes 
# also known as subclasses fir different tyes of vehicles such as car.

class Vehicle:

    def __init__(self,wheel_size, wheel_number): #initilization of a wheel_size and number.
        self.wheel_size = wheel_size
        self.wheel_number= wheel_number
    # instance methods that describe some common vehicle behavour.
    def go(self):
        return "vrrrrrrm!"
    
    def fill_up_tank(self):
        return "filling up!"
    


# defining the subclass 
class Car(Vehicle): # we'll use vehicle as an argument for the Car class to note that Car inherits Vehicle.
    # The go() method o the individual car to retur the phrase "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!" this is different than the return value of hte go() mtethod what was inheritef from the vehcle class.
    def go(self):# overwriting inherited methods.
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"


# Class interospection.
'''
when the program is first executed, at the point at which the go() methos is invoked, the interpretatir will first look in the class to which the instance of
car that we are calling the method on belongs.
if it finds a go() method there, it will execute that method. if it does not find such a method there, it will move on
to look in the parent class that this class inherits.

note that we can ask the Car clas what its parent or superclass is whith its __bases__ attribute.
Car.__bases__ -> it will show all the superclass of the Car class. while there is only one here, there are many classes that 
inherit directly from multiple parent classes.
'''

# NOTE.
'''
Private attributes are only visible in the defining class the private inherited attributes must be accessed through 
public inherited methods.

Private Attributes -> private attributes are vatibles that are only accessible within the clas where they are defined.
the cannot be accessed directly from outside the class.

inheritance -> when a class(child class) inherits from another class(parent class) it gains access tot he parents 
methods and attributes.however attributes of the parent class are not directly acessible in the child class.

Accessing private attributes -> to access private attributes of the parent class, the child must use public or protected methods provided 
bythe parent class.
these methods act as intermediaries allowing controlled access to theprivate attributes.

the following are  methods that can be used to access private attributes by the child class. 
    1. Public getter and setter methods. ->
     these are defined in the parent class to provide controlled access to privite attributes.
     the child can call these methods to get or set the value of the private attributes.
    2. protected attributes. -> while not direclty accessing private attributes, you can use protected attributes(
    which are accesible within the clas and its subclasses) to achieve similar functionality.
    
'''

class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def Display(self):
        print(self.name, self.id)

caroline = Person("Caroline", 40195580)
print(caroline.Display())

# creating a child class 
class Caroline(Person):
    def Print(self):
        print("Caroline class Called")

Caroline_details = Caroline("Wanjiru", 40010030)
Caroline_details.Display()
Caroline_details.Print()

# Note that the constructor __init__ function os a class is invoked when we create an object variable
#  or an instance of the class.
# the varibales defined within __init__ () are called instance varibale or objects.

# Check the code below.
# class A:
#     def __init__(self, n='Rahul'):
#         self.name = n

# class B(A):
#     def __init__(self, roll):
#         self.roll = roll

# object = B(23)
# print(object.name)

'''
why an error will occur in the code below?

when you crete an instance of B tje __init__ method of B is called.
the __init__ method of B does not call the __init__ method of A.
THerefire the name attribute is never intinalized in the B instance.
when you try to access object.name, python raises an attributeError because name does not exist in the B instance.
'''
# The correct code of the cide in line 114
'''
To fix this, you need to call the __init__ method of the parent class A within the __init__ method of B.
You can do this using the super() function.
'''

class A:
    def __init__(self, n= "Rahul"):
        self.name = n


class B(A):
    def __init__(self, roll):
        super().__init__() # call the parent's class's __init__ method.
object = B(23)
print(object.name)


# THE SUPER() FUNCTION.
'''
the super () fucntion is a built in function that returns the objects that represent the parent class. it allows to access the parent classes 
methods and attributes in the child class.
Follow the example below.

we have created the object 'obj' of the child class.
when we called the constructor of the child class 'student', it
initialized the data members to the values passed during the object creation.
'''
class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)


class Student(Person):
    def __init__(self, name, age, dob):
        self.sname = name
        self.sage = age
        self.dob =dob
        super().__init__("Rahul", age)
    
    def displayInfo(self):
        print(self.sname, self.sage)
        print(self.name, self.age, self.dob)

obj = Student('Mayank', 23, "10th-07-2002")
print(obj.display())
print(obj.displayInfo())


# Adding of properties.
'''
One of the features that inheritance provides is inheriting the properties if the parent class as well as sdding 
new properties of our own to the child class.
'''

# Different types of python inheritnace.
# there are 5 different types of python inheritance.
'''
1. Single inheritance - when a cild class inherits from only one patent class, it is called single inheritnce.
2. Multiple inheritnces - when  a child class inherits from multiple parent classes, it is called multiple inheritnaces.
3. Multilevel inheritance - when we have a child and grandchil rellationship. this means taht a child class will inherit from 
its parent class which in turn is inheriting from its parent class.
4 heirachle inheritance - this is when multiple classes inherit from the same parent.
5. Hybrid inheritance- a combination of two or more tyoes of inheritance.
'''

# what is method overidding in python
'''
 methid overidding occurs when a child class provied a specific implementation for a methid that is already defined in its parent class.
 the implementation in the child class replces the one in the parent class when the method is called on an instance of the child class.
 
'''