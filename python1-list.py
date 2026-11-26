
# listas


frutas = ["manzanas","peras","uva"]
numeros = [10,20,30,40]

print(numeros)

#accesder a un elem de la lista

print(frutas[0])

#agregar elementos

frutas.append("banana")

print(frutas[3])

# inseetar elemento y despliega el resto de su posicion
frutas.insert(1, "mango")

print(frutas)

frutas[0]= "piña"
print(frutas)

# elimiar un valor
frutas.remove ("uva")
frutas.pop(2)
del frutas[0]


print (frutas)
