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
global volume_base
global distance_base
global weight_base
global weight_units

#function to change values of Comboboxes
def change_units(event):
    volume_units = []
    distance_units = []
    weight_units = []
    if unit_type_select.get() == "Volume":
        for key in volume_base.keys():    
            volume_units.append(key)
        start_unit.config(values=volume_units)
        convert_unit_to.config(values=volume_units)
    if unit_type_select.get() == "Distance":
        for key in distance_base.keys():
            distance_units.append(key)
        start_unit.config(values=distance_units)
        convert_unit_to.config(values=distance_units)
    if unit_type_select.get() == "Weight":
        for key in weight_base.keys():
            weight_units.append(key)
        start_unit.config(values=weight_units)
        convert_unit_to.config(values=weight_units)

def calc_units():
    if unit_type_select.get() == "Volume":
        #base unit of measure = mL
        for key in volume_base.keys():
            if base_unit.get() == key:
                calc_val = float(start_value.get()) * volume_base[key]
        for key in volume_base.keys():  
            if converted_unit.get() == key:
                calc_val = float(calc_val / volume_base[key])
        
    if unit_type_select.get() == "Weight":
#         #base unit of measure = mg
        for key in weight_base.keys():
            if base_unit.get() == key:
                calc_val = float(start_value.get()) * weight_base[key]
        for key in weight_base.keys():
            if converted_unit.get() == key:
                calc_val = float(calc_val / weight_base[key])
    if unit_type_select.get() == "Distance":
        #base unit of measure = mm
        for key in distance_base.keys():
            if base_unit.get() == key:
                calc_val = float(start_value.get()) * distance_base[key]
        for key in distance_base.keys():
            if converted_unit.get() == key:
                calc_val = float(calc_val / weight_base[key])
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
volume_base = {"mL": 1, "L": 1000, "fl. oz.": 29.754, "cups": 240, "pints": 473.176, "quarts": 946.353, "gallons": 3785.41, "Tbsp": 15, "tsp": 5}
weight_base = {"mg": 1, "g": 1_000, "kg": 1_000_000, "oz.": 28349.5, "lbs.": 453592, "US ton": 907200000}
distance_base = {"mm": 1, "cm": 10, "m": 1_000, "km": 1_000_000, "inches": 25.4, "feet": 304.8, "yards": 914.4, "miles": 1609000}

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