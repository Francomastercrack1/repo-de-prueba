cadena1 = "hola soy dalto el"
cadena2 = "cadena de caracteres 2"

#convierte la cadena de mayuscula
resultado1 = cadena1.upper()

#convierte la cadena de minuscula
resultado2 = cadena1.lower()

#convierte la primera en mayuscula
resultado3 = cadena1.capitalize()

#buscamos una cadena en otra cadena (devuelve -1 si no encuentra coinsidencias)
#busqueda_find = cadena1.find()

#buscamos una cadena en otra cadena (devuelve una excepcion si no hay coinsidencias)
#busqueda_index = cadena1.index()

#si es numerico devolvemos true sino devuelve false
es_numerico = cadena1.isnumeric()

#buscamos una cadena en otra cadena, devuelve la cantidad de veces que coincieda
contar_coincidencias = cadena1.count("a")

#contamosd ciantos caracteres hau en una cadena
contar_caracteres = len(cadena1)

#ramplaza un pedazo de la cadena dada,por otra dada
cadena_nueva = cadena1.replace("el","crack")

print(cadena_nueva)