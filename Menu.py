import os
from Clases import Tienda, Factura

def mostrar_mensaje(mensaje):
    limpiar_pantalla()
    print(mensaje)
    pausar_pantalla()
    limpiar_pantalla()
    
def mostrar_productos(tienda):
    limpiar_pantalla()
    print('tienda uno')
    print("")
    tienda.mostrar_productos()
    print("")
    pausar_pantalla()
    limpiar_pantalla()

    
def manejoVentas(tienda):
    factura = Factura()
    while True:
        print ('Manejo Ventas')
        print('------------------------------')
        print("1. Agregar producto a la venta")
        print("2. Ver factura actual")
        print("3. Finalizar venta")
        print("4. cancelar venta actual")
        print("5. mostrar todas las facturas")
        print('6. Regresar menu principal ')
        print('------------------------------ ')
        
        opcion = int(input('Opcion --> '))
        
        match opcion:
            case 1:
                limpiar_pantalla()
                print("productos disponibles")
                print("")
                tienda.mostrar_productos()
                print("")
                
                try:
                    codigo = int(input("Ingresa el código del producto: "))
                    cantidad_vendida = int(input("ingresa la cantidad que quieres comprar:"))
                    if cantidad_vendida <= 0:
                        mostrar_mensaje("Error: Debes ingresar un numero mayor a 0")
                        continue                  
                            
                except ValueError:
                    mostrar_mensaje("Error: Debes ingresar un número entero válido")
                    continue
                    
                producto = tienda.comprobar_existencia_producto_por_codigo(codigo)
                
                if not producto:
                    mostrar_mensaje("Producto no encontrado")
                    return None
                
                cantidad_disponible = producto.cantidad_bodega
                
                if cantidad_vendida <= cantidad_disponible:
                    limpiar_pantalla()
                    factura.agregar_producto(producto,cantidad_vendida)
                    pausar_pantalla()
                    limpiar_pantalla()
                elif cantidad_disponible == 0:
                    mostrar_mensaje("ya no quedan mas cantidad de este producto para vender")             
                else:
                    mostrar_mensaje("la cantidad es mayor a la que se tiene, por ende se le vendera todos los productos")   
                    factura.agregar_producto(producto,cantidad_disponible)

            case 2:
                limpiar_pantalla()
                factura.mostrar_factura()
                pausar_pantalla()
                limpiar_pantalla()

            case 3:
                limpiar_pantalla()
                tienda.vender_productos(factura) 
                factura = Factura()
                pausar_pantalla()
                limpiar_pantalla()
                
            case 4:   
                limpiar_pantalla()
                factura.cancelar_venta_actual(tienda)
                pausar_pantalla()
                limpiar_pantalla()
                            
            case 5:
                limpiar_pantalla()
                tienda.mostrar_facturas()
                pausar_pantalla()
                limpiar_pantalla()
            
            case 6:
                break
            
            case other:
                mostrar_mensaje('error opcion invalida ')

def pausar_pantalla():
    os.system("pause")

def limpiar_pantalla():
    os.system("cls")

def crearTienda():
    return Tienda()

def menu_principal():
     tienda_creada=False
     
     while True:
        print ('Menu Tienda')
        print('------------------------------')
        print('1. Crear tienda con productos ')
        print('2. Mostrar tienda')
        print('3. Manejo de ventas ')
        print('4. Manejo de pedidos ')
        print('5. Manejo de Estadísticas ')        
        print('6. Salir ')
        print('------------------------------ ')
        
        opcion= int(input('Opcion --> '))
        
        match opcion:
            case 1:
                if not tienda_creada:
                    limpiar_pantalla()
                    tienda = crearTienda()
                    tienda_creada = True
                    print("Tienda Creada")
                    pausar_pantalla()
                    limpiar_pantalla()
                else:
                    mostrar_mensaje('Ya hay productos en la tienda')

                    
            case 2:
                if tienda_creada:
                    mostrar_productos(tienda)
                else:
                    mostrar_mensaje('no se ha creado la tienda. ejecutar la opcion 1')
            case 3:
                if tienda_creada:
                    limpiar_pantalla()
                    manejoVentas(tienda)
                    limpiar_pantalla()
                else:
                    mostrar_mensaje('no se ha creado la tienda. ejecutar la opcion 1')
                
            case 4:
                if tienda_creada:
                    #manejoPedidos(tienda)
                    pass
                else:
                    mostrar_mensaje('no se ha creado la tienda. ejecutar la opcion 1')
            case 5:
                if tienda_creada:
                   # manejoEstadisticas(tienda)
                    pass
                else:
                    mostrar_mensaje('no se ha creado la tienda. ejecutar la opcion 1')
            
            case 6:
                break
            
            case other:
                mostrar_mensaje('error opcion invalida')





menu_principal()