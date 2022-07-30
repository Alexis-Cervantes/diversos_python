import random
'''Programa que simula juego de dados informando al usuario tirar los dados. El programa elegirá dos números aleatorios entre el 1 y el 6. Imprimiendo en pantalla los numeros que salieron, imprimira la suma entre ambos y preguntarle al usuario si quiere tirar los dados otra vez.'''

print('='*10,'Dados de la Suerte','='*10)
numeros = []
resp1 = str(input('¿Desea jugar?. [S/N]: ')).strip().upper()
while resp1 == 'S':
    print('Entonces Tire los los dados por favor...')
    numeros = random.choices([1, 2, 3, 4, 5, 6], k=2)
    print(f'Los numeros que salieron fueron: {numeros}')
    suma_numeros = numeros[0] + numeros[1]
    print(f'La suma de los 2 valores es: {suma_numeros}')
    print('='*40)
    resp2 = str(input('¿Desea continuar jugando?. [S/N]: ')).strip().upper()
    if resp2 == 'N':
        print('El juego termino...')
        break
else:
    print('El juego acabo...Hasta la próxima')
print('='*40)