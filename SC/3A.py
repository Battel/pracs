print("Name : Kimberly Moniz")
print("Roll No : 21")

print("Enter 4 binary training pairs")

w1=[0,0,0,0]
w2=[0,0,0,0]

for m in range(0,4):     
     print("Enter 4 binary input values")
     s=[]
     t=[]
    
for i in range(0,4):
    x=int(input())
    s.append(x)

    print("Enter 2 binary target values")

    for i in range(0,2):
        y=int(input())
        t.append(y)
           
    print("s= ",s)
    print("t= ",t)

    

    w1new=[]

    for i in range(0,4):
        newweight1=w1[i] + s[i]*t[0]
        w1new.append(newweight1)
        '''print new weights'''

    for i in range(0,4):
        print("w",(i+1),"1 = ",w1new[i])
    

    w2new=[]

    for i in range(0,4):
        newweight2=w2[i] + s[i]*t[1]
        w2new.append(newweight2)

    for i in range(0,4):
        print("w",(i+1),"2 = ",w2new[i])

    w1=w1new
    w2=w2new
    print(w1)
    print(w2)


print("The final weight matrix is : ")
print("W = ")
for i in range(0,4):
     print(w1[i] , w2[i])


print("Done")     
