from scripts.polynomialRegression import train_modal,predict_angle
import numpy as np
from arduino.testing_live import connect_arduino,read_values
from scripts.plotGraphs import plot_Graph
import time
from utils.main import get_time
import serial


ser = serial.Serial()
ser.baudrate = 9600
# ---:Try to connect with arduino microcontroller:---
is_connected = True
# is_connected = connect_arduino(ser)

if is_connected:
    # ---:Training of model before live testing with antenna:---
    reg,poly,y,X,X_test,y_pred,y_test =  train_modal()
    # plot_Graph(y,X,X_test,y_pred,y_test,'Antenna Data training using Polynomial Regression')
    index=0
    ans_20=[0.0,0.0,0.0,0.0,0.0,0.0]
    while True:
        # res = read_values(ser)
        # print(res)
        res = [0.44989,0.20209,0.156405,0.01347,0.041055,0.4682]
        for i in range(len(res)):
            res[i] = float(res[i])
            ans_20[i]+=res[i]
        index+=1
        if index==20:
            index=0
            for elem in range(len(ans_20)):
                ans_20[elem]/=20.0
            input_arr = [ans_20]
            input_ = np.asarray(input_arr) 
            X = poly.fit_transform(input_)
            print("Angle at => "+get_time()+"=>")
            print(round(predict_angle(X,reg)[0][0], 3))
            for elem in range(6):
                ans_20[elem]=0.0
        time.sleep(0.08)
else:
    print("Unable to connect with arduino. Try again...")




# ----:Temp Code:----

# reg,poly =  train_modal()
# input_arr = [[0.43426,0.01712,0.03251,0.02761,0.120225,0.235795]]
# input_ = np.asarray(input_arr) 
# X = poly.fit_transform(input_)
# print(predict_angle(X,reg))
