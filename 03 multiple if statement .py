# if elif else ladder


a=int(input("enter your age: "))

#if statement no. 1
if(a%2==0):
    print("a is even")

# end of if statement no. 1

#if statement no. 2
if(a>=19):
    print("you are above the age of consent")
    print("good for you")
elif(a<0):
    print("you are entring an invalid age")

elif(a==0):
    print("you are entring 0 which is not a valid age")    
else:
    print("you are below of the age of consent")    
#end of if statement no. 2
print("end of the program")    