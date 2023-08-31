# Assignment 9: Triangle Classification 
# Problem: Write a program that reads the length of three sides of triangle and
# determines whether it is a equilateral (all sides are equal),
# isosceles(two sides are equal), or scalene (no sides are equal)
side_1 = int(input(" Enter first side "))
side_2 = int(input("Enter second side "))
side_3 = int(input("Enter third side  "))
if side_1 == side_2 & side_2 == side_3:
    print(" Equilateral triangle")
elif (side_1 == side_2) | (side_3==side_1) | (side_2 == side_3) :
    print("isoceles triangle")
else :
    print("scalene")
    
#if side_1 == side_2 == side_3:
 #   print(" Equilateral triangle")
#elif side_1 == side_2 or side_3==side_1 or side_2 == side_3 :
 #   print("isoceles triangle")
#else :
 #   print("scalene")
    