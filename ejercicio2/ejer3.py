#mport random
#
#um = random.randint(1,10)
#
#umm = 0
#
#hile numm < num:
#   numm +=1
#   numeroAleatorio = int(input("adivina el numero:"))
#   if num < numeroAleatorio:
#
#       print("lo siento, el nuemro es menor")
#
#   elif num > numeroAleatorio:
#
#       print("lo siento, el numero es mayor")
#       
#   else:
#       print("!!adivinaste!!")
#       break

#----------------------------------------------------------------

#
#horasTrabajadas = int(input("dime tus horas trabajadas:"))
#
#costePorHora = int(input("dime el coste de la hora:"))
#
#pagaCorrespondiente = horasTrabajadas * costePorHora
#
#print(f"horas trabajadas:{horasTrabajadas},y el total a pagar es:{pagaCorrespondiente}")

#---------------------------------------------------------
#
#nteroPositivo = int(input("ingresa un num entero positivo:"))
#
#umaEnteroPositivos = enteroPositivo * (enteroPositivo + 1) /2
#
#rint(f"la suma de los numeros enteros desde 1 hasta {enteroPositivo} es {sumaEnteroPositivos}")

#-------------------------------------------------------


#ntInvertir = int(input("monto a invertir:"))
#
#teresAnual = float(input("ingrese el interes anual(%):")) / 100
#
#osDeInversion =  int(input("años de inversion:"))
#
#maDelCapitalObtenido = cantInvertir * interesAnual * añosDeInversion
#
#nancia = cantInvertir + sumaDelCapitalObtenido
#
#int(f"el monto a invertir es de:{cantInvertir} el interes es de:{interesAnual} el tiempo es de:{añosDeInversion}, dando como total ganado de:{round(ganancia)} ")

#-------------------------------------------------------

#oPayaso = 112
#
#eca = 75 
#
#ido = int(input("payasos vendidos:"))
#
#ido2 = int(input("muñecas vendidas:"))
#
#ultado = pedido * pesoPayaso + pedido2 * muñeca
#
#nt(f"el total del peso de la caja es de:{resultado}g")

#-----------------------------------------------------------

#contraseña = "groso"
#
#ing = input("ingrese la contraseña:")
#
#if contraseña != ing:
#    print("la contraseña ingresada es incorrecta")
#else:
#    print("la contraseña ingresada es correcta")

#-----------------------------------------------------------


#def dividir():
#    resul = (lambda a,b: "error" if b == 0 else a/b)(
#        float(input("ingrese un numero:")),
#        float(input("ingrese el divisor:"))
#    )
#    print(resul)
#dividir()    

#------------------------------------------------------------

#parOimpar = int(input("ingrese un numero:"))
#
#if parOimpar % 2 == 0:
#    print("par")
#
#else:
#    print("impar")

#---------------------------------------------------------

#edad = int(input("ingrese su edad:"))
#
#ingresos = int(input("ingrese sus ingresos:"))
#
#if edad > 18 and ingresos > 1000:
#    print("debe tributar")
#else:
#    print("no debe tributar")
#
#----------------------------------------------------------

pregunta = input("pizza vegetariana o no:")

if pregunta == "vegetariana" or pregunta == "si":
    res = input("""ingredientes vegetarianos:
          Pimiento
          Tofu
          (solo puede agregar un ingrediente)
            que desea:""")

    if res == "pimiento":
        print(f"su pizza es vegetariana y lleva mozzarella, tomate y {res}")
    elif res == "tofu":
        print(f"su pizza es vegetariana y lleva mozzarella, tomate y {res}")
    else:
      print("solo puede elejir un ingrediente")
