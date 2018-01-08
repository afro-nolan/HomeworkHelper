#Calculates formulas from given data
import math
def area_triangle():
    b = float(input("Enter breadth of triangle: "))
    h = float(input("Enter height of triangle: "))
    area = 0.5 * b * h
    print "Area of triangle is: ", float(area)

def area_circle():
    r = float(input("Enter radius: "))
    area = 3.14 (r ** 2)
    print "Area of circle is: ", float(area)

def circum_circle():
    r = float(input("Enter radius: "))
    circ = 2 * 3.14 * r
    print "Circumference of circle is ", float(circ)
         
def area_rectangle():
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    area = l * w
    print "Area of Rectangle is ", float(area)

def sur_area_cylinder():
    h = float(input("Enter height: "))
    r = float(input("Enter radius: "))
    area = 2 * 3.14 * r * h
    print "Surface Area of cylinder is ", float(area)

def volume_cylinder():
    r = float(input("Enter radius: "))
    h = float(input("Enter height: "))
    volume = 3.14 * (r ** 2) * h
    print "Volume of cylinder is: ", float(volume)

def pythagoras():
    s = float(input("Enter side: "))
    s1 = float(input("Enter side: "))
    hyp = math.sqrt((s**2) + (s1 ** 2))
    print "Hypotheneuse is: ", float(hyp)
    
def slope():
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))
    slope = float((y2 - y1) / (x2 - x1))
    print "Slope is: ", float(slope)
    
def midpoint():
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))
    x_cor = (x1 + x2) / 2
    y_cor = (y1 + y2) / 2
    mid = str(x_cor) + "," + str(y_cor)
    print "(" + mid + ")"

def arithmetic_series():
    a = float(input("Enter first term: "))
    d = float(input("Enter common difference: "))
    n = float(input("Enter n: "))
    term = float(a + (n-1) * d)
    print "Nth term is: ", float(term)
                  
print "Formulas: "
print "1. Area Of A Triangle"
print "2. Area of A Circle"
print "3. Circumference Of A Circle"
print "4. Area Of A Rectangle"
print "5. Surface Area Of Cylinder"
print "6. Volume Of Cylinder"
print "7. Pythagoras' Theorem"
print "8. Slope of a line"
print "9. Midpoint Of A Line"
print "10. Arithmetic Series"

formula = raw_input("Enter number of formula: ")

#Area of triangle
if int(formula) == 1:
    area_triangle()

#Area of circle  
elif int(formula) == 2:
    area_circle()
  
#Circumference of circle
elif int(formula) == 3:
    circum_circle()
    
#Area of rectangle
elif int(formula) == 4:
    area_rectangle()
    
#Surface Area of cylinder
elif int(formula) == 5:
    sur_area_cylinder()

#Volume of cylinder
elif int(formula) == 6:
    volume_cylinder()
    
#pythagoras
elif int(formula) == 7:
    pythagoras()

#Slope    
elif int(formula) == 8:
    slope()
    
#midpoint   
elif int(formula) == 9:
    midpoint()
    
#arithmetic series
elif int(formula) == 10:
    arithmetic_series()
    
    
   
    