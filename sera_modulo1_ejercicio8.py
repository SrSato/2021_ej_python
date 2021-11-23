import utilidades

cm = utilidades.pideNumero("Dame una medida en cm: ")
inch = cm/2.54
inch=round(inch,2)
print("Esto son",inch, "pulgadas")