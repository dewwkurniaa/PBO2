print('Dewi Kurnia\n210511032\nT121A(R1)\n')

try:
    with open("ini_file.txt") as file:
        data = file.read()

except FileNotFoundError:
        print("File yang diminta tidak ditemukan!")