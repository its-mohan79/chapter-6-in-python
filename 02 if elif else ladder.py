
# if elif else ladder


a=int(input("enter your age: "))

if(a>=18):
    print("you are above the age of consent")
    print("good for you")
elif(a<0):
    print("you are entring an invalid age")

elif(a==0):
    print("you are entring 0 which is not a valid age")    
else:
    print("you are below of the age of consent")    

print("end of the program")    