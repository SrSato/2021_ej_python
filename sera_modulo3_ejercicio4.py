lista=[8,9,10]

print(f'4. Los últimos serán los primeros. Antes de tocar tenemos {lista}...')

ultimo=lista.pop(len(lista)-1)
lista.insert(0,ultimo)

print(f'\tEsto quedaría así: {lista}.')
