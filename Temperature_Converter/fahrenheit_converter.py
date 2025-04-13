def to_celsius(temp):
    cel_temp = temp - 32
    cel_temp = 5*cel_temp
    cel_temp = cel_temp/9
    return float(cel_temp)

def to_kelvin(temp):
    kel_temp = temp-32
    kel_temp = kel_temp*5
    kel_temp = kel_temp/9
    kel_temp = kel_temp+273.15
    return float(kel_temp)