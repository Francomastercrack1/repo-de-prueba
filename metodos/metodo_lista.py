#un buen uso espara crear una lista vacia, es decir sin elementos
lista = list(["maquinola",2,True])

resul1 =  lista.append("maquinolovich")

#agrega un elemento en una posicion especifica
resul2 = lista.insert(0,"puto")

#elimina todos lso elementos de la lista 
resul3 = lista.clear()

#ordenando la lista(si usamos el parametro reverse=true la ordena en reversa)
resul4 = lista.sort(reverse=True)

#index verificando si un elementod se encuentra en la lista(el valor que le pasemos debe ser igual al de la lista)
#resul5 = elemento_encontrado = lista.index(2)

#elimina un elemento de una lista, pide indice y devuelve valor
resul6 = lista.pop(0)

#removiendo un elemento por su valor
resul7 = lista.remove(True)

#agregando varios elementos a la lista
resul8 = lista.extend([4234,"la concha de la lora"])

print(resul6)