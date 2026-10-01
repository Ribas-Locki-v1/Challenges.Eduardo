# You are given a non-negative floating point number rounded to two decimal places Celsius, that denotes the temperature in Celsius.
# You should convert Celsius into Kelvin and Fahrenheit and return it as an array ans = [Kelvin, Fahrenheit].

def convert_celsius(celsius: float) -> list[float]:

    Fahrenheit = (celsius * 9/5) + 32
    Kelvin = celsius + 273


    return([Kelvin, Fahrenheit])


print(convert_celsius(36.50))
print(convert_celsius(122.11))

