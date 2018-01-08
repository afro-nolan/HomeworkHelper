#Calculates formulas from given data
import sqrt from math
print "Formulas: "
print "1. Area Of A Triangle"
print "2. Area of A Circle"
print "3. Circumference Of A Circle"
print "4. Area Of A Rectangle"
print "5. Surface Area Of Cylinder"
print "6. Volume Of Cylinder"
print "7. Pythagoras' Theorem"
print "8. Slope of a line"

formula = raw_input("Enter number of formula: ")

#Area of triangle
if int(formula) == 1:
    b = float(input("Enter breadth of triangle: "))
    h = float(input("Enter height of triangle: "))
    area = 0.5 * b * h
    print "Area of triangle is: ", float(area)

#Area of circle  
elif int(formula) == 2:   
    r = float(input("Enter radius: "))
    area = 3.14 (r ** 2)
    print "Area of circle is: ", float(area)
    
#Circumference of circle
elif int(formula) == 3:
    r = float(input("Enter radius: "))
    circ = 2 * 3.14 * r
    print "Circumference of circle is ", float(circ)
    
#Area of rectangle
elif int(formula) == 4:
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    area = l * w
    print "Area of Rectangle is ", float(area)
    
#Surface Area of cylinder
elif int(formula) == 5:
    h = float(input("Enter height: "))
    r = float(input("Enter radius: "))
    area = 2 * 3.14 * r * h
    print "Surface Area of cylinder is ", float(area)

#Volume of cylinder
elif int(formula) == 6:
    r = float(input("Enter radius: "))
    h = float(input("Enter height: "))
    volume = 3.14 * (r ** 2) * h
    print "Volume of cylinder is: ", float(volume)

#pythagoras
elif int(formula) == 7:
    s = float(input("Enter side: "))
    s1 = float(input("Enter side: "))
    hyp = math.sqrt((s**2) + (s1 ** 2))
    print "Hypotheneuse is: ", float(hyp)

#Slope    
elif int(formula) == 8:
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))
    slope = float((y2 - y1) / (x2 - x1))
    print "Slope is: ", float(slope)
    
   
    