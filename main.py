# imports
import xlsxwriter
from tkinter import *

# variables
p = 0 # principal
r = 0 # rate
t = 0 # time

#objects
interest_wb = xlsxwriter.Workbook(r'(YOUR PATH)\interest.xlsx') #making the workbook

# code
def worksheet_formatter(name):
    worksheet = interest_wb.add_worksheet(name)
    worksheet.write(0,0, 'Time') # making time row
    worksheet.write(1,0, 'Principal') # making principal row
    worksheet.write(2,0, 'Rate') # making rate row
    worksheet.write(3,0, 'Interest') # making interest row
    worksheet.write(4,0, 'Balance') # making balance row
    worksheet.write(5,0, 'Profit') # making profit row
    return worksheet

def simple_interest(p,r,t): # defining simple interest calc func
    si_worksheet = worksheet_formatter('Simple Interest') # creating simple interest worksheet
    si_worksheet.write(0,1,str(t)) # writing time passed
    si_worksheet.write(1,1,str(p)) # writing principal
    si_worksheet.write(2,1,str(r)) # writing the rate
    si_worksheet.write(3,1,str((r*t/100)*p)) # writing the interest
    si_worksheet.write(4,1,str((r*t/100+1)*p)) # writing the balance after interest

def compound_interest(p,r,t): # definining compound interest calc func
    ci_worksheet = worksheet_formatter('Compound Interest') # creating compound interest worksheet
    profit = 0 # profit variable
    for i in range(t+1): # for loop to show progression
        profit += r/100*p # profit counter
        ci_worksheet.write(0,i+1,str(i)) # time passed
        ci_worksheet.write(1,i+1,str(round(p,2))) # new principal (perivous principal+interest)
        ci_worksheet.write(2,i+1,str(r)) # rate 
        ci_worksheet.write(3,i+1,str(round(r/100*p,2))) # interest
        ci_worksheet.write(4,i+1,str(round(r/100*p+p,2))) # balance (principal+interest)
        ci_worksheet.write(5,t+1,str(round(profit,2))) # profit
        p += r/100*p # updating principal to be the perivous principal+the interest

def compound_button(): # code for pressing the compound interest button
    p = int(principal.get(1.0, "end-1c")) # gets input from principal text box
    r = int(rate.get(1.0, "end-1c")) # gets input from rate text box
    t = int(time.get(1.0, "end-1c")) # gets input from time text box
    compound_interest(p,r,t)  # executes compound interest calculator
    interest_wb.close() # closes workbook
    window.destroy()
    
def simple_button(): # code for pressing the simple interest button
    p = int(principal.get(1.0, "end-1c")) # gets input from principal text box
    r = int(rate.get(1.0, "end-1c")) # gets input from rate text box
    t = int(time.get(1.0, "end-1c")) # gets input from time text box
    simple_interest(p,r,t) # executes simple interest calculator
    interest_wb.close() # closes workbook
    window.destroy()

window = Tk() # makes window
window.geometry('250x250') # sets window to be 250x250
window.title("Bank Interest Calculator") # sets window title to "Bank Interest Calculator"
compound_btn = Button(window,text = "Compound Interest",command = compound_button) # creating compound interest button
compound_btn.place(x = 5,y = 5) # placing compound button at 5,5
simple_btn = Button(window,text = "Simple Interest",command = simple_button) # creating simple interest button
simple_btn.place(x = 5,y = 35) # placing compound button at 5,35
principal = Text(window, height = 1, width = 10) # creating principal text box
principal.place(x = 95, y=100) # placing principal text box at 95,100
rate = Text(window, height = 1, width = 10) # creating rate text box
rate.place(x = 95, y=125) # placing rate text box at 95,125
time = Text(window, height = 1, width = 10) # creating time text box
time.place(x = 95, y=150) # placing time text box at 95,150
p_label = Label(window, height = 1, width = 10, text = "Principal:") # creating principal label
p_label.place(x = 17,y = 100) # placing principal label at 17,100
r_label = Label(window, height = 1, width = 5, text = "Rate:") # creating rate label
r_label.place(x = 18,y = 125) # placing rate label at 17,125
t_label = Label(window, height = 1, width = 5, text = "Time:") # creating time label
t_label.place(x = 18,y = 150) # placing time label at 17,150
window.mainloop() # runs tkinter event loop which listens and can react to events (eg. button press)
