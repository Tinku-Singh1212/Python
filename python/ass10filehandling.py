'''def writedata():
    a=input("enter about yourself")
    myfile=open("ip2.text","w+")
    myfile.write(a)
    myfile.close()
    while stop==exit:
        myfile.close()
writedata()'''   
story=input("write about yourself")

while "stop" not in story:
    story=input()

print(story)
    