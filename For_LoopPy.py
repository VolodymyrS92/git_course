a = ['Hey', 'hello', 'goodbye']

print(a[0])
print(a[1])
print(a[2])
# тобто "for"  - для кожного елемента в списку "а"
for element in a:
    print(element)

b = [20, 30, 50, 60]
for num in b:
    print(num)
    print(num)

total_sum = 0
for e in b:
    total_sum = total_sum + e
print(total_sum)
range(1, 5)
print(range(1, 5))
print(list(range(1, 5)))             # range функція яка виконує певний заданий діапазон в списку

for i in range(1, 5):
    print(i)

total_sum2 = 0
for i in range(1, 5):
    total_sum2 = total_sum2 + i     # також знак =+ означає теж саме, тільки скороченому синтаксисі /total_sum2=+i/
print(total_sum2)

print(list(range(1, 100)))

total_sum3 = 0
for i in range(1, 100):
    if i % 3 == 0:
        total_sum3 += i
print(total_sum3)

total_sum3 = 0
for i in range(1, 100):
    if i % 3 == 0 or i % 5 == 0:  # числа які діялться на 3 без залишку або числа які діляться на 5 без залишку
        total_sum3 += i
print(total_sum3)

total1 = 0
for i in range(1, 5):
    total1 += i
print(total1)

total2 = 0
i1 = 0

while i1 < 5:
    total2 += i1
    i1 += 1
print(total2)
# умова і тіло циклу вайл(до того часу), правда чи брехня, в тілі циклу не виконується умова в тілі цикла вайл.

my_list = [7, 5, 4, 4, 3, 2, 1, -5, -10, -15]
total3 = 0
i2 = 0

while my_list[i2] > 0:
    total3 += my_list[i2]
    i2 += 1

total4 = 0
for element in my_list:
    if element <= 0:
        break
    total4 += element

print(total4)
print(total3)

total5 = 0
i5 = 0

while total5 < 10 and my_list[i5] > 0:
    total5 += my_list[i5]
    i5 += 1
print(total5)

names = ['mike', 'Tom', "katy", "Alex"]
for element in names:
    print(element)

for i in range(0, 4):
    print(names[i])

for i in range(len(names)):
    for J in range(i + 1):
        print(names[i])
