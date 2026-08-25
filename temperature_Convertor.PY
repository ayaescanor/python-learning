def fahrenheit(c):
    print((c*1.8)+32)

def celsius(F):
    print((F-32)*5/9)

choice=float(input(" choose 1: if you want to convert from fahrenheit to celsius , choose 2: if you want to convert from celsius to fahrenheit  "))
if choice==1:
    celsius_temperature=float(input(" enter your temeperature in celsius :"))
    fahrenheit(celsius_temperature)
elif choice==2:
    fahrenheit_temperature=float(input("enter your temperature in fahrenheit : "))
    celsius(fahrenheit_temperature)
    
 


