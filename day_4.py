# Function as a arguments

def greet(num):
    if num==1:
        return "Good Morning"
    elif num==2:
        return "Good Afternoon"
    elif num==3:
        return "Good Night"
    else:
        return "Good Morning"

def name(name,greet_fun):
    print(name, greet_fun(2))

name("Aman",greet)