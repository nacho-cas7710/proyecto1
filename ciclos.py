# if y else
#numero = int(input("Ingrese un número: "))

#if numero > 0:
 #   print("El número es positivo.")
#else:
 #   print("El número es negativo.")
##2
#numero = int(input("Ingrese un número: "))

#if numero % 2 == 0:
 #   print("El número es par.")
#else:
  #  print("El número es impar.")
##3
#puntuacion = float(input("Ingrese la puntuación del examen: "))

#if puntuacion >= 5.0:
 #   print("¡Felicidades! Has aprobado el examen.")
#else:
 #   print("Lo siento, has reprobado el examen.")

#distancia_pared=int(input("ingrese la distacia a la que su robot quire girar:"))
#if distancia_pared<=12:
 #   print("su robot debe girar")
#else:
 #   print("su robot debe detenerse!!!")

#detecto_rojo=int(input("ingrese el valor del color rojo"))
#detecto_azul=int(input("ingrese el valor del color azul"))
#if detecto_rojo==90:
  #  print("gire a la derecha")

#if detecto_azul==20:
 #   print("gire a la izquierda")


##4


numero=int(input("igresame numero: "))
if numero== 1:
    print("lunes")
elif numero==2:
    print("martes")
elif numero==3:
    print("miercoles")









#ciclo while

limite=10
contador=0
while contador<limite:
    contador=contador+1
    print(contador)


# Usando True y False para controlar el ciclo
#contador = 0
#while True:
  
     # Este ciclo se ejecutará indefinidamente a menos que se rompa explícitamente
 #   print("El contador es:", contador)
  #  contador += 1
   # print(contador)
    #if contador > 100:
     #   break  # Rompe el ciclo cuando el contador alcanza o supera 5




#limite = 10
#suma = 0
#contador = 1
#while contador <= limite:
   # suma =+ contador
   # contador += 1
    
#print("La suma de los números enteros hasta", limite, "es:", suma)



#FOR
numero_limite=int(input("ingrese un numero limite"))
for posicion in range(numero_limite):
   print("hola",[posicion])

for i in range(0,10):
    i=i+1
    print(i)


for i in range(1,10,2):
   i=i+1
   print(i)

#resoluciones
# Inicializamos la variable para almacenar la suma
suma = 0

# Inicializamos el contador en 100
#numero = 100

# Creamos el bucle while
#while numero <= 200:
    # Sumamos el número actual a la suma total
 
 #   suma += numero
    # Mostramos el número actual
  #  print(numero)
    # Incrementamos el número para pasar al siguiente
   # numero += 1

# Mostramos la suma total fuera del bucle
#print("La suma total es:", suma)


#while True:
    # Aquí dentro puedes colocar cualquier instrucción que desees repetir infinitamente
    # Por ejemplo, puedes imprimir un mensaje repetidamente
  #print("Este es un ciclo infinito. Presiona Ctrl + C para detenerlo.")
  #  # O puedes pedir entrada al usuario continuamente
  #entrada = input("Ingresa algo (presiona Ctrl + C para detener): ")
  #print("Ingresaste:", entrada)

#while True:
 #   respuesta = input("¿Quieres finalizar la ejecución del programa? (si/no): ")
  #  if respuesta== "si":
   #   print("Programa finalizado.")
    #  break


# Pedimos al usuario que ingrese un número
#numero = int(input("Ingresa un número: "))

# Mostramos la tabla de multiplicar del número ingresado
#print("Tabla de multiplicar del :", numero)
#for i in range(1, 11):
 #   resultado = numero * i
  #  print(numero, "x", [i],"=",resultado)

# Inicializamos la variable para almacenar la suma
#suma = 0

# Usamos un bucle for para iterar sobre los números del 100 al 200
#for numero in range(100, 201):
    # Sumamos el número actual a la suma total
 #   suma = suma + numero
    # Mostramos el número actual
  #  print(numero)

# Mostramos la suma total fuera del bucle
#print("La suma total es:", suma)
