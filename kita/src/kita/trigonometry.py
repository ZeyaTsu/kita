__pi = 3.141592653589793

def __exp(x:complex):
    return 2.718281828459045**x

def __factorial(n:int):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def deg(radians):
    rad = radians * 180/__pi
    return rad

def rad(deg):
    deg = deg * __pi/180
    return deg

def sin(x:float):
    sinx = (__exp(x*1j) - __exp(x*-1j))/2
    if sinx.imag == 0:
        return sinx.real
    elif sinx.real == 0:
        return sinx.imag
    return sinx

def cos(x:float):
    cosx = (__exp(x*1j) + __exp(x*-1j))/2
    if cosx.imag == 0:
        return cosx.real
    elif cosx.real == 0:
        return cosx.imag
    return cosx

def tan(x:float):
    return sin(x)/cos(x)
