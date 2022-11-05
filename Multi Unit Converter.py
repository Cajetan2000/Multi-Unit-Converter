

import tkinter as tk
import math as m

##------------------------------------#create a GUI window and setting on the screen#-------------------------------------------------------------------------------------------------------------
dom = tk.Tk()
dom.title("Multi-unit convertor")
dom.geometry("1600x1000+0+0")
dom.configure(background='green')
# ----------------------------------------------------#Creating the GUI Frames And setting them on the screen#-----------------------------------------------------------------------------------------------------------


Heading = tk.Frame(dom, width=1000, height=50, bd=16, relief="sunken")
Heading.pack(side=tk.TOP)
Leftside = tk.Frame(dom, width=200, height=3000, bd=10, relief="raise")
Leftside.pack(side=tk.LEFT)
Rightside = tk.Frame(dom, width=600, height=1000, bd=10, relief="sunken")
Rightside.pack(side=tk.RIGHT)
Anotherside = tk.Frame(dom, width=1200, height=2000, bd=18, relief="sunken")
Anotherside.pack(side=tk.TOP)
Anotherframe = tk.Frame(dom, width=100, height=1800, bd=18, relief="sunken")
Anotherframe.pack(side=tk.TOP)

##---------------------------------------------------------#creating a label and naming the GUI#--------------------------------------------------------------------------------------------

mylabe = tk.Label(Heading, font=('verdana', 50, 'bold'), text='Multi-unit convertor', padx=2, pady=2, bd=2,
                  fg="blue").grid(row=0, column=2, sticky=tk.W)

# -----Declaring the state for input buttons------------------------------------------------------------------------------------------------------------------------------------------------
mydistance = tk.DoubleVar()
convert = tk.StringVar()
Distance = tk.DoubleVar()
form = tk.StringVar()


# ----------------------------------------------------#Creating a lists of items keeping the various units and their corresponding formulas in conversion#-------------------------------


def poparameters():
    # -------------------------------------------#creating the lists for all the options of unit to be converter by the user.#----------------------------------------------------------------------------------------------
    Length_list = ["kilometers to miles", "miles to kilometers", "yards to foot", "foot to inches"]
    Mass_list = ["kilograms to tonnes", "tonnes to pounds", "grams to ounce"]
    Temperature_list = ["degreecelcius to kelvin", "fahrenheit to celcius", "fahrenheit to Kelvin"]
    PlaneAngle_list = ["radian to degree", "degree to radian"]
    # -------------------------------------------#creating a list to keep all the formulas to guide the users undderstanding after conversion. #---------------------------------------------------------------------
    Lenth_formular = ["multiply length value by 1.609", "divide length value by 1.609", "mulitiply length value by 3",
                      "multiply lenghth value by 12"]
    Mass_formular = ["divide mass value by 1000", "multiply mass value by 2204.62", "divide mass value by 0.035274"]
    Temperature_formular = ["Degree celcius Value + 273.15", "(number-32)*5/9", "(number-32)*5/9+273.15"]
    PlaneAngle_formular = ["(radian value*180)/pi", "(degree value*pi/180)"]
    # ----------------------------------------------------Writing a code for all the conversions for the various unit-----------------------------------------------------------------------------
    if (length.get() == Length_list[0]):
        convert1 = float(Distance.get() * 1.609)
        convert2 = str(round(convert1, 4)), "Miles"
        mydistance.set(convert2)


    elif (length.get() == Length_list[1]):
        convert1 = float(Distance.get() / 1.609)
        convert2 = str(round(convert1, 4)), "Kilometres"
        mydistance.set(convert2)



    elif (length.get() == Length_list[2]):
        convert1 = float(Distance.get() * 3.0)
        convert2 = str(round(convert1, 4)), "Feet"
        mydistance.set(convert2)

    elif (length.get() == Length_list[3]):
        convert1 = float(Distance.get() * 12.00)
        convert2 = str(round(convert1, 4)), "Inches"
        mydistance.set(convert2)


    elif (mass.get() == Mass_list[0]):
        convert1 = float(Distance.get() / 1000)
        convert2 = str(round(convert1, 4)), "Tonnes"
        mydistance.set(convert2)

    elif (mass.get() == Mass_list[1]):
        convert1 = float(Distance.get() * 2204.62)
        convert2 = str(round(convert1, 4)), "Pounds"
        mydistance.set(convert2)



    elif (mass.get() == Mass_list[2]):
        convert1 = float(Distance.get() * 0.035274)
        convert2 = str(round(convert1, 4)), "Ounce"
        mydistance.set(convert2)

    elif (temperature.get() == Temperature_list[0]):
        convert1 = float(Distance.get() + 273.15)
        convert2 = str(round(convert1, 4)), "Kelvin"
        mydistance.set(convert2)

    elif (temperature.get() == Temperature_list[1]):
        convert1 = float(Distance.get() - 32) * 5 / 9
        convert2 = str(round(convert1, 4)), "Celcius"
        mydistance.set(convert2)

    elif (temperature.get() == Temperature_list[2]):
        convert1 = float(Distance.get() - 32) * 5 / 9 + 273.15
        convert2 = str(round(convert1, 4)), "Kelvin"
        mydistance.set(convert2)

    elif (plane_angle.get() == PlaneAngle_list[0]):
        convert1 = float(Distance.get() * 180 / m.pi)
        convert2 = str(round(convert1, 4)), "Degree"
        mydistance.set(convert2)

    elif (plane_angle.get() == PlaneAngle_list[1]):
        convert1 = float(Distance.get() * m.pi / 180)
        convert2 = str(round(convert1, 4)), "Radian"
        mydistance.set(convert2)

    # ------------------------------------------------------------These block of code is used to pop up the formular for each conversion done at a time--------------------------------------------------
    for i in range(0, len(Length_list)):
        if (length.get() == Length_list[i]):
            pop1 = str(convert.get())
            pop2 = str(pop1), Lenth_formular[i]
            form.set(pop2)

    for i in range(0, len(Mass_list)):
        if (mass.get() == Mass_list[i]):
            pop1 = str(convert.get())
            pop2 = str(pop1), Mass_formular[i]
            form.set(pop2)

    for i in range(0, len(Temperature_list)):
        if (temperature.get() == Temperature_list[i]):
            pop1 = str(convert.get())
            pop2 = str(pop1), Temperature_formular[i]
            form.set(pop2)

    for i in range(0, len(PlaneAngle_list)):
        if (plane_angle.get() == PlaneAngle_list[i]):
            pop1 = str(convert.get())
            pop2 = str(pop1), PlaneAngle_formular[i]
            form.set(pop2)


