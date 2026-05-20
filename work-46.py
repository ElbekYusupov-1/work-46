# Array56
# 3 ga karrali indeksdagi elementlardan b massiv hosil qilish

n = int(input("n = "))
a = []

for i in range(n):
    a.append(int(input(f"a[{i}] = ")))

b = []

for i in range(n):
    if i % 3 == 0:
        b.append(a[i])

print("b massiv:", b)
print("Elementlar soni:", len(b))


# Array57
# Avval juft indeksdagilar, keyin toq indeksdagilar

n = int(input("n = "))
a = []

for i in range(n):
    a.append(int(input(f"a[{i}] = ")))

b = []

for i in range(0, n, 2):
    b.append(a[i])

for i in range(1, n, 2):
    b.append(a[i])

print("b massiv:", b)


# Array58
# b[k] = a[0] + ... + a[k]

n = int(input("n = "))
a = []

for i in range(n):
    a.append(int(input(f"a[{i}] = ")))

b = []
summa = 0

for i in range(n):
    summa += a[i]
    b.append(summa)

print("b massiv:", b)


# Array59
# b[k] = (a[0] + ... + a[k]) / k

n = int(input("n = "))
a = []

for i in range(n):
    a.append(int(input(f"a[{i}] = ")))

b = []
summa = 0

for i in range(n):
    summa += a[i]
    b.append(summa / (i + 1))

print("b massiv:", b)


# Array60
# b[k] = a[k] + ... + a[n-1]

n = int(input("n = "))
a = []

for i in range(n):
    a.append(int(input(f"a[{i}] = ")))

b = []

for i in range(n):
    summa = 0

    for j in range(i, n):
        summa += a[j]

    b.append(summa)

print("b massiv:", b)