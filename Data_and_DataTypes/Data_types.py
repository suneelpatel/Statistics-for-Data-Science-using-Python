# Types of Data

# 1. Qualitative Data: “Data Associated with the quality in different categories”

# (a). Ordinal Data

marks=int(input("Enter your percentage"))

if(marks<=40):
    print("Fail")
elif((marks>40)&(marks<=50)):
    print("Second Class")
elif((marks>50)&(marks<=60)):
    print("First Class")
elif(marks>=60):
    print("Congratulations!! You got distinction")

# [“Girls and boys are differentiated based on the answer given by them.]


# (b). Nominal Data

ans1=input("Would you like to go for shopping? if yes then type Y / y else N/n")
ans2=input("Do you love talking on any topic? if yes then type Y / y else N/n")

if(((ans1=='Y')|(ans1=='y'))&((ans2=='Y')|(ans2=='y'))):
    print("Welcome to girls club")
else:
    print("Sorry boys, you can not join the club")

# [“Grade are given to students according to their score on the exam”]


#-------------------------------------------------------------------------------------------

# 2. Qantitative Data : “Data associated with Quantity which can be measured”

# (a). Discrete Data : Product_List(in fixed quantity)

Product_List = {"Samsung":500, "Apple":30, "Nokia":10, "LG":450, "Sony":200}
print(Product_List)


# (b). Continuous Data = Weight of Patients(in Kg)
Patients_Weight = {"P_ID001":86.5, "P_ID002":91.3, "P_ID003":45.8, "P_ID004":78.2, "P_ID005":80.3}
print(Patients_Weight)
