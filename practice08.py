# num = int(input())
# result = num
# if num < 0:
#     result = -result
# print("Absolute Value:", result)

# num1, num2 = map(int, input().split())
# result = "First"
# if num1 < num2:
#     result = "Second"
# print(result)

# num = int(input())
# result = "Single"
# if num // 10 != 0:
#     result = "Double"
# print(result)

# num = int(input())
# if num % 2 != 0:
#     num += 1
# print(num)

# num = int(input())
# result = "Rounded"
# if num % 10 != 0:
#     result = "Not Rounded"
# print(result)

# num = int(input())
# result = "Fifty"
# if num != 50:
#     result = "Other"
# print(result)

# num = int(input())
# result = "VALID"
# if num > 5:
#     result = "INVALID"
# print(result)

# num1, num2 = map(int, input().split())
# if num1 > num2:
#     temp = num1
#     num1 = num2
#     num2 = temp
# print(num1, num2)

# num1, num2, num3 = map(int, input().split())
# if num1 > num2:
#     temp = num1
#     num1 = num2
#     num2 = temp
# if num1 > num3:
#     temp = num1
#     num1 = num3
#     num3 = temp
# if num2 > num3:
#     temp = num2
#     num2 = num3
#     num3 = temp

# print("The middle value is", num2)

# num1, num2, num3 = map(int, input().split())
# avg = (num1 + num2 + num3) // 3
# diff1 = abs(num1 - avg)
# diff2 = abs(num2 - avg)
# diff3 = abs(num3 - avg)
# pos = 1

# min = diff1
# if min > diff2:
#     min = diff2
#     pos = 2
# if min > diff3:
#     min = diff3
#     pos = 3
# print("The position is", pos, ".")

# num1, num2 = map(int, input().split())
# pos1 = 1
# pos2 = 2
# if num1 > num2:
#     pos1 = 2
#     pos2 = 1
# print(num1, pos1)
# print(num2, pos2)

# num = int(input())
# first = num // 100
# rem = num % 100
# result = str(first) + "00"
# if rem >= 50:
#     first = int(first)
#     first += 1
#     result = str(first) + "00"
# print(result)

# num1, num2, num3 = map(int, input().split())
# if num1 > num2 and num2 > num3:
#     print(num1, num2)
# if num2 > num1 and num1 > num3:
#     print(num2, num1)
# if num1 < num2 and num2 < num3:
#     print(num3, num2)
# if num2 > num3 and num3 > num1:
#     print(num2, num3)
# if num1 > num3 and num3 > num2:
#     print(num1, num3)
# if num3 > num1 and num1 > num2:
#     print(num3, num1)

num1, num2, num3, num4 = map(int, input().split())
avg = (num1 + num2 + num3 + num4) / 4

if (avg - num1) > 0:
    print(num1, "is smaller than average")
else:
    print(num1, "is greater than average")
if (avg - num2) > 0:
    print(num2, "is smaller than average")
else:
    print(num2, "is greater than average")
if (avg - num3) > 0:
    print(num3, "is smaller than average")
else:
    print(num3, "is greater than average")
if (avg - num4) > 0:
    print(num4, "is smaller than average")
else:
    print(num4, "is greater than average")
