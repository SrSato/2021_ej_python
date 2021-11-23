import utilidades

palabra=utilidades.pideFrase("Por favor, dame una palabra: ")

total_char=len(palabra)
last_char=palabra[-1]
thrd_char=palabra[2]

res=f'La palabra \"{palabra}\" tiene {total_char} carácteres.\nSu última posición es para \"{last_char}\" y su tercera posición es para \"{thrd_char}\"'

print(res)