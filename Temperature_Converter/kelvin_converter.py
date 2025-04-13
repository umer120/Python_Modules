def to_celsius(temp):
    cel_temp = temp-273.15
    return float(cel_temp)

def to_fahrenheit(temp):
    farh_temp = temp-273.15
    farh_temp = farh_temp*1.8
    farh_temp = farh_temp+32
    return float(farh_temp)