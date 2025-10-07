import os
from Clases import Tienda, Factura, Producto

def pausar_pantalla():
    os.system("pause")

def limpiar_pantalla():
    os.system("cls")
   
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

# menus 
def menu_realizar_venta(tienda):
    factura = Factura()
    while True:
        print ('realizar_venta')
        print('------------------------------')
        print("1. Agregar producto a la venta")
        print("2. Ver factura actual")
        print("3. Ver factura actual detallada")        
        print("4. Finalizar venta")
        print("5. cancelar venta actual")
        print("6. regresar")

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
                factura.mostrar_factura_detallada()
                pausar_pantalla()
                limpiar_pantalla()

            case 4:
                limpiar_pantalla()
                tienda.vender_productos(factura) 
                factura = Factura()
                pausar_pantalla()
                limpiar_pantalla()
                
            case 5:
                limpiar_pantalla()
                factura.cancelar_venta_actual(tienda)
                pausar_pantalla()
                limpiar_pantalla()
            
            case 6:
                break
            
            case other:
                mostrar_mensaje('error opcion invalida ')

def menu_manejoVentas(tienda):
    while True:
        print('Manejo Ventas')
        print('------------------------------')
        print('1. Realizar venta ')
        print('2. Mostrar Facturas Resumen')
        print('3. Mostrar Facturas con detalle ')
        print('4. Mostrar venta por producto ')
        print('5. Regresar menu principal ')
        print('------------------------------ ')
        
        opcion = int(input('Opcion --> '))
        match opcion:
            case 1:
                limpiar_pantalla()
                menu_realizar_venta(tienda)
                limpiar_pantalla()                
            case 2:
                limpiar_pantalla()
                tienda.mostrar_facturas()
                pausar_pantalla()
                limpiar_pantalla()
            case 3:
                limpiar_pantalla()
                tienda.mostrar_facturas_detalladas()
                pausar_pantalla()
                limpiar_pantalla()
            case 4:
                limpiar_pantalla()
                tienda.consultar_venta_por_producto()
                pausar_pantalla()
                limpiar_pantalla()
            case 5:
                break
            
            case _:
                print('Error: opcion invalida ')

def menu_pedidos(tienda):
    while True:
        print('Manejo Pedidos')
        print('------------------------------')
        print('1. Pedido por producto ')
        print('2. Realizar todos los pedidos ')
        print('3. Regresar menú principal ')
        print('------------------------------ ')
        
        opcion = int(input('Opcion --> '))
        match opcion:
            case 1:
                limpiar_pantalla()
                tienda.realizar_pedido_por_productos()
                pausar_pantalla()
                limpiar_pantalla()
            case 2:
                limpiar_pantalla()
                tienda.realizar_todos_los_pedidos()
                pausar_pantalla()
                limpiar_pantalla()
            case 3:
                break
            case _:
                print('Error: opcion invalida ')

def menu_estadisticas(tienda):
    while True:
        print('Menu Estadísticas')
        print('------------------------------')
        print('1. Total ventas ')
        print('2. Promedio de ventas')
        print('3. Venta por Producto ')
        print('4. Promedio venta producto')
        print('5. Producto más vendido ')
        print('6. Regresar ')
        print('------------------------------ ')
        
        opcion = int(input('Opcion --> '))
        
        match opcion:
            case 1:
                #tienda.totalVentaProductos()
                os.system('pause')
            
            case 2:
                #tienda.promedioVentas()
                os.system('pause')
                
            case 3:
                #consultarVentaProducto(tienda)
                os.system('pause')
            case 4:
                #tienda.promedioVentasProducto()
                os.system('pause')
            
            case 5:
                #tienda.productoMasVendido()
                os.system('pause')
            case 6:
                break
            case _:
                print('Error: opcion invalida ')
                                
def crearTienda():
    return Tienda()

def menu_principal():
    limpiar_pantalla()
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
                    menu_manejoVentas(tienda)
                    limpiar_pantalla()
                else:
                    mostrar_mensaje('no se ha creado la tienda. ejecutar la opcion 1')
                
            case 4:
                if tienda_creada:
                    limpiar_pantalla()
                    menu_pedidos(tienda)
                    limpiar_pantalla()
                    pass
                else:
                    mostrar_mensaje('no se ha creado la tienda. ejecutar la opcion 1')
            case 5:
                if tienda_creada:
                    limpiar_pantalla()
                    menu_estadisticas(tienda)
                    limpiar_pantalla()
                else:
                    mostrar_mensaje('no se ha creado la tienda. ejecutar la opcion 1')
            
            case 6:
                limpiar_pantalla()
                if  tienda_creada:
                    tienda.guardar_archivo()
                break
            
            case other:
                mostrar_mensaje('error opcion invalida')




menu_principal()