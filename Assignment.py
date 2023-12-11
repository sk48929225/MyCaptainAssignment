
# assigment 0 1
import math
r=float(input("enter the radius"))
area=math.pi*(r*r)
print("area of circle with " + str(r) + " is: " , str(area))



# assigment 0 2
filename= input("enter the filename:")
f_extns = filename.split(".")
print("the extension of the file is :" + repr(f_extns[-1]))
