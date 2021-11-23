import utilidades

tope_por_menor=10
tope_por_mayor=100

precio_por_menor=12
precio_por_mayor=10
precio_especial=7

unidades=utilidades.pideNumero("¿Cuántas unidades quiere?: ")

if unidades < tope_por_menor:
    tipo = "Compra minorista"
    precio=precio_por_menor    
if unidades > tope_por_menor and unidades < tope_por_mayor :
    tipo = "Compra mayorista"
    precio=precio_por_mayor
if unidades > tope_por_mayor :
    tipo = "Compra especial"
    precio=precio_especial

total=unidades*precio

print("\n",tipo,": \n----------------\nPrecio :",precio,"\nUnidades :",unidades,"\n----------------\nTotal :",total)