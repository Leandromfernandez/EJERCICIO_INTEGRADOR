""" Ejercicio Integrador 01
La división de higiene está trabajando en un control de stock para productos
sanitarios. Debemos realizar la carga de 5 (cinco) productos de prevención de
contagio, de cada una debe obtener los siguientes datos:

1. El tipo (validar "barbijo", "jabón" o "alcohol")
2. El precio: (validar entre 100 y 300)
3. La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las
1000 unidades)
4. La marca y el Fabricante."""
#######################################################################################


"""Se debe informar lo siguiente:
A. Del más caro de los barbijos, la cantidad de unidades y el fabricante.
B. Del ítem con más unidades, el fabricante.
C. Cuántas unidades de jabones hay en total. """

lista_productos = []
lista_precios = []
lista_unidades = []
lista_marca = []
lista_fabricante = []

barbijo_max = None

unidades_max = None

acumulador_jabon = 0

for productos in range(5):
        
    tipo_de_producto = input('Ingrese el tipo de producto [ BARBIJO - JABON - ALCOHOL]: ')
    tipo_de_producto = tipo_de_producto.upper()
    while tipo_de_producto != "BARBIJO" and tipo_de_producto != "JABON" and tipo_de_producto != "ALCOHOL":
        tipo_de_producto = input('ERROR. Ingrese el tipo de producto [ BARBIJO - JABON - ALCOHOL]: ')
        tipo_de_producto = tipo_de_producto.upper()
        
    precio = int(input('Ingrese el precio del producto entre [100 - 300]: '))
    while precio < 100 or precio > 300:
        precio = int(input('ERROR. Ingrese un precio valido. '))
    
    unidades = int(input('Ingrese la cantidad de unidades: '))
    while unidades < 0 or unidades > 1000:
        unidades = int(input('ERROR. Ingrese la cantidad de unidades válida : '))

    marca = input('Ingrese la marca del producto: ')
    marca = marca.upper()
    while marca == "":
        marca = input('ERROR. Ingrese la marca del producto: ')
        marca = marca.upper()
    
    fabricante = input('Ingrese el fabricante del producto: ')
    fabricante = fabricante.upper()
    while fabricante == "":
        fabricante = input('ERROR. Ingrese el fabricante del producto: ')
        fabricante = fabricante.upper()

    lista_productos.append(tipo_de_producto)
    lista_precios.append(precio)
    lista_unidades.append(unidades)
    lista_marca.append(marca)
    lista_fabricante.append(fabricante)       

#A. Del más caro de los barbijos, la cantidad de unidades y el fabricante.   
for i in range(len(lista_productos)):
    if lista_productos[i] == "BARBIJO":
        precio = lista_precios[i]
        if barbijo_max == None or precio > barbijo_max:
            barbijo_max = lista_precios[i]
            unidades_barbijos_max = lista_unidades[i]
            fabricante_max = lista_fabricante[i]
    #C. Cuántas unidades de jabones hay en total.
    elif lista_productos[i] == "JABON":
        unidades_jabon = lista_unidades[i]
        acumulador_jabon = acumulador_jabon + unidades_jabon 


#B. Del ítem con más unidades, el fabricante.
for i in range(len(lista_unidades)):
    if unidades_max == None or unidades > unidades_max:
        unidades_max = lista_unidades[i]
        producto_con_unidades_max = lista_productos[i]
        fabricante_con_unidades_max = lista_fabricante[i]    


#A-
if barbijo_max != None:
    print(f'el barbijo mas caro sale: {barbijo_max}, hay {unidades_barbijos_max} unidades del fabricante: {fabricante_max} ')
else:
    print('NO SE CARGARON BARBIJOS')

#B-
print(f'El item con mas unidades es: {producto_con_unidades_max}, tiene {unidades_max} y el fabricante es: {fabricante_con_unidades_max}')

#C-
if acumulador_jabon > 0:
    print(f'hay: {acumulador_jabon} unidades de jabon')
else:
    print("NO HAY JABONES")







