    # program of even or odd with current date
print("*************")    
print("welcome to Delhi")
print("---------------")
print("Even number vehical travels from date 1 to 15")
print("Odd number vehical travels from date 16 to 31")
print("---------------")
veh=int(input("enter the last four digit of your vehical number"))
if  (veh%2==0):
    date=int(input("enter the current date"))
    if  (date<=15):
        print("you are allowed to delhi")
    else:
        print("you are not allowed to delhi")
else:
    date=int(input("enter the current date"))
    if (date>=16):
       print("you are allowed to delhi")     
    else:
        print("you are not allowed to delhi") 
    