# ----------------------------------------These block of codes work on the conversion of the first item in list1 and displays the result and the formula


# This function also work for the reset button in the GUI which set all the components to an intial start after use or before use.

def Reset():
    mydistance.set("0.0")
    Distance.set("0.0")
    convert.set(" ")
    form.set("Formula= ")
    length.set("LENGTH")
    mass.set("MASS")
    temperature.set("TEMPERATURE")
    plane_angle.set("PLANE ANGLE")


##-----------------------------------------#Creating all the Entries widgets that recieves entries and show result in the GUI#------------------------------------------------------------------------------------------------

first_entry = tk.Entry(Anotherside, textvariable=Distance, bd=2, width=27, justify='center', bg='violet',
                       fg='white')  # This entry recieves the values to be converted
first_entry.grid(row=3, column=0)

second_entry = tk.Label(Anotherframe, textvariable=mydistance, bd=2, width=27, bg='yellow', fg='black',
                        # This entry box displays the results after conversions
                        relief='groove')
second_entry.grid(row=3, column=0)
third_entry = tk.Label(Rightside, textvariable=form, bd=2, width=35, bg='yellow', fg='black',
                       # The third entry widget shows the formulae for every conversion between two units
                       relief='groove')
third_entry.grid(row=0, column=3)

# ----------------------------------------------Creating the buttons for controlling the codes in the Graphic User Inteface------------------------------------------------------------------
first_button = tk.Button(Leftside, text='convert', padx=2, pady=2, bd=10, fg="red",
                         font=('verdana', 18, 'bold'), width=10, height=3, command=poparameters).grid(row=1, column=0)
second_button = tk.Button(Leftside, text='Reset', padx=2, pady=2, bd=10, fg="green",
                          font=('verdana', 18, 'bold'), width=10, height=3, command=Reset).grid(row=2, column=0)
third_button = tk.Button(Leftside, text='Exit', padx=2, pady=2, bd=10, fg='black',
                         font=('verdana', 18, 'bold'), width=10, height=3, command=exit).grid(row=3, column=0)
# ---------------------------------#Creating The Option menus for the user to choose his option of unit conversions--------------------------------------------------------------------------------------------------------------------------------------------------------


length = tk.StringVar()
length.set("LENGTH")
drop1 = tk.OptionMenu(dom, length, "kilometers to miles", "miles to kilometers", "yards to foot",
                      "foot to inches")  # -------------OPtions for units conversions  involving only lengths.
drop1.pack()

mass = tk.StringVar()
mass.set("MASS")
drop2 = tk.OptionMenu(dom, mass, "kilograms to tonnes", "tonnes to pounds",
                      "grams to ounce")  # --------------------Options for units involoving only masses
drop2.pack()

temperature = tk.StringVar()
temperature.set("TEMPERATURE")
drop3 = tk.OptionMenu(dom, temperature, "degreecelcius to kelvin", "fahrenheit to celcius","fahrenheit to Kelvin")  # -------Options for units involving only Temperature
drop3.pack()

plane_angle = tk.StringVar()
plane_angle.set("PLANE ANGLE")
drop4 = tk.OptionMenu(dom, plane_angle, "radian to degree","degree to radian")  # ------------------------Options for units involving only Plane Angle.
drop4.pack()

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
dom.mainloop()
