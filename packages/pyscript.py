import serial
import time
from win10toast import ToastNotifier

port = "COM5" 
baud_rate = 9600  

toaster = ToastNotifier()

ser= serial.Serial(port, baud_rate)

on_not_dis = False
start_time = time.time()
while True:
    message = ser.readline().strip().decode()
    if on_not_dis==False:
        toaster.show_toast("SFDK message", "Device on \n be safe wile using your device \n follow the rules", duration=2, icon_path=r'logo.ico')
        on_not_dis=True
   
    now_time = time.time()
    if message == "Time Exceeded":
        toaster.show_toast("SFDK alert", "The time limit for screen usage have exceeded \n please wait until cooldown completes!", duration=2 , icon_path=r"logo.ico")

    if message == "Too Close":
        toaster.show_toast("SFDK alert", "Your eyes are too close to the \n screen try to move a little far away", duration=2 , icon_path=r"logo.ico")

    if message == "Cooldown not complete":
        toaster.show_toast("SFDK alert", "You can't use your device until and unless the cooldown completes ! \n give your eyes some rest", duration=2, icon_path=r"logo.ico")

    