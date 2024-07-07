# import math

# centigrade = int(input())
# fahrenheit = (centigrade * (9 / 5)) + 32
# print(int(fahrenheit))

# num1 = int(input())
# num2 = int(input())
# print(num1 + num2)
# print(num1 - num2)
# print(num1 * num2)
# print(num1 / num2)
# print(num1 // num2)
# print(num1 % num2)
# print(num1 ** num2)

# num1 = int(input())
# print(num1 // 10)
# print(num1 % 10)

# cost = int(input())
# sale_price = int(input())
# profit = sale_price - cost
# profit_ratio = (profit / cost) * 100
# print(profit_ratio)

# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# print("Average:", ((num1 + num2 + num3) / 3))

# monthly_rent = int(input())
# time = int(input())
# used_time = 12 - time
# fixed_expenses = int(input())
# print("Annual Rental Income:", (monthly_rent * used_time) - fixed_expenses)

# units = int(input())
# units_rate = int(input())
# fixed_charges = int(input())

# print("Amount on Units:", (units * units_rate))
# print("Fixed Charges:", fixed_charges)
# print("Total Amount:", (units * units_rate) + fixed_charges)      

# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())

# print("Distance:", int(math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))))

# length = int(input())
# width = int(input())

# print("Area:", length * width)
# print("Perimeter:", 2 * (length + width))

# purchase = float(input())
# repair = float(input())
# sold = float(input())
# print("Result:", sold - (purchase + repair))

# item11 = float(input())
# item21 = float(input())
# item12 = float(input())
# item22 = float(input())

# change1 = item12 - item11
# change2 = item22 - item21

# total_change = change2 + change1
# print("Change 1:", change1)
# print("Change 2:", change2)
# print("Total Change:", total_change)

# price1 = float(input())
# price2 = float(input())
# price3 = float(input())

# print("Difference Second Year:", price2 - price1)
# print("Difference Third Year:", price3 - price2)
# print("Percentage Difference Second Year:", ((price2 - price1) / price1) * 100)
# print("Percentage Difference Third Year:", ((price3 - price2) / price2) * 100)

# basic_salary = int(input())
# house_rent = basic_salary * 0.45
# print("House Rent:", int(house_rent))
# medical_allowance = basic_salary * 0.1
# print("Medical Allowance:", int(medical_allowance))
# gross_salary = basic_salary + house_rent + medical_allowance
# print("Gross Salary:", int(gross_salary))
# provident_fund = gross_salary * 0.05
# print("Provident Fund:", int(provident_fund))
# net_salary = gross_salary - provident_fund
# print("Net Salary:", int(net_salary))

english = int(input())
urdu = int(input())
drawing = int(input())
mathematics = int(input())
science = int(input())
social_studies = int(input())
history = int(input())
physical_education = int(input())

print("English", english,100)
print("Urdu", urdu,100)
print("Drawing", drawing,75)
print("Mathematics", mathematics,100)
print("Science", science,75)
print("Social Studies", social_studies,100)
print("History", history,100)
print("Physical Education", physical_education,75)
print("Total:", english + urdu + drawing + mathematics + science + social_studies + history + physical_education,725)
