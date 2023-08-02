import tkinter as tk
import time

window = tk.Tk()
window.title("Test")

warningHigh = tk.Label(text="Battery hoch", font=("Arial", 15))
warningHigh.pack(padx=50, pady=20)
button = tk.Button(text="Intellēxῑ!", font=("Arial", 10), command=window.destroy)
button.pack(padx=10, pady=(0, 15))

button2 = tk.Button(text="Vῑdῑ!", font=("Arial", 10), command=quit)
button2.pack(padx=10, pady=(0, 15))

window.mainloop()
while(True):
    window = tk.Tk()
    button.pack()
    window.mainloop()
    time.sleep(0.5)
    
