#Unit converter 
from ast import Str
import tkinter as tk
from tkinter import Entry, Label, OptionMenu, StringVar, Text, ttk
from tkinter.constants import NONE

global unit_type_select 
global start_unit 
global start_value 
global converting_unit
global converted_value
global base_unit
global format_calc_val
global calc_val 

#function to change values of Comboboxes
def change_units(event):
    if unit_type_select.get() == "Volume":
        start_unit.config(values=volume_options)
        convert_unit_to.config(values=volume_options)
    if unit_type_select.get() == "Distance":
        start_unit.config(values=distance_options)
        convert_unit_to.config(values=distance_options)
    if unit_type_select.get() == "Weight":
        start_unit.config(values=weight_options)
        convert_unit_to.config(values=weight_options)

def calc_units():
    if unit_type_select.get() == "Volume":
        #base unit of measure = mL
        if base_unit.get() == "tsp":
            calc_val = float(start_value.get()) * 5
        elif base_unit.get() == "L":
            calc_val = float(start_value.get()) * 1000
        elif base_unit.get() == "fl. oz.":
            calc_val = float(start_value.get()) * 29.754
        elif base_unit.get() == "cups":
            calc_val = float(start_value.get())* 240
        elif base_unit.get() == "pints":
            calc_val = float(start_value.get()) * 473.176
        elif base_unit.get() == "quarts":
            calc_val = float(start_value.get()) * 946.353
        elif base_unit.get() == "gallons":
            calc_val = float(start_value.get()) * 3785.41
        elif base_unit.get() == "Tbsp":
            calc_val = float(start_value.get()) * 15
        else:
            calc_val = float(start_value.get())

        if converted_unit.get() == "L":
            calc_val = float(calc_val / 1000)
        elif converted_unit.get() == "fl. oz.":
            calc_val = float(calc_val / 29.574)
        elif converted_unit.get() == "cups":
            calc_val = float(calc_val / 240)
        elif converted_unit.get() == "pints":
            calc_val = float(calc_val / 473.176)
        elif converted_unit.get() == "quarts":
            calc_val = float(calc_val / 946.353)
        elif converted_unit.get() == "gallons":
            calc_val = float(calc_val / 3785.41)
        elif converted_unit.get() == "Tbsp":
            calc_val = float(calc_val / 15)
        elif converted_unit.get() == "tsp":
            calc_val = float(calc_val / 5)
        else:
            calc_val = float(calc_val)

    if unit_type_select.get() == "Weight":
        #base unit of measure = g
        if base_unit.get() == "mg":
            calc_val = float(start_value.get()) / 1000
        elif base_unit.get() == "kg":
            calc_val = float(start_value.get()) * 1000
        elif base_unit.get() == "oz.":
            calc_val = float(start_value.get()) * 28.3495
        elif base_unit.get() == "lbs":
            calc_val = float(start_value.get()) * 453.592
        elif base_unit.get() == "US ton":
            calc_val = float(start_value.get()) * 907185
        else:
            calc_val = float(start_value.get())
        
        if converted_unit.get() == "mg":
            calc_val = float(calc_val * 1000)
        elif converted_unit.get() == "kg":
            calc_val = float(calc_val / 1000)
        elif converted_unit.get() == "oz.":
            calc_val = float(calc_val / 28.3495)
        elif converted_unit.get() == "lbs":
            calc_val = float(calc_val / 453.592)
        elif converted_unit.get() == "US ton":
            calc_val = float(calc_val / 907185)
        else:
            calc_val = float(calc_val)

    if unit_type_select.get() == "Distance":
        #base unit of measure = m
        if base_unit.get() == "mm":
            calc_val = float(start_value.get()) / 1000
            print("base: "+ str(calc_val))
        elif base_unit.get() == "cm":
            calc_val = float(start_value.get()) / 100
        elif base_unit.get() == "km":
            calc_val = float(start_value.get()) * 1000
        elif base_unit.get() == "inches":
            calc_val = float(start_value.get()) / 39.3701
        elif base_unit.get() == "feet":
            calc_val = float(start_value.get()) * 3.280
        elif base_unit.get() == "yards":
            calc_val = float(start_value.get()) / 1.09361
        elif base_unit.get() == "miles":
            calc_val = float(start_value.get()) * 1609.34
        else:
            calc_val = float(start_value.get())
        print("base before conversion: " + str(calc_val))
        if converted_unit.get() == "mm":
            calc_val = float(calc_val * 1000)
            print("convert mm: " + str(calc_val))
        elif converted_unit.get() == "cm":
            calc_val = float(calc_val * 100)
            print("convert cm: " + str(calc_val))
        elif converted_unit.get() == "km":
            calc_val = float(calc_val / 1000)
        elif converted_unit.get() == "inches":
            calc_val = float(calc_val * 39.3701)
        elif converted_unit.get() == "feet":
            calc_val = float(calc_val / 3.280)
        elif converted_unit.get() == "yards":
            calc_val = float(calc_val * 1.09361)
        elif converted_unit.get() == "miles":
            calc_val = float(calc_val / 1609.34)
        else:
            calc_val = float(calc_val)
    format_calc_val = "{:.3f}".format(calc_val)
    converted_value.set(format_calc_val)
        


root = tk.Tk()
root.title("Unit Converter")

mainframe = tk.Frame(root, padx=3, pady=15, bg="#476072")
mainframe.grid(row=0, column=0, sticky="NWES")
root.resizable(height=False, width=False)
root.columnconfigure(0, weight=30)
root.rowconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)

unit_classes = ["Volume", "Weight", "Distance"]
volume_options = ["mL", "L", "fl. oz.", "cups", "quarts", "pints", "gallons", "Tbsp", "tsp"]
weight_options = ["mg", "g", "kg", "oz.", "lbs", "US ton"]
distance_options = ["mm", "cm", "m", "km", "inches", "feet", "yards", "miles"]

prompt_label = tk.Label(mainframe, text="Select your units, type your value, and press the button", bg="#548CA8").grid(row=0, columnspan=3)
select_type_label = tk.Label(mainframe, text="Select unit type", bg="#548CA8").grid(row=1, column=0, padx=5, pady=10)
unit_type_select = StringVar()
#have to create the combo box and then place it (grid()) on a second line so that it isn't a NoneType object, gives it value??
unit_class = ttk.Combobox(mainframe, width=10, values=unit_classes, textvariable=(unit_type_select))
unit_class.grid(row=1, column=1, sticky="WE")
unit_class.bind("<<ComboboxSelected>>", change_units)

# look at IntVar implementation but stay with this for now
base_unit = StringVar()
start_value = StringVar()

start_label = Label(mainframe, text="Start Value", bg="#548CA8")
start_label.grid(row=2, column=0)
start_entry = Entry(mainframe, width=10, textvariable=start_value).grid(row=2, column=1, padx=5, pady=5)
start_unit = ttk.Combobox(mainframe, textvariable=base_unit, width=10)
start_unit.grid(row=2, column=2, padx=5, pady=5)

converted_unit = StringVar()
converted_value = StringVar()

converted_label = Label(mainframe, text="Converted Value", bg="#548CA8")
converted_label.grid(row=3, column=0)
converted_entry = Entry(mainframe, width=10, textvariable=converted_value).grid(row=3, column=1)
convert_unit_to = ttk.Combobox(mainframe, width=10, textvariable=converted_unit)
convert_unit_to.grid(row=3, column=2)

calc_button = tk.Button(mainframe, text="Calculate", command=calc_units)
calc_button.grid(row=4, column=1, pady=10)
root.mainloop()