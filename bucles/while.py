#el bucle termina cuando la condicion se cumple

contador = 0 

print("solo tienes 3 intentos")

while contador < 3:
     
     contraseña = input("ingrese la contraseña:")

     if contraseña == "martin":
          print("contraseña correcta")
          break
     else:
          print("contraseña incorrecta")
          contador += 1
          intentos = 3 - contador
          print(f"te quedan {intentos} intentos")
          