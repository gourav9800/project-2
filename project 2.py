#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1.Class Definition and Object Creation Create a Python class called "Student" that has
#the following attributes: name, age, and grade. Define an initialization method to initialize
#these attributes when an object of the class is created. Create an instance of the class and set
#the attributes. Finally, print the attributes of the student object.



#Methods in a Class Extend the "Student" class from the previous question. Add a method called "is_passing" that returns
#True if the student's grade is greater than or equal to 50 and False otherwise. Create an instance of the class and
#use this method to check if the student is passing. Display the result.


class Student:
    
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
        

    
    def is_passing(self):
        return self.marks >= 50
students = [student_1, student_2, student_3]

student_1=Student("gourav",24,56)
student_2=Student("rachit",25,80)
student_3=Student("SOURAV",32,35)

for student in students:
    print("Name: " + student_1.name)
    print("Age: " + str(student_1.age))
    print("Grade: " + str(student_1.marks))
    if student.is_passing():
        print(student_1.name + " is passing.")
    else:
        print(student_1.name + " is not passing.")
    print()


# In[ ]:


#Function with Default Parameters Create a Python function called "greet" that takes a name as a parameter and a greeting
#message as an optional parameter with a default value of "Hello". The function should return a formatted greeting 
#message. Test the function by calling it with and without the optional parameter and display the results


def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"


greet_with_default = greet("Alice")  
greet_custom = greet("Bob", "Hi") 

print(greet_with_default)
print(greet_custom)


# In[ ]:


#Function with Variable Number of Arguments Write a Python function called 
#"calculate_average" that takes a variable number of arguments and calculates the average of those numbers. Use this function 
#to find the average of 5, 10, 15, and 20, and display the result.


def calculate_average(num1, num2, num3, num4):
    total = num1 + num2 + num3 + num4
    average = total / 4
    return average


result = calculate_average(5, 10, 15, 20)

print(result)


# In[2]:


#Function with Parameters Write a Python function called "calculate_rectangle_area" that takes two parameters,
#length and width, and returns the area of a rectangle. Call the function with different sets
#of values and display the results.

def calculate_rectangle_area(length, width):
    area = length * width
    return area


area1 = calculate_rectangle_area(4, 6)
area2 = calculate_rectangle_area(5, 10)
area3 = calculate_rectangle_area(3.5, 7)

print(area1)
print(area2)
print(area3)


# In[ ]:




