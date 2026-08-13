NUM_EMPOYEES = 6

def main():
    hours = [0] * NUM_EMPOYEES
    
    for index in range(NUM_EMPOYEES):
        print('Enter the hours worked by employee ', \
            index + 1, ': ', sep='', end='')
        hours[index] = float(input())
        
    pay_rate = float(input('Enter the hourly pay rste: '))
    
    for index in range(NUM_EMPOYEES):
        gross_pay = hours[index] * pay_rate
        print('Gross pay for employee ', index + 1, ': $', \
            format(gross_pay, ',.2f'), sep='')

main()
