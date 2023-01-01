# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment = 1000.0
extra_payment_month = 61
extra_payment_before = 108
mths = 0

while principal > 0:
    mths = mths + 1
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

    if mths >= extra_payment_month and mths <= extra_payment_before:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment

    if principal < 0:
        total_paid = total_paid + abs(principal)

    print(mths, round(total_paid,2), round(principal,2))
print(f'Paid as much as ${total_paid:0.2f} over the span of {mths} months')
