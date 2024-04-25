# exception handling
try:
    a=int(input("enter first value"))
    b=int(input("enter second value"))
    print(a,b)
except Exception as abc:
    print(abc)
finally:
    print("hello student")
print("thank you......")            