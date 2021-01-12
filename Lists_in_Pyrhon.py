# Списки в Пайтон - це тип даних який зберігає в собі ще один тип ланих, List [];

a = [3,5,20]
print(a)
a.append(32)
print(a)

a.append('hi')
print(a)

a.append([5,6])
print(a)


a.pop()
print(a)

a.pop()
print(a)

print(a)
print(a[3])
# [3, 5, 20, 32] -1 виводить останній елемент у списку!
print(a[-1])



