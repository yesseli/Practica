print ("1,-suma")
print ("2,-resta")
print ("3,-multiplicacion")
print ("4,-divicion")
opcion = int (input ("elija una opcion: "))
if  opcion == 1:
  numero1 = int (input ("introduce el primer numero  ")) 
  numero2 = int (input ("introduce el segundo numero "))
  numero3 = numero1+numero2
  print ("el resultado es: ", numero3 )
  opcion = input ("elija una opcion: ")
if opcion == 2:
  numero1 = int (input ("introduce el primer numero  ")) 
  numero2 = int (input ("introduce el segundo numero "))
  numero3 = numero1-numero2
  print ("el resultado es: ", numero3) 
  opcion = input ("elija una opcion: ")
if opcion == 3:
  numero1 = int (input ("introduce el primer numero  ")) 
  numero2 = int (input ("introduce el segundo numero "))
  numero3 = numero1*numero2
  print ("el resultado es: ", numero3 )
  opcion = input ("elija una opcion: ")
if opcion == 4:
  numero1 = int (input ("introduce el primer numero  "))
  numero2 = int (input ("introduce el segundo numero "))
  numero3 = numero1/numero2
  print ("el resultado es: ", numero3)