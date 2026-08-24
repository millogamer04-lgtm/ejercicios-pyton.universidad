# Declaramos dos edades diferentes. 
edad_1 = int(input("Ingrese la primera edad: "))
edad_2 = int(input("Ingrese la segunda edad: "))
# Comprobamos si las edades son iguales. 
son_iguales = edad_1 == edad_2 
# Comprobamos si la primera edad es mayor que la segunda. 
primera_es_mayor = edad_1 > edad_2 
# Comprobamos si ambas personas son mayores de 18 años. 
ambas_mayores_de_18 = edad_1 > 18 and edad_2 > 18 
# Mostramos los tres resultados booleanos. 
print("¿Las edades son iguales?", son_iguales) 
print("¿La primera edad es mayor?", primera_es_mayor) 
print("¿Ambas personas son mayores de 18?", ambas_mayores_de_18)