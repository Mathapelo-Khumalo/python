
try:
    print(x)
except NameError:
    print("variable not defined")
else:
    print("Every thing went wrong")
    
    
    x= -1
    if x <0:
        raise Exception("sorry no numbers below zero")