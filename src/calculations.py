import math

# Calculating dew point
def dewgamma(thermo, humidity):
    b = 18.678
    c = 257.14
    RH = humidity
    #Below goes just the dew point formula with +-0.1C uncertainty
    T = (thermo[0]+thermo[1]+thermo[2]+thermo[3]+thermo[4])/5
    g = math.log(RH / 100) + ( (b * T) / (c + T) )
    result = (c * g) / (b - g)
    return result
