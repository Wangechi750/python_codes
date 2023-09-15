#program to prompt hours and rate per hours worked
hrs=float(input("enter hours worked:"))
rate=float(input("enter hourly rate:"))
#calcute gross_pay
gross_pay=hrs*rate
print("grosspay=%.2f"%gross_pay)