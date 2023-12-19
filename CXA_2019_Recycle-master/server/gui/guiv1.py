import tkinter
from tkinter import *
import tkinter.font as font

gui = Tk(className='Python Examples - Button')  #initalises
gui.geometry("500x200")  #sets the dimensions

gui.title("CODE::D") #title of window
            
myFont = font.Font(family='Helvetica', size=50, weight='bold') #define font


##################################################################
########FUNCTION TO SCAN BARCODE, PLACE CODE INSIDE###############
##################################################################
def activate_event(): #called when button is pressed
    btn.destroy()
    
    loading_message = tkinter.Label(gui, text = "Scanning...", fg = "green", bg = "white")
    loading_message['font'] = myFont
    loading_message.pack(ipady = 50, ipadx = 70, expand = True)
    
####scan():                     
#       mat = get_material()  #PLACEHOLDER
#       loading_message.destroy()
#       material_message = tkinter.Label(gui, text = mat, fg = "black", bg = "yellow")
#       material_message['font'] = myFont
#       material_message.pack(ipady = 120, ipadx = 100, expand = True)
#################################################################
#################################################################


    


    


btn = Button(gui, text='SCAN', bg='black', fg='red', command = activate_event) # create button

btn['font'] = myFont # apply font to the button label

btn.pack(ipady = 50, ipadx = 70, expand = True) # add button to gui window



gui.mainloop() 
