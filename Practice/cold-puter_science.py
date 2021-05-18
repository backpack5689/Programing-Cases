input()
temps = input().split(" ")
days_below_zero = 0
for day in temps:
    if int(day) < 0:
        days_below_zero = days_below_zero + 1

print(days_below_zero)
