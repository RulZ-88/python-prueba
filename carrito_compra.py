'''
    Programa para carrito de compras
    - Tienen que haber productos
    - Tienen que haber usuarios, únicos
    - Tiene que haber un carrito de compra que asocie
      los productos y sus cantidades, que quiere comprar un usuario
    - Tiene que existir un código de descuento
        - Tiene solo letras mayúsculas, a lo menos 6 caracteres y por lo menos 2 números  
        - ej. 2BNM8YT
'''
codigo_descuento = {
    "2BNM8YT":0.1,
    "UGLYKID47":0.15,
}
productos = {
    "italiano":2990,
    "dinamico":3450,
    "chacarero":3740,
    "papas_fritas":1890
}

carritos = {
        "racsodia":{ 
                    "productos":{
                        "italiano":3,
                        "papas_fritas":2
                    },
                "codigo_descuento":""
        },
        "jorgeb":{ 
                "productos":{
                    "italiano":3,
                    "papas_fritas":2
                },
                "codigo_descuento":""
        },
    }

# Función que agregue productos al carrito
def agregar_producto(usuario,producto,cantidad):
    if producto in productos and usuario in carritos:
            if producto in carritos[usuario]["productos"]:
                carritos[usuario]["productos"][producto] += cantidad
            else:
                carritos[usuario]["productos"][producto] = cantidad

print(carritos)
agregar_producto("jorgeb","dinamico",2)
print(carritos)
agregar_producto("jorgeb","dinamico",1)
print(carritos)

def eliminar_producto(usuario,producto,cantidad):
    if producto in productos and usuario in carritos:
        if producto in carritos[usuario]["productos"]:
            carritos[usuario]["productos"][producto] -= cantidad
        else:
            print("El producto no está en su carrito")
    else:
        print("Ingrese datos válidos")

def calcular_boleta(usuario):
    if usuario in carritos:
        if len(carritos[usuario]["productos"]) > 0:
            subtotal = 0
            boleta = "****** BOLETA ******\n***  Detalle  ****:\n"
            for producto in carritos[usuario]["productos"]:
                venta = carritos[usuario]["productos"][producto] * productos[producto]
                subtotal += venta
                boleta += "**" + producto + ":" + str(venta) + "\n"
            iva = subtotal * 0.19
            total = subtotal + iva

            boleta += "**" + "SubTotal: " + str(subtotal) + "\n" + "**" + "IVA: " + str(iva) +"\n"
            boleta += "**" + "TOTAL: " + str(total)
            print(boleta)
        else:
            print("El carrito no tiene productos")
    else:
        print("El usuario no tiene carrito creado")

calcular_boleta("jorgeb")