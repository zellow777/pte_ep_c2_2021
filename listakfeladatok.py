import random

# 1.
daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 30, 31, 30]
month = ["Január", "február", "március", "április", "május", "június",
         "július", "agusztus", "szeptember", "október", "november", "december"]

monthAndDays = []
for i in range(len(month)):
    monthAndDays.append(month[i])
    monthAndDays.append(daysInMonth[i])
print(monthAndDays)

# 2.
list = [1, 1200, 6, 8, 32, 55, 100]

max = 0
for i in list:
    if i > max:
        max = i

print(max)

# 2. így is lehet
list.sort(reverse=True)
print(list[0])

for i in range(20):
    list.append(random.randint(1, 101))

