# find greates of 3 numbers entered by user

no1= int(input("Enter first number: "))
no2= int(input("Enter second number: "))
no3= int(input("Enter third number: "))

if(no1>=no2 and no1>=no3):
    print(no1,"is greatest")
elif(no2>=no1 and no2>=no3):
     print(no2,"is greatest")
else:
      print(no3,"is greatest")