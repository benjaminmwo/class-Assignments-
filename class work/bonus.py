 # program to print bonus
salary=float(input("Enter your salary:"))
years=int(input("Enter years you have worked"))
if years>10:
    print("your bonus is",0.1*salary)
elif (years>=6 and years<=10):
    print("your bonus is=:" ,0.08*salary)
elif(years<6 and years<=10):
    print("your bonus is=:",0.05*salary)

    