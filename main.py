# imports
import xlsxwriter

# variables
p = 0
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

def compound_interest(p,r,t):
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

p = int(input('Principal Amount? '))
r = int(input('Rate? '))
t = int(input('How long (years)? '))
compound_interest(p,r,t)
simple_interest(p,r,t)
interest_wb.close()
