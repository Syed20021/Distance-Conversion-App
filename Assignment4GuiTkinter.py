# Assignment 4: Distance Unit Conversion GUI Application
# By: Syed Hassnat Ali
# Professor: Kyle Chapman
# Date: 2022-12-05
# Project Description:
# This program will convert kilometres to miles and vise versa, and also round the converted value by 2 decimal places as the output,

# Imports.
from tkinter import *
from idlelib.tooltip import Hovertip

# Declare our tkinter window object.
window = Tk()

# Use a boolean variable to track the state.
is_km = BooleanVar()

# Functions
def km_to_miles(input_KM):
    Miles = input_KM / 1.60934
    return round(Miles, 2)

def miles_to_km(input_miles):
    Kilometres = input_miles * 1.60934
    return round(Kilometres, 2)

# Function to produce output and effectively show the result.
def get_result(_event = None):
    # Get the text from the input entry field.
    user_input = entry_input.get()
    # Get the state of the radiobuttons and assign it to user_choice.
    user_choice = is_km.get()
    # Input is valid unless we find out it isn't.
    is_valid = True
    
    # User's input is blank; report an error.
    if user_input == "":
        label_output.configure(text = "ERROR: The input must not be blank.")
        is_valid = False

    # If it's still valid, convert it and output it into a widget.
    if is_valid:
        # If Condition is met the program will run (user input is a valid number).
        if user_input.isdigit(): 
            if user_choice == True:
        
                resultmiles = km_to_miles(float(user_input))
                resultmilesoutput = str(user_input) +" Kilometres equals " +str(resultmiles) + " Miles"
                label_output.configure(text = resultmilesoutput)
        # user_choice is False so Miles to Kilometres.
            else:
                resultkm = miles_to_km(float(user_input))
                resultkmoutput = str(user_input) +" Miles equals " + str(resultkm) + " Kilometres "
                label_output.configure(text = resultkmoutput)
        # Produces an error message if users input is not valid.
        else:
            label_output.configure(text = "ERROR: Please enter a valid number.")



# Function to clear all fields; window returns to its default state.
def clear_window(_event = None):
    label_output.configure(text = "")
    entry_input.delete(0, END)
    is_kilometre = True
    radio_kilometre.select()

# Properties on the window.
window.geometry("350x300")
window.minsize(width = 320, height = 180)
window.title("Unit Conversion Calculator")

# Row 0 widgets.
label_input_prompt = Label(text = "Input Number(s) : ")
label_input_prompt.grid(row = 0, column = 0, sticky = E, padx = 5, pady = 5)
entry_input = Entry()
entry_input.grid(row = 0, column = 1, sticky = W, padx = 5, pady = 5)
entry_input_tip = Hovertip(entry_input, text = "Enter the value for distance")

# Row 2 widgets.
radio_kilometre = Radiobutton(text = "Km", variable = is_km, value = True)
radio_kilometre.grid(row = 2, column = 0, padx = 5, pady = 5)
radio_kilometre_tip = Hovertip(radio_kilometre, text = "Km")
radio_mile = Radiobutton(text = "mi", variable = is_km, value = False)
radio_mile.grid(row = 2, column = 1, padx = 5, pady = 5)
radio_mile_tip = Hovertip(radio_mile, text = "mi")

# Row 3 widgets.
label_output = Label(borderwidth = 2, relief = GROOVE, width = 40)
label_output.grid(row = 3, column = 0, columnspan = 2, padx = 5, pady = 5)
label_output_tip = Hovertip(label_output, text = "Displays the coverted value")

# Row 4 widgets.
button_result = Button(text = "Get Result", command = get_result)
button_result.grid(row = 4, column = 0, padx = 5, pady = 5)
button_result_tip = Hovertip(button_result, text = "Click for conversion")
button_reset = Button(text = "Reset", command = clear_window)
button_reset.grid(row = 4, column = 1, padx = 5, pady = 5)
button_reset_tip = Hovertip(button_reset, text = "Click to reset")

# Set up some access keys (hotkeys).
window.bind("<Alt-g>", get_result)
window.bind("<Alt-r>", clear_window)
window.bind("<Return>", get_result)

# Assign weight values to each row in the grid so that they evenly distribute through the application.
for row_index in range(4):
    window.rowconfigure(row_index, weight = 1)
# Assign weight values for each column for the same reason.
for column_index in range(2):
    window.columnconfigure(column_index, weight = 1)

window.mainloop()