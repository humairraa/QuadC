# simple calculator that shows you the same equations qritten in standard, factored, vertex, and inverse
# this calculator will tell you the properties of the parbola based on user the user-input

import math 

# y = x^2 + 5x + 6, x = -2,-3
#a = 1
#b = 5
#c = 6

#user input
print("Neg. numbers are fine, if number does not have + or - in front of it, it is +. if number has - in front, it is - ")
print("Enter your variable values assuming the form ağ¥Â²+bğ¥+c.") 
a = float(input("Input number for ağ¥Â²: "))
b = float(input("Input number for bğ¥: "))
c = float(input("Input number for c: "))

# stating formula / putting it together
outside_sqrt = -b
sqrt_and_inside =  (b**2 - 4*a*c) ** 0.5
under_divide = 2*a

# puting formula together / making it work
formula_one = (outside_sqrt + sqrt_and_inside)
formula_two = (outside_sqrt - sqrt_and_inside) 
solution_one = formula_one / under_divide
solution_two = formula_two / under_divide

#vertex (x,)
x_side = -b / 2*a

# vertex (,y) #a
y_a_side_one = x_side**2
yy_a_side_one = a * y_a_side_one
#b
y_b_side = b * x_side
y_c_side = c

#adding them all
y_side_axis = float(yy_a_side_one) + float(y_b_side) + float(y_c_side)

# for vertex equation (,y) have to make sign opposite
w = -x_side

# factored form
xone_opposite = -solution_one
xtwo_opposite = -solution_two

# domain and range 
domain = '{XER}'
range_r = '{YER'

#axis of symmetry
aos = (0 - 2) ** 0.5 
aos_two = aos + c

#inverse form inside squareroot
molly = -y_side_axis

# 'for the quadratic formula ________, the x-int are:
print("")
#print("If there is a - in front of number, number it negative, otherwise its positive")
print("For the quadratic equation:",str(a)+"ğ¥Â²",str(b)+"ğ¥",str(c) + '...')

print("Standard Form:", "y =",str(a)+"ğ¥Â²",str(b)+"ğ¥",str(c))
print("Factored Form:", "y = ("+ "ğ¥", str(xone_opposite)+ ")" + "(ğ¥", str(xtwo_opposite) +")")
print("Vertex Form:", "y =", "(ğ¥", str(w) + ")Â²", str(y_side_axis))
print("Inverse: y =", str(w), "Â± âğ¥" + str(molly))

print("")

print("PROPERTIES...")
print("1. ğ¥â =", solution_one)
print("2. ğ¥â =", solution_two)
print("3. y-intercept =", c)
print("4. Vertex = (" + str(x_side) + "," + str(y_side_axis) + ")")
print("5. Domain:", domain)
#print("6. Range:", range_r, 'â¥ OR â¤', str(y_side_axis) + "}" + ' **IF A IS + SIGN IS â¥, IF A IS - SIGN IS â¤**')
#print("7. Opens = up (min point) if (+axÂ²) /// down (maximum point) if (-axÂ²)")

#range
if a > 0:
    print("6. Range:", range_r, 'â¥', str(y_side_axis) + "}")
else:
    print("6. Range:", range_r, 'â¤', str(y_side_axis) + "}")

#way parabola opens
if a > 0:
    print("7. Opens: up (minimum point)")
if a < 0:
    print("7. Opens: down (maximum point)")

print('8. min/max =', y_side_axis)
print("9. Axis of symmetry = (" + str(x_side) + ",", str(aos_two) + ")")

