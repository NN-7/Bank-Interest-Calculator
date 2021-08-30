# imports
import xlsxwriter

# variables
p = 0
r = None
t = None

#objects
interest_wb = xlsxwriter.Workbook(r'C:\Users\darks\git\Bank-Interest-Calculator\interest.xlsx') #making the workbook

# code
def worksheet_formatter(name):
    worksheet = interest_wb.add_worksheet(name)
    worksheet.write(0,0, 'Time')
    worksheet.write(1,0, 'Principal')
    worksheet.write(2,0, 'Rate')
    worksheet.write(3,0, 'Interest')
    worksheet.write(4,0, 'Balance')
    worksheet.write(5,0, 'Increase')
    return worksheet

def simple_interest(p,r,t): # defining simple interest calc func
    si_worksheet = worksheet_formatter('Simple Interest') # creating simple interest worksheet
    si_worksheet.write(0,1, str(t))
    si_worksheet.write(1,1, str(p))
    si_worksheet.write(2,1, str(r))
    si_worksheet.write(3,1, str((r*t/100)*p))
    si_worksheet.write(4,1, str((r*t/100+1)*p))
    si_worksheet.write(5,1, str((r*t/100)*p))

p = int(input('Principal Amount? '))
r = int(input('Rate? '))
t = int(input('How long (years)? '))
simple_interest(p,r,t)
interest_wb.close()
