listaEdad = []

def clase():
    for i in range(3):  
      
      nombre = input("dime tu nombre:")
      edad = int(input("dime tu edad:"))
  
      compañero = (nombre,edad)
      listaEdad.append(compañero)
    listaEdad.sort(key=lambda x:x[1])
    asistente = listaEdad[0][0]
    prof = listaEdad[-1][0]

    print(f" dds {asistente} {prof}")

#clase()

