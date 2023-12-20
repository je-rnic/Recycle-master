import tkinter
from tkinter import *
import tkinter.font as font
import time
import image_send
import qr_send

gui = Tk(className='Python Examples - Button')  #initalises
gui.geometry("1000x562")  #sets the dimensions


gui.title("CODE::D") #title of window
            
myFont = font.Font(family='Helvetica', size = 100, weight='bold') #define font
myFont2 = font.Font(family='Helvetica', size = 60, weight='bold') #define font
myFont3 = font.Font(family='Helvetica', size = 16, weight='bold') #define font




def scan_barcode(): #called when btn1 is pressed
    btn1.destroy()
    loading_message.pack(ipady = 675, ipadx = 1200, expand = True)
    image_send.send()
    loading_message.after(1000, read_material)
    



def read_material():
    try:
        with open("send_pi.txt", "r") as infile:
            material = infile.read().strip("\n")
            loading_message.destroy()
            global material_message
            material_message = tkinter.Button(gui, text = "Material: " + material + "\n (tap to continue)",
                                              fg = "black", bg = "yellow", command = scan_cardInitaliser)

            material_message['font'] = myFont3
            material_message.pack(ipadx = 500, ipady = 500, expand = True)



    except FileNotFoundError:
        time.sleep(5.0)
        read_material()
    

    
def scan_cardInitaliser():  #called when btn2 is pressed
    material_message.destroy()
 
    btn3.pack(ipady = 675, ipadx = 1200, expand = True)
    

def scan_card(): #called when btn3 is pressed
    btn3.destroy()
    qr_send.send()
    loading_message2.pack(ipady = 675, ipadx = 1200, expand = True)
    loading_message2.after(1000, read_rwpoints)
              


    
def read_rwpoints():  #is called when btn2 is pressed
    loading_message2.destroy()
    try:
        with open("new_points.txt", "r") as infile:
            rwpoints = infile.read().strip("\n")
                    
            rwpoints_display = tkinter.Label(gui, text = "Current Reward Points:\n" +
                                             rwpoints, fg = "red", bg = "yellow")
            rwpoints_display['font'] = myFont3            
            rwpoints_display.pack(ipady = 500, ipadx = 500, expand = True)
            
    except FileNotFoundError:
        time.sleep(5.0)       
        read_rwpoints()

 



    
loading_message = tkinter.Label(gui, text = "Scanning...", fg = "green", bg = "white")
loading_message['font'] = myFont2

loading_message2 = tkinter.Label(gui, text = "Scanning...", fg = "green", bg = "white")
loading_message2['font'] = myFont2

material_message = tkinter.Label(gui, text = "glass", fg = "black", bg = "yellow")

btn1 = Button(gui, text='SCAN', bg='black', fg='red', command = scan_barcode) # create button
btn3 = Button(gui, text = "SCAN ID", bg = "black", fg = "red", command = scan_card)

btn1['font'] = myFont # apply font to the button label
btn3['font'] = myFont2



btn1.pack(ipady = 675, ipadx = 1200, expand = True) # add button to gui window

gui.mainloop() 
