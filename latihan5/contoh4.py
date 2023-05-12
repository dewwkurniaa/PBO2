print('Dewi Kurnia\n210511032\nT121A(R1)\n')

dictionary = {"satu": 1, "dua": 2, "tiga": 3}

try:
    value = dictionary["empat"]
    
except KeyError:
    print("Key yang diminta tidak ditemukan pada dictionary!")