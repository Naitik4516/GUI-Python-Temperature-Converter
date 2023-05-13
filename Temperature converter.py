from tkinter import *
from tkinter.ttk import Combobox

UNITS = [
    "C",
    "F",
    "K"
]

def conv():
    from_ = from_unit.get()
    to_ = to_unit.get()
    temperature_ = temperature.get()
    result_ = temperature_

    match from_:
        case "C":
            match to_:
                case "F":
                    result_ = (temperature_ * 9/5) + 32
                case "K":
                    result_ = temperature_ + 273.15
        case "F":
            match to_:
                case "C":
                    result_ = (temperature_ - 32) * (5/9)
                case "K":
                    result_ = (temperature_ - 32) * (5/9) + 273.15
        case "K":
            match to_:
                case "C":
                    result_ =  temperature_ - 273.15
                case "F":
                    result_ = (temperature_ - 273.15) * (9/5) + 32

    result.set(f"{temperature_} °{from_} = {result_} °{to_}")
    if str(temperature_).endswith(".0"):
        result.set(f"{int(temperature_)} °{from_} = {int(result_)} °{to_}")
    else:
        result.set(f"{temperature_} °{from_} = {result_} °{to_}")

root = Tk()
root.geometry("700x350+300+200")
root.title("Temperature converter")
Label(root, text="Temperature converter", bg="Black", fg="white", font="Calibri 18 bold", padx=6, pady=6).pack(fill=X)

temperature = DoubleVar(value=0)
from_unit = StringVar(value=UNITS[0])
to_unit = StringVar(value=UNITS[1])
result = StringVar(value="Result will display here")

Label(root, text="From - ", font="Calibri 24").place(x=120, y=77)
temperature_input = Entry(root, textvariable = temperature, font="Lucida 20", borderwidth=3, relief="sunken", bg="white", fg="black", width=7)
from_unit_box = Combobox(root, textvariable=from_unit, values=UNITS, width=2, state="readonly", font=("helvetica",20, "bold") )
Label(root, text="to - ", font="Calibri 22 ").place(x=400, y=75)
to_unit_box = Combobox(root, textvariable=to_unit, values=UNITS, width=2, state="readonly", font=("helvetica",20, "bold") )

ou = Label(root, textvariable=result, borderwidth=5, relief="raised", font="Lucida 12 bold", background="lightgray", width=30, height=2)
ou.place(x=215, y=250)

temperature_input.place(x=220, y=80)
from_unit_box.place(x=340, y=79)
from_unit_box.bind("<<ComboboxSelected>>",lambda e: root.focus())
to_unit_box.place(x=450, y=79)
to_unit_box.bind("<<ComboboxSelected>>",lambda e: root.focus())


Button(root, text="Convert", command=conv, pady=5, padx=2, border=5, relief="raised", font="Helvetica 10 bold" ).place(x=530, y=77)

root.mainloop()