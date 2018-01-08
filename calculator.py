#Calculates formulas from given data

print "Formulas: "
print "1. Area Of A Triangle"
print "2. Area of A Circle"
print "3. Circumference Of A Circle"
print "4. Area Of A Rectangle"
print "5. Surface Area Of Cylinder"

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
    
    