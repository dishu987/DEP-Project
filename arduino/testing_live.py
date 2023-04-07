import serial
import time
import re

def connect_arduino(ser):
    list=['COM1','COM2','COM3','COM4','COM5','COM6','COM7','COM8','COM9','COM10','COM11','COM12','COM13','COM14','COM15','COM16','COM17','COM18',]
    COM1='COM1'
    COM2='COM2'
    COM3='COM3'
    COM4='COM4'
    COM5='COM5'
    COM6='COM6'
    COM7='COM7'
    COM8='COM8'
    COM9='COM9'
    COM10='COM10'
    COM11='COM11'
    COM12='COM12'
    COM13='COM13'
    COM14='COM14'
    COM15='COM15'
    COM16='COM16'
    COM17='COM17'
    COM18='COM18'
    COM19='COM19'
    time.sleep(1)
    is_connected = False
    i=1
    while True:
        time.sleep(.2)
        print(i)
        ser.port = list[i]
        try:
            ser.open()
            if ser.isOpen()==True:
                print('Connected')
                is_connected=True
                #print('arduino is on COMPORT'.join(i))
                break
            break
        except:
            print('Waiting...')
            i=i+1
            if i==18:
                print('Kindly remove usb cable and try again')
                break   
    return is_connected


def read_values(ser):
    temp = re.findall(r"[-+]?\d*\.?\d+|[-+]?\d+", ser.readline().decode('utf-8'))
    return temp

