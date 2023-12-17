from tkinter import *

def calculate_total_pay():
    wage = float(e1.get())
    regular_hours = float(e2.get())
    overtime_hours = float(e3.get())

    # Calculation for total pay
    regular_pay = wage * regular_hours
    overtime_pay = wage * 1.5 * overtime_hours
    total_pay = regular_pay + overtime_pay

    # Display the total pay in the entry field
    e4.delete(0, END)
    e4.insert(0, total_pay)

master = Tk()
Label(master, text='Enter the wage').grid(row=0)
Label(master, text='Enter the regular hours').grid(row=1)
Label(master, text='Enter the overtime hours').grid(row=2)
Label(master, text='The total weekly pay is').grid(row=3)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)

calculate_button = Button(master, text="Calculate", command=calculate_total_pay)
calculate_button.grid(row=4, column=0, columnspan=2)

mainloop()