def to_fahrenheit(temp):
    fahr_temp = 9*temp
    fahr_temp = fahr_temp/5
    fahr_temp = fahr_temp+32
    return float(fahr_temp) 

def to_kelvin(temp):
    kel_temp = temp + 273.15
    return float(kel_temp)