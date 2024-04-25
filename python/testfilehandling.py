def writedata():
    a=input("enter the string")
    myfile=open("ip.text","a")
    myfile.write(a)
    myfile.close()
def readdata():
    myfile=open("ip.text","r")
    print(myfile.read())
    myfile.close()
writedata()
readdata()        