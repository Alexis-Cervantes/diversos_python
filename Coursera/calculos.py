from random import randint
 
res = "S"
while res == "S" or res == "s":
       
   numero1 = randint(1,6)
   numero2 = randint(1,6)
   print("el primer numero es:",numero1,"el segundo numero es",numero2)
   print("la suma de los dos numeros es:",numero1 + numero2)
   res = input("Desea lanzar los dados?: S/N ")