import math
print("Name : Mahek Gala ")
print("Roll No : 11")
n=int(input("Enter number of elements : "))
yin=0
for i in range(0,n):
      x=float(input("X = "))
      w=float(input("W = "))
      b=float(input("B = "))
      yin = yin + x*w +b
print("Yin" , yin)
binary_sigmoidal = (1 / (1 + (math.e**(-yin))))
print("Binary Sigmoidal = " , round(binary_sigmoidal,3))                    
bipolar_sigmoidal = (2 / (1 + (math.e**(-yin))))+1
print("Bipolar Sigmoidal = " , round(bipolar_sigmoidal,3))  
