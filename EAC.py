age=int(input("please enter age: "))
citizenship=input("enter nationality: ")
print(citizenship.upper())
print(citizenship.lower())
if age>=18 and citizenship in ["Kenyan","Ugandan","Tanzanian"]:
    print("Eligible to vote")
else:
    print("Oops! you are not elegible")