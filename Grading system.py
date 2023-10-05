#code to show grading system
sub1=int(input("enter marks for sub1: "))
sub2=int(input("enter marks for sub2: "))
sub3=int(input("enter marks for sub3: "))
sub4=int(input("entet marks for sub4: "))
sub5=int(input("enter marks for sub5: "))
avg=(sub1+sub2+sub3+sub3+sub4+sub5)/5
if avg>=70 and avg<=100:
    print("Grade: A")
if avg>=60 and avg<=69:
    print("Grade: B ")
if avg>=50 and avg<=59:
    print("Grade: C")
if avg>=40 and avg<=49:
    print("Grade: D")
if avg>=0 and avg<=39:
    print("Grade: Fail ")