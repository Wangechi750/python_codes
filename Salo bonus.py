#code to prompt employee forvtheir salary and years of serviceand display net bonus amount
salo=float(input("enter your salo: "))
years_of_service=int(input("enter year of service"))
if years_of_service>10:
    bonus=0.10*salo
    print("bonus: ",bonus)
if years_of_service>=6 and years_of_service<=10:
    bonus=0.08*salo
    print("bonus is: ",bonus)
if years_of_service<6:
    bonus=0.05*salo
    print("bonus is: ",bonus)