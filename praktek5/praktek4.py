print('Dewi Kurnia\n210511032\nT121A(R1)\n')

dictionary = {"a": 7, "b": 16, "c": 38}

try:
    value = dictionary["d"]
    
except KeyError:
    print("Key yang diminta tidak ditemukan pada dictionary!")