#var1 nos pide un input del usuario, entregandole a él la
#información de que debe introducir el 'Piso del ascensor en Europa'
var1 = input ('Piso del ascensor en Europa?')
#nombramos la variable que nos entregará el valor convertido a pisos EEUU,
#convertimos el valor de la variable con input a un integer para poder sumarle
converted = int(var1) + 1
#escribimos los resultados, separando el texto del valor con una coma (,)
print ("Piso del ascensor en EEUU", converted)
