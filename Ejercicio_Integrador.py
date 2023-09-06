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


for productos in range(2):
        
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
        
        

    productos += 1
    
for i in range(len(lista_productos)):
    precio = lista_precios[i]
    if barbijo_max == None or precio > barbijo_max:
        barbijo_max = precio
        unidades_max = lista_unidades[i]
        fabricante_max = lista_fabricante[i]
  

print(f'el barbijo mas caro sale: {barbijo_max}, del fabricante: {fabricante_max}, y hay {unidades_max} unidades. ')






#print (f'PRODUCTOS: {lista_productos}\nPRECIOS: {lista_precios}\nUNIDADES: {lista_unidades}\nMARCA: {lista_marca}\nFABRICANTE: {lista_fabricante} ')    
