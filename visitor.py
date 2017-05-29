#-------------------------------------------------------
#
# Author: Laert Pires
# Version: 1.0
# Date: 29/05/2017
#
# Description: Randomly generates shapes and computes its area.
#
# Usage: python visitor.py
#
#
# History
#-------------------------------------------------------
# v1.0 - Laert Pires - Initial version
#
#


#
# Imports section
#
import math 
import random

#
# Main Interface Class Shape
#

class Shape(object):

   # constructor
   def __init__(self, type):
      self.type = type
      return

   # visitor
   def accept(self, visitor):
      visitor.visit(self)

   # calculate area
   def getArea(self):
        return


#
# Contrete Class Rectangle
#   

class Rectangle(Shape):

   # constructor
   def __init__(self, width, height):
      Shape.__init__(self, type)
      self.type  = self.__class__.__name__
      self.width = width
      self.height = height

#
# Concrete Class Circle
#

class Circle(Shape):

   # constructor
   def __init__(self, radius):
      Shape.__init__(self, type)
      self.type = self.__class__.__name__
      self.radius = radius

#
# Concrete Class Triangule
#

class Triangle(Shape):

   # constructor
   def __init__(self, a, b, c):
      Shape.__init__(self, type)
      self.type = self.__class__.__name__
      self.a = a
      self.b = b
      self.c = c   

#
# Visitor Class
#

class Visitor:
    def __str__(self):
        return self.__class__.__name__

#
# Class AreaVisitor for the shapes class 
#

class AreaVisitor(Visitor):

   def visit(self, shape):
       if shape.type == "Rectangle":
          return print ("\n" + str(shape.type) + " Area: " + str(round(shape.width * shape.height,2)) + "\n")
       elif shape.type == "Circle":
          return print ("\n" + str(shape.type) + " Area: " + str(round(math.pi*(shape.radius**2),2)) + "\n")
       elif shape.type == "Triangle":
          perimeter = (shape.a + shape.b + shape.c)/2  
          return print ("\n" + str(shape.type) + " Area: " + str(round(math.sqrt(perimeter * (perimeter - shape.a) * (perimeter - shape.b) * (perimeter - shape.c)),2)) + "\n") 
       else:
          return print ("\n" + shape.type + "\n")
        

#
# Function to generate random values for shapes
#

def shapesGen(n): 

    rand_shapes=[Rectangle( random.randint(1,n), random.randint(1,n)), Circle(random.randint(1,n)), Triangle( random.randint(4,n), random.randint(5,n), random.randint(4,n))]

    return rand_shapes


#
# Main section to generate random values and calculate areas
#

def main():

   print ("\n.... Generating Area values for shapes .... \n") 

   # iterate through the lists of shapes and apply the areaVisitor
   areavisitor = AreaVisitor()
   
   for shap in shapesGen(9):
       shap.accept(areavisitor)

   print ("\n........................................... \n")
   

if __name__ == "__main__":
    main()

