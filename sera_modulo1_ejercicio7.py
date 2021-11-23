import utilidades

compra=utilidades.pideNumero("Dame el valor de la compra: ")

iva = compra * 0.21
total = compra + iva

print("Tu compra vale",compra,"€","\nGenera un I.V.A. de",iva,"€","\nEn total deberás pagar",total,"€")
