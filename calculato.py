def sum (a,b):
    print(a+b)

def sub (a,b):
    print(a-b)

def mult(a,b):
    print(a*b)

def div(a,b):
    if a==0:
        print("error")
    else:
        print(a/b)

   
operation=input(" choose:  +,-,*,/")

if operation=="+":
    a=float(input(" enter your first number :"))
    b=float(input(" enter your second number :"))
    sum(a,b)
elif operation=="-":
    a=float(input(" enter your first number :"))
    b=float(input("enter your second number : "))
    sub(a,b)
else:
    a=float(input(" enter your first number :"))
    b=float(input(" enter your second number :"))     
    div(a,b)








