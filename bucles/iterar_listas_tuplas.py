animales  = ["gato","perro"]
numeros = [34,565,43,4532]

#for animal in animales:
#   print(animal)

#forma de iterar dos lista
for animal, num in zip(animales,numeros):
    print(f"recorriendo lista 1:{animal}")
    print(f"recorriendo lista 2:{num}")


#for nume in range(3,7):
#   print(num)


#forma correcta de recorrer una lista con su indice
for num,i in enumerate(numeros):
    resul = num
    resul2 = i
    print(f"el indice es:{resul} y el valor es:{resul2}") 