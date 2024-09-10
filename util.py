import math
def converter(latitude, longitude):
    offset = 1.0 / 1000.0
    latMax = latitude + offset
    latMin = latitude - offset
    lngOffset = offset * math.cos(latitude * math.pi / 180.0)
    lngMax = longitude + lngOffset
    lngMin = longitude - lngOffset
    return {'latMax/north': str(latMax), 'latMin/south' : str(latMin), 'lngMax/east' : str(lngMax), 'lngMin/west' : str(lngMin)}

