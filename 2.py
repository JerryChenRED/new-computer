import math

numCount = int(input("有幾個數字: "))
numbers = []

print(f"請輸入{numCount}個數字:")
for i in range(numCount):
    inputNum = float(input())
    numbers.append(inputNum)

average = sum(numbers) / len(numbers)

variance = sum((num - average) ** 2 for num in numbers) / len(numbers)
standard_deviation = math.sqrt(variance)

print(f"平均值: {average}")
print(f"標準差: {standard_deviation}")

