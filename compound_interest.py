"""
Calculate compound interest
Formula
ammount = p(1+r/100) ** T
compound interest = amount - p
P: Principal ammount
R: Rate of interest
T: Time duration


"""

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate : "))
time = float(input("Enter the time : "))
# Two way of using pow of
amount1 = principal * (1+ rate / 100) ** time
amount2 = principal * pow((1+ rate / 100), time)
print("Amount is: ", round(amount1,2))
print("Amount is: ", round(amount2,2))
ci= amount1- principal
print("Compound Intrest is",round(ci,2))