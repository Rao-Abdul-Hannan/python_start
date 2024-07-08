# num1, num2, num3 = map(int, input().split())
# sum = num1 + num2 + num3
# print("Sum:", sum)

# num1, num2, num3 = map(int, input().split())
# print(str(num1) + "*" + str(num2) + "*" + str(num3))

# num1, num2 = map(int, input().split())
# print("Numerator:", num1 + num2)
# print("Denominator:", num1 * num2)

# units, units_rate, fixed_charges = map(int, input().split())
# print("Total Amount:", (units_rate * units) + fixed_charges)

price1, quantity1, discount1 = map(int, input().split())
price2, quantity2, discount2 = map(int, input().split())
price3, quantity3, discount3 = map(int, input().split())

cash_discount = float(input())

total_price1 = price1 * quantity1
total_price2 = price2 * quantity2
total_price3 = price3 * quantity3

amount1 = total_price1 - (total_price1 * (discount1 / 100))
amount2 = total_price2 - (total_price2 * (discount2 / 100))
amount3 = total_price3 - (total_price3 * (discount3 / 100))

total_amount = amount1 + amount2 + amount3
cash_discount_amount =  total_amount * (cash_discount / 100)

print("Item 1:", amount1)
print("Item 2:", amount2)
print("Item 3:", amount3)

print("Total Amount:", total_amount)
print("Cash Discount:", cash_discount_amount)
print("Net Amount:", total_amount - cash_discount_amount)
