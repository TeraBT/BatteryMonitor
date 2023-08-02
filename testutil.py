import psutil
import sys
import winsound
import ctypes

winsound.Beep(1000, 1000)
ctypes.windll.user32.MessageBoxW(0, "Erorr", "mess", 0)
ctypes.windll.user32.MessageBoxW(0, "12", "23", 0)

battery = psutil.sensors_battery()
percentage = battery.percent
def bell():
    sys.stdout.write('\r\a')
    sys.stdout.flush()
bell()
print("Percentage: %s%%" % percentage)