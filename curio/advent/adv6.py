import utilidades

input = utilidades.leer("input05.txt")

input = input.split("\n")
input.pop(input.index(input[-1]))

print(input)

print(input[0][2])

oxygen = input
co2 = input

for pos in range(0, 12):
    count = 0
    for elem in oxygen:
        if int(elem[pos]) == 1:
            count = count+1
    print(f"De {len(oxygen)} en la posicion {pos} hay {count} 1")
    if count >= len(oxygen)/2:
        criterio = 1
    else:
        criterio = 0
    print(f"Lo que más mola es {criterio}")
    new = []
    if len(oxygen) > 1:
        for elem in oxygen:
            if int(elem[pos]) == criterio:
                new.append(elem)
        oxygen = new
#             co2.append(out)
print("O:", len(oxygen))
print(oxygen[0])

for pos in range(0, 12):
    count = 0
    for elem in co2:
        if int(elem[pos]) == 1:
            count = count+1
    print(f"De {len(co2)} en la posicion {pos} hay {count} 1")
    if count >= len(co2)/2:
        criterio = 0
    else:
        criterio = 1
    print(f"Lo que menos mola es {criterio}")
    new = []
    if len(co2) > 1:
        for elem in co2:
            if int(elem[pos]) == criterio:
                new.append(elem)
        co2 = new
#             co2.append(out)
print("CO2:", len(co2))
print(co2[0])

total_o = 0
total_co2 = 0
for num in range(0, 12):
    total_o = total_o + int(oxygen[0][num]) * 2**(11-num)
    total_co2 = total_co2 + int(co2[0][num]) * 2**(11-num)

print(total_o*total_co2)
# print(len(co2))
# print(oxygen)
