#lista_ejemplo = ["A", "B","C","D","E","f","3455"]
#print(lista_ejemplo)
#print(lista_ejemplo[2])
#print(lista_ejemplo[-1])

#porcion de lista
#print(lista_ejemplo[2:4])
#print(lista_ejemplo[3:])
#print(lista_ejemplo[:4])

#funciones extras 
#lista_ejemplo.append("F")
#print(lista_ejemplo)

#lista_ejemplo.insert(2,"Y")
#print(lista_ejemplo)

#lista_ejemplo.extend(["casa","hotel"])
#print(lista_ejemplo)

#sacar
#lista_ejemplo.remove([2])
#print(lista_ejemplo)

#variable=lista_ejemplo.pop()
#print(lista_ejemplo)
#print(variable)


##tuplas
#tupla_ejemplo = ("A", "B","C","D","E")
#print(tupla_ejemplo[2])
#print(tupla_ejemplo[-1])

#porcion de lista
#print(tupla_ejemplo[2:4])
#print(tupla_ejemplo[3:])
#print(tupla_ejemplo[:4])

#ejemplos
#lista_ej = [2,3,4,5,6]
#tupla_ej =tuple(lista_ej)
#print(tupla_ej)

#tulpa_ej = (2,3,4,5,6)
#lista_ej =list(tulpa_ej)
#print(lista_ej)

#dicc_ejemplo = {"usuario": "castillo", "contraseña": 392023, "telefono": 372837288293}
#print(dicc_ejemplo["usuario"])

# Generar y mostrar los números del 1 al 35

#--------------------------------------------------------------------
#RESOLUCIONES 
#Inicializar una lista para almacenar los números aleatorios
#lista = []

# Inicializar una semilla arbitraria
#semilla = 42

# Generar 10 números aleatorios
#for i in range(10):
    # Calcular un nuevo número pseudoaleatorio utilizando una técnica simple
 #   semilla = (semilla * 17 + 97) % 100  # Se utilizan números arbitrarios para la fórmula
  #  numero_aleatorio = semilla % 10 + 1  # Ajustar el número para estar dentro del rango 1-10
   # lista.append(numero_aleatorio)  # Agregar el número a la lista

# Mostrar cada elemento de la lista junto con su cuadrado y su cubo
#print("Elemento |  Cuadrado |  Cubo")
#for elemento in lista:
 #   cuadrado = elemento ** 2
  #  cubo = elemento **3
   # print(f"{elemento:<10} {cuadrado<10} {cubo}")
#---------------------------------------------------------------
#RESOLUCION 2

#-------------------------------------------------------------------------------------------------
# Inicializar una lista vacía
#lista = []
#[2,3,1,34,0]
# Solicitar al usuario que ingrese 10 números y agregarlos a la lista
#for i in range(10):
 #   numero = float(input(f"Ingrese el número {i + 1}: "))
  #  lista.append(numero)

# Inicializar una variable para almacenar el menor elemento y su índice
#menor_elemento = lista[0]
#indice_menor = 0

# Iterar sobre la lista para encontrar el menor elemento y su índice
#for i in range(1, len(lista)):
 #   if lista[i] < menor_elemento:
  #      menor_elemento = lista[i]
   #     indice_menor = i

# Mostrar el menor elemento y su índice
#print(f"El menor elemento es {menor_elemento} y se encuentra en la posición {indice_menor + 1} de la lista.")
#--------------------------------------------------------------------
#RESOLUCION 3 TUPLAS
#-----------------------------------------------------------------------
# Crear una tupla con números
#numeros = (3, 5, 7, 3, 8, 3, 2, 5, 9, 3)
#print(numeros)

# Pedir un número por teclado
#numero_buscado = int(input("Ingrese un número para buscar cuántas veces se repite en la tupla: "))

# Contador para almacenar el número de repeticiones
#repeticiones = 0

# Iterar sobre la tupla y contar las repeticiones del número
#for elemento in numeros:
 #   if elemento == numero_buscado:
  #      repeticiones += 1

# Mostrar el resultado
#print(f"El número {numero_buscado} se repite {repeticiones} veces en la tupla.")

#------------------------------------------
# Crear una tupla con los nombres de los meses
#meses = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")

# Pedir al usuario un número entre 1 y 12
#numero_mes = int(input("Ingrese un número entre 1 y 12 para ver el mes correspondiente: "))

# Validar si el número ingresado está dentro del rango válido
#if 1 <= numero_mes <= 12:
    # Mostrar el mes correspondiente
 #  mes_correspondiente = meses[numero_mes - 1 ]  # Restamos 1 porque los índices en Python comienzan en 0
  # print(f"El mes correspondiente al número {numero_mes} es: {mes_correspondiente}.")
#else:
 #   print("Número de mes inválido. Debe ser un número entre 1 y 12.")

 #-----------------------------------------------------------------------
 #diccionarios

 # Definir un diccionario de alumnos y sus notas
#alumnos = {
 #   "juan": [10, 9, 8],
  #  "maría": [7, 8, 9],
   # "pedro": [6, 7, 8]
#}

# Pedir al usuario el nombre del alumno
#nombre = input("Ingrese el nombre del alumno: ")

# Verificar si el alumno está en el diccionario y mostrar sus notas
#if nombre in alumnos:
 #   print(f"Notas de {nombre}: {alumnos[nombre]}")
#else:
 #   print(f"El alumno {nombre} no se encuentra en la lista.")



# Creamos un diccionario con los nombres de los meses como clave y el número de días como valor
# Creamos un diccionario con los nombres de los meses como clave y el número de días como valor
#meses = {
 #   "enero": 31,
  #  "febrero": 28,
   # "marzo": 31,
    #"abril": 30,
    #"mayo": 31,
    #"junio": 30,
    #"julio": 31,
    #"agosto": 31,
    #"septiembre": 30,
    #"octubre": 31,
    #"noviembre": 30,
    #"diciembre": 31
#}

# Pedimos al usuario que ingrese el nombre del mes (en minúsculas para simplificar)
#nombre_mes = input("Ingrese el nombre del mes: ").lower()

# Verificamos si el mes ingresado está en nuestro diccionario
#if nombre_mes in meses:
    # Si está, imprimimos el número de días
# print(f"{nombre_mes} tiene {meses[nombre_mes]} días.")
#else:
    # Si no está, mostramos un mensaje de error
   # print("Mes no válido.")

