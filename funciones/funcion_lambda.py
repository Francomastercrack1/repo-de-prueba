numerosPares = [1,2,3,4,5,6,7,8,9]

numPar = filter(lambda x : x%2 == 0, numerosPares)

print(f"los numeros pares son:{list(numPar)}")