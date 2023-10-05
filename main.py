import math

# Въвеждане на коефициентите на уравнението
a = float(input("Въведете коефициент a: "))
b = float(input("Въведете коефициент b: "))
c = float(input("Въведете коефициент c: "))

# Изчисляване на дискриминантата
дискриминанта = b**2 - 4*a*c

# Проверка за решения
if дискриминанта > 0:
    решение1 = (-b + math.sqrt(дискриминанта)) / (2*a)
    решение2 = (-b - math.sqrt(дискриминанта)) / (2*a)
    print(f"Уравнението има две реални корени: {решение1} и {решение2}")
elif дискриминанта == 0:
    решение = -b / (2*a)
    print(f"Уравнението има един реален корен: {решение}")
else:
    част_реална = -b / (2*a)
    част_имагинерна = math.sqrt(abs(дискриминанта)) / (2*a)
    корен1 = complex(част_реална, част_имагинерна)
    корен2 = complex(част_реална, -част_имагинерна)
    print(f"Уравнението има два комплексни корена: {корен1} и {корен2}")
