import celsius_converter as cel_conv
import fahrenheit_converter as far_conv
import kelvin_converter as kel_conv

val = int(input("Input value for temperature : "))

temp = input("Input which type of temp is it ? (C,F,K) : ")


if temp == "C":
    print("Temperature in Celsius :",val)
    print("Temperature in Fahrenheit :",cel_conv.to_fahrenheit(val))
    print("Temperature in Kelvin :",cel_conv.to_kelvin(val))
elif temp == "F":
    print("Temperature in Fahrenheit :",val)
    print("Temperature in Celsius :",far_conv.to_celsius(val))
    print("Temperature in Kelvin :",far_conv.to_kelvin(val))
elif temp == "K":
    print("Temperature in Kelvin :",val)
    print("Temperature in Celsius :",kel_conv.to_celsius(val))
    print("Temperature in Fahrenheit :",kel_conv.to_fahrenheit(val))
else:
    print("WRONG TEMPERATURE!!")