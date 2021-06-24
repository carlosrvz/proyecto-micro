# Importamos la libreira de PySerial
import serial
from time import localtime, strftime

# Crea un objeto de tipo serial llamado ser y a continuación se seleccionan los parámetros
ser = serial.Serial()
# Parámetros
ser.port = 'COM3'               # Ruta en la cual se conecta el micro
ser.baudrate = 115200           # Velocidad de transmisión que se configuró en él
ser.open()                      # Se abre el puerto

''' Se genera un archivo temporal llamado dht con el método append que nos
permite agregar nuevos datos a la lista el cual se designa con 'a' y por
ultimo la codificación utf-8 '''

# Crea un ciclo while que se repita indefinidamente
while(True):
    temp_file = open('data.txt', 'a', encoding = 'utf-8')
    line = ser.readline()           # Lee una línea de texto del puerto serie
    print(line)                     # Imprime esa línea
    temp_file.write(strftime("%d %b %Y %H:%M:%S ", localtime()))
    temp_file.write(line.decode())  # Agrega la línea al archivo de texto
    temp_file.close()

ser.close()                 # Se cierra el puerto
