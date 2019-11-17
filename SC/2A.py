print("Mahek Gala")
print("Roll No : 11 ")
print("AND NOT function using Mc Culloch Pitts")
print("Enter 4 binary inputs.");
x1inputs=[]
x2inputs=[]
c=input("Press 1 to enter input values or press enter to use default values.")
if(c=="1"):
    for i in range(0,4):
        x1=int(input("Enter x1 : "))
        x1inputs.append(x1)       
        x2=int(input("Enter x2 : "))
        x2inputs.append(x2)
else:
    x1inputs=[1,1,0,0]
    x2inputs=[1,0,1,0]

print("Considering all weights as excitatory.");
w1 = [1,1,1,1]
w2 = [1,1,1,1]
y=[]          
for i in range(0,4):     y.append(x1inputs[i]*w1[i] + x2inputs[i]*w2[i])
print("x1", " x2", " y")
for i in range(0,4):     print(x1inputs[i]," " ,x2inputs[i]," " , y[i])
print("Considering one weight as excitatory and other as inhibitory.");
w1 = [1,1,1,1]
w2 = [-1,-1,-1,-1]
y=[]          
for i in range(0,4):     y.append(x1inputs[i]*w1[i] + x2inputs[i]*w2[i])
print("x1", " x2 ", "y")
for i in range(0,4):     print(x1inputs[i]," ",x2inputs[i]," " , y[i])
print("Applying Threshold = 1")
Y=[]
for i in range(0,4):
    if(y[i]>=1):
        value=1
        Y.append(value)
    else:
        value=0
        Y.append(value)
print("x1 ", "x2 ", "Y")
for i in range(0,4):     print(x1inputs[i]," ", x2inputs[i]," ",Y[i])
