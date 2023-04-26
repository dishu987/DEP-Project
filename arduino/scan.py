import serial
import time
import pandas as pd
import numpy as np
import re


list=['COM1','COM2','COM3','COM4','COM5','COM6','COM7','COM8',
'COM9','COM10','COM11','COM12','COM13','COM14','COM15','COM16','COM17','COM18',]

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
ser = serial.Serial()
ser.baudrate = 9600

i=1

while True:
    time.sleep(.2)
    print(i)
    ser.port = list[i]
    try:

        ser.open()
        if ser.isOpen()==True:
            print('Connected')
            #print('arduino is on COMPORT'.join(i))
            break
        break

    except:
        print('Waiting...')
        i=i+1
        if i==18:
            print('Kindly remove usb cable and try again')
            break


print('Loading...')
index_val = 0

try:
    DF1  = pd.read_csv("data1.csv",header=None)
    if DF1.shape[0]==1:
        DF1 = DF1.iloc[0]
    else:
        DF1 = DF1.iloc[-1]
    index_val = DF1.iloc[0]
    print(index_val)
    index_val+=5
except:
    print("Empty CSV file")


arr1 = [0.0,0.0,0.0,0.0,0.0,0.0]
index=0
ans = 0.0


while True:
    "a1,a2,a3"
    temp = re.findall(r"[-+]?\d*\.?\d+|[-+]?\d+", ser.readline().decode('utf-8'))
    if temp==[]:
        continue
    print(temp)
    for j in range(len(temp)):
        arr1[j]+=float(temp[j])
    index=index+1
    if index==21:
        break


for elem in range(len(arr1)):
    arr1[elem] /=20.0

arr1.insert(0, index_val)
DF = pd.DataFrame(arr1).transpose() 
DF.to_csv('data1.csv', mode='a', index=False, header=False)
print(DF)