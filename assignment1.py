#find year leap/not
year = int(input("enter year"))
if year%4 ==0 and year%100 != 0:
    print(f"{year} is a leap year")
else: 
    print(f"{year} is a not leap year")