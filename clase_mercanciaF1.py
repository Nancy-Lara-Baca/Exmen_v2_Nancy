print ("Examen Nancy Lara Baca 1225")

class mercanciaF1:
    def diccionario_productos1225(self):
        print("Diccionario Productos")
        Productos = {
            "ID: ": "1225",
            "Nombre: ": "Chamarra Ferrari",
            "Cantidad de productos: ": "540",
            "Precio: ": "$1020",
            "Tamaño/Talla: ":  "Talla Mediana",
            "Descripcion: ": "Color rojo",
            "Calidad: ": "Buena"
            }
        for produ, produ2 in Productos.items():
            print(produ, produ2)
            
    def diccionario_proveedores1225(self):
        print("Diccionario Proveedores")
        Proveedores = {
            "ID: ": "3435",
            "Nombre: ": "Ferrari",
            "Productos: ": "Gorras",
            "Cantidad de Productos: ": "290",
            "Direccion: ": "Calle Guerbera col. Jardin #1225",
            "Telefono: ": "656-332-1225",
            "NIE: ": "4435"
        }
        for prove, prove2 in Proveedores.items():
            print(prove, prove2)
            
    def diccionario_clientes1225(self):
        print("Diccionario Clientes")
        Clientes = {
            "ID: ": "1136",
            "Nombre: ": "Nancy",
            "Numero de Telefono: ": "656-122-5723",
            "Correo: ": "nancy@729.com",
            "Direccion: ": "Calle Tul col. Nueva #729",
            "Edad: ": "17",
            "Genero: ": "Femenino"
        }
        for cli, cli2 in Clientes.items():
            print(cli, cli2)
            
    def diccionario_Local1225(self):
        print("Diccionario Local")
        Local = {
            "ID: ": "1248",
            "Direccion: ": "Calle Rol col. Pan #131",
            "Gerente: ": "Nancy",
            "Empleados: ": "7",
            "Cantidad de productos: ": "790",
            "Capacidad: ": "900 Articulos de venta",
            "Telefono: ": "656-122-5723"
        }
        for lo, lo2 in Local.items():
            print(lo, lo2)
            
diccionario=mercanciaF1()
diccionario.diccionario_productos1225()
diccionario.diccionario_proveedores1225()
diccionario.diccionario_clientes1225()
diccionario.diccionario_Local1225()