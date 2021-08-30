# imports
import xlsxwriter
from tkinter import *

# variables
p = None
r = None
t = None

#objects
interest_wb = xlsxwriter.Workbook(r'(YOUR PATH)\interest.xlsx') #making the workbook

# code
def worksheet_formatter(name):
    worksheet = interest_wb.add_worksheet(name)
    worksheet.write(0,0, 'Time')
    worksheet.write(1,0, 'Principal')
    worksheet.write(2,0, 'Rate')
    worksheet.write(3,0, 'Interest')
    worksheet.write(4,0, 'Balance')
    worksheet.write(5,0, 'Profit')
    return worksheet

def simple_interest(p,r,t): # defining simple interest calc func
    si_worksheet = worksheet_formatter('Simple Interest') # creating simple interest worksheet
    si_worksheet.write(0,1,str(t))
    si_worksheet.write(1,1,str(p))
    si_worksheet.write(2,1,str(r))
    si_worksheet.write(3,1,str((r*t/100)*p))
    si_worksheet.write(4,1,str((r*t/100+1)*p))
    si_worksheet.write(5,0, '')

def compound_interest(p,r,t): # definining compound interest calc func
    ci_worksheet = worksheet_formatter('Compound Interest') # creating compound interest worksheet
    profit = 0
    for i in range(t+1):
        profit += r/100*p
        ci_worksheet.write(0,i+1,str(i))
        ci_worksheet.write(1,i+1,str(round(p,2)))
        ci_worksheet.write(2,i+1,str(r))
        ci_worksheet.write(3,i+1,str(round(r/100*p,2)))
        ci_worksheet.write(4,i+1,str(round(r/100*p+p,2)))
        ci_worksheet.write(5,t+1,str(round(profit,2)))
        p += r/100*p

def compound_button():
    p = int(principal.get(1.0, "end-1c"))
    r = int(rate.get(1.0, "end-1c"))
    t = int(time.get(1.0, "end-1c"))
    compound_interest(p,r,t)
    interest_wb.close()

def simple_button():
    p = int(principal.get(1.0, "end-1c"))
    r = int(rate.get(1.0, "end-1c"))
    t = int(time.get(1.0, "end-1c"))
    simple_interest(p,r,t)
    interest_wb.close()

def main():
    window = Tk()
    window.geometry('250x250')
    window.title("Bank Interest Calculator")
    compound_btn = Button(window,text = "Compound Interest",command = compound_button)
    compound_btn.place(x = 5,y = 5)
    simple_btn = Button(window,text = "Simple Interest",command = simple_button)
    simple_btn.place(x = 5,y = 35)
    principal = Text(window, height = 1, width = 10)
    principal.place(x = 95, y=100)
    rate = Text(window, height = 1, width = 10)
    rate.place(x = 95, y=125)
    time = Text(window, height = 1, width = 10)
    time.place(x = 95, y=150)
    p_label = Label(window, height = 1, width = 10, text = "Principal:")
    p_label.place(x = 17,y = 100)
    r_label = Label(window, height = 1, width = 5, text = "Rate:")
    r_label.place(x = 18,y = 125)
    t_label = Label(window, height = 1, width = 5, text = "Time:")
    t_label.place(x = 18,y = 150)
    window.mainloop()

main()
