# Mi trivia de conocimiento de historia del Perú
import random
import time
RED     = '\033[31m'
BLUE = '\033[34m'
RESET = '\033[39m'

iniciar_trivia = True
intentos = 0

print ("Bienvenido a la trivia sobre Historia del Perú.\n")
print ("Esta trivia consiste en responder 3 preguntas y ver cuanto puntaje puedes alcanzar.\n")

nombre = input(RED+"\nPrimero ingresa tu nombre: "+RESET)
time.sleep(1)
print("\nNombre registrado ",nombre)

time.sleep(3)
print("\nResponde las siguientes preguntas escribiendo la letra de la alternativa y presiona 'Enter' para enviar tu respuesta.\n")
time.sleep(4)
print("Se te sumarán 10 puntos por respuesta correcta y se restarán 5 puntos por las incorrectas.\n")

time.sleep(3)
while iniciar_trivia == True:
  intentos += 1
  puntaje = random.randint(5,15) 
  print(RED+"\nIntento número:"+RESET,intentos)
  input("Presiona Enter para continuar")

  print(RED+"\nComenzarás con:",puntaje, "puntos.\n"+RESET)
  
  time.sleep(2)
  # Pregunta 1
  print (BLUE+"Pregunta 1 ¿Cuándo se dio la declaración de la independencia del Perú?\n"+RESET)
  print ("a) 29 de junio de 1921")
  print ("b) 28 de julio de 1921")
  print ("c) 28 de julio de 1821")
  
  respuesta_1 = input(BLUE+"\nTu respuesta: "+RESET).lower()
  
  while respuesta_1 not in ("a", "b", "c"):
    respuesta_1 = input("Debes responder a, b, o c. Ingresa nuevamente tu respuesta: ").lower()
  if respuesta_1 == "a":
    print("\nIncorrecto", nombre, "\nEs el 28 de julio de 1821\n")
    puntaje = puntaje - 5
  elif respuesta_1 == "b":
    print("\nIncorrecto", nombre, "\nEs el 28 de julio de 1821\n")
    puntaje = puntaje - 5
  else:
    puntaje += 10
    print("\nCorrecto", nombre,"!\n")
  
  print (RED+nombre, "llevas",puntaje,"puntos"+RESET)
  
  time.sleep(2)
  #Pregunta 2
  print (BLUE+"\nPregunta 2 ¿Cuál fue el último emperador inca?\n"+RESET)
  print ("a) Moctezuma II ")
  print ("b) Atahualpa")
  print ("c) Gerónimo")
  
  respuesta_2 = input(BLUE+"\nTu respuesta: "+RESET).lower()
  
  while respuesta_2 not in ("a", "b", "c"):
    respuesta_2 = input("Debes responder a, b, o c. Ingresa nuevamente tu respuesta: ").lower()
  
  if respuesta_2 == "a":
    print("\nIncorrecto", nombre,"\nAtahualpa fue el último soberano inca, aunque no alcanzó a coronarse oficialmente como tal.\n")
    puntaje -= 2
  elif respuesta_2 == "c":
    print("\nIncorrecto", nombre,"\nAtahualpa fue el último soberano inca, aunque no alcanzó a coronarse oficialmente como tal.\n")
    puntaje = puntaje - 5
  else:
    puntaje += 10
    print("\nCorrecto", nombre,"!\n")
  
  print (RED+nombre, "llevas",puntaje,"puntos"+RESET)
  
  time.sleep(3)
  # Pregunta 3
  print (BLUE+"\nPregunta 3 Uno de los grandes ideales políticos de San Martín fue.\n"+RESET)
  print ("a) Liberar Chile y Perú")
  print ("b) Establecer la Monarquía Constitucional.")
  print ("c) El pago de una indemnización de Guerra")
  
  respuesta_3 = input(BLUE+"\nTu respuesta: "+RESET).lower()
  
  while respuesta_3 not in ("a", "b", "c"):
    respuesta_3 = input("Debes responder a, b, o c. Ingresa nuevamente tu respuesta: ").lower()
  
  if respuesta_3 == "a":
    print("\nIncorrecto", nombre, ",\nla respuesta es la opción b.\n")
    puntaje = puntaje - 5
  elif respuesta_3 == "c":
    print("\nIncorrecto", nombre, ",\nla respuesta es la opción b.\n")
    puntaje = puntaje - 5
  else:
    puntaje += 10
    print("\nCorrecto", nombre, "!\n")
    
    print (RED+nombre, "llevas",puntaje,"puntos"+RESET)

  time.sleep(4)
  #Resultados
  print (RED+"\nVeamos tu resultado"+RESET)
  print(BLUE+"\nTu puntaje es de",puntaje, "puntos"+RESET)
  print("\n¿Deseas intentar la trivia nuevamente?")
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()

  if repetir_trivia != "si":  # != distinto
   print("\nOkey",nombre,"espero te haya gustado. Adios")
   iniciar_trivia = False
   