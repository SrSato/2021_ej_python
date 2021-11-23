import utilidades

bueno="@miweb.com"
parada="salir"
mail="rita@thesinger.com"
peritado="incorrecto"

while True:
    mail=input("Por favor, dame un email: ")

    if mail == parada:
        break
    if mail.endswith(bueno) and mail.count("@")==1 and mail.count(" ")==0:
        peritado='correcto'
    else:
        peritado='incorrecto'

    res=f'El e-mail {mail} es {peritado}'
    print(res)

print("Adios...")
