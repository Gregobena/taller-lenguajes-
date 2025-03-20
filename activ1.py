## activ 7
#7. Escribe un programa que tome una lista de números enteros como 
# entrada del usuario. Luego, convierte cada número en la lista a 
# string y únelos en una sola cadena, separados por guiones ('-'). 
# Sin embargo, excluye cualquier número que 
# sea múltiplo de 3 de la cadena final.

lista = list()
num = int(input("ingrese un numero para la lista"))
while num != 0: 
    lista.append(num)
    num = int(input("ingrese un numero para la lista"))
x = ''
for i in lista: 
    if i % 3 != 0: 
        x += str(i) + '-'
print(x)



## activ 6
#6. Modifique el ejercicio 4 para que dada la lista de 
# número genere dos nuevas listas, una con los número pares y 
# otras con los que son impares. Imprima las listas al terminar de 
# procesarlas.

pares = list() 
impares = list() 
lista = [1,2,3,4,5]
for i in lista: 
    if i % 2 == 0: 
        pares.append(i)

for i in lista: 
    if i % 2 != 0:
        impares.append(i) 
        continue

for j in pares: 
    print(j)
for k in impares:
    print(k)


## activ 5 
#5.Implementa un programa que solicite al usuario que ingrese 
# una lista de números. Luego, imprime la lista pero detén la 
# impresión si encuentras un número negativo. Nota: utilice 
# la sentencia `break` cuando haga falta.

lista = list()
num = int(input("ingrese un numero para la lista"))
while num != 0: 
    lista.append(num)
    num = int(input("ingrese un numero para la lista"))

for i in lista:
    if i < 0: 
        break
    print(i)

## activ 4 
#4. Cree un programa que dada una lista de números imprima sólo
#los que son pares.Nota: utilice la sentencia `continue` donde haga falta.

lista = [1,2,3,4,5]
for i in lista: 
    if i % 2 == 0: 
        print(i)

for i in lista: 
    if i % 2 != 0: 
        continue
    print(i)

## activ 3 
# 3. Crea un programa que calcule la suma de los primeros 
# 100 números naturales utilizando un bucle for.
x = 0 
for i in range(101): 
    x = i + x 
print(x)

## activ 2  

celcius = int(input("ingrese los grados celcius"))
Fahrenheit = (celcius * (9/5)) + 32 
print("los grados Fahrenheit son", Fahrenheit)

## activ 1 
edad = int(input("cuantos años tenes"))
print("te faltan", 100 - edad, " años para tener 100")

