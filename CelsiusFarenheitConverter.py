#converting Farenheit into Celsius


#temperatureF = 23

def convert_to_celsius(temperatureF):
    celsius = round((temperatureF - 32) * (5 / 9), 1)
    if celsius < 0:
        return(str(celsius) +" is freezing temperature")
    else:
        return(str(celsius) +" is above freezing temperature")

#print(convert_to_celsius(temperatureF))

