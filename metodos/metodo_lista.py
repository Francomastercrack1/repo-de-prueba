#un buen uso espara crear una lista vacia, es decir sin elementos
lista = list(["maquinola",342523,True])

resul =  lista.append("maquinolovich")

#agrega un elemento en una posicion especifica
lista.insert(0,"puto")

#elimina todos lso elementos de la lista 
lista.clear()

#ordenando la lista(si usamos el parametro reverse=true la ordena en reversa)
lista.sort(reverse=True)

#index verificando si un elementod se encuentra en la lista
elemento_encontrado = lista.index(2)

print(elemento_encontrado)