### Version 1.2.2

#Version Log:
#1.0 Primary program checking for battery status
#1.1 Window stays on top
#1.2 Close session button added
#1.2.1 Sound deactivated. 27.12.2021
#1.2.2 Window reduplication bug NOT YET fixed. --13.07.2023--
#Idea: don't show for 10 min: button with window destroy and time.sleep
#https://www.geeksforgeeks.org/how-to-bind-multiple-commands-to-tkinter-button/



import psutil
import tkinter as tk
import time
import ctypes
#import winsound



def showMessage(value):

    #winsound.Beep(1000, 1000)
    window = tk.Tk()
    window.wm_attributes("-topmost", 1)
    window.title("Accumulātōris Monitor")

    if(value == "high"):
        warning_high = tk.Label(text="Accumulātōris vῑs satis māgna: %d%%" % percentage,
                               font=("Arial", 15))
        warning_high.pack(padx=50, pady=20)

    if(value == "low"):
        warning_low = tk.Label(text="Accumulātōris vῑs satis parva: %d%%" % percentage,
                              font=("Arial", 15))
        warning_low.pack(padx=50, pady=20)

    ok_button = tk.Button(text="Vῑdῑ!", font=("Arial", 10), command=window.destroy)
    end_program_button = tk.Button(text="Hāc sessiōne nōn adhibēre", font=("Arial", 10), command=exit)
    ok_button.pack(padx=10, pady=(0, 15))
    end_program_button.pack(padx=10, pady=(0, 15))
    window.after(50000, window.destroy)
    window.mainloop()

#TODO this might not be necessary but only putting exit with brackets as command in end_program_button
# but see if this works first, then we can test it with the old setup but I don't think it will do mutch
# def killProgram(window: tk.Tk):
#     window.destroy()
#     exit



while(True):

    try:
        battery = psutil.sensors_battery()
        plugged = battery.power_plugged
        percentage = battery.percent

        if(plugged):
            if(percentage >= 80):
                showMessage("high")
        else:
            if(percentage <= 20):
                showMessage("low")

        time.sleep(60)

    except Exception as error:
        ctypes.windll.user32.MessageBoxW(0, "The following error has occurred: " + error, "Error", 0)
