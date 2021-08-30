# variables
p = 0
r = None
t = None

# code
def simple_interest(p,r,t,with_principal): # defining simple interest calc func
    if(with_principal): # whether to return new balance or return interest
        return (r*t/100+1)*p # returns total balance
    return (r*t/100)*p # returns interest


p = int(input('Principal Amount? '))
r = int(input('Rate? '))
t = int(input('How long (years)? '))
print('Interest is '+str(simple_interest(p,r,t,False)))
print('Balance is '+str(simple_interest(p,r,t,True)))
