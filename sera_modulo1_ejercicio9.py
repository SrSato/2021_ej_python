import utilidades

temp = utilidades.pideNumero("¿Qué temperatura hace? (en º): ")

if temp < -273.15:
    print("Rompiste el cero absoluto!!! Aurora Strike!!!!!")
elif temp > -273.15 and temp < 0 :
    print("Estamos por debajo del punto de congelación del agua. Burn your Cosmos!!!!")
elif temp == 0 :
    print("Cero grados, ya sabes, ni frio ni calor")
elif temp > 0 and temp < 100 :
    print("Calentica está la agüica, pero aún no hace chup chup")
elif temp == 100 :
    print("Punto de ebullición! Steam está contento")
elif temp > 100 :
    print("Te pasaste, a este paso te quedas sin agua")