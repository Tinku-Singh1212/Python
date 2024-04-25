capital_letter,small_letter,numbers,symbols=0,0,0,0
for i in input("enter the input"):
    if i.isupper():
        capital_letter +=1
    elif i.islower():
        small_letter +=1
    elif i.isdigit():
        numbers +=1
    else :
        symbols +=1
print("capital letter count :-",capital_letter)
print("small letter count :-",small_letter)
print("numbers count :-",numbers)
print("symbols count :-",symbols)                 
