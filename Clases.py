import os

def pausar_pantalla():
    os.system("pause")

def limpiar_pantalla():
    os.system("cls")


class Producto():
    def __init__(self,codigo,producto_nombre,tipo_producto,cantidad_bodega,cantidad_minima,valor_unitario):
        self.codigo = codigo
        self.nombre = producto_nombre
        self.tipo_producto = tipo_producto
        self.cantidad_bodega  = cantidad_bodega
        self.cantidad_minima = cantidad_minima
        self.valor_unitario = valor_unitario
    
    def __str__(self):
        return f"{self.codigo} {self.nombre} (${self.valor_unitario:,.2f}) - Stock: {self.cantidad_bodega}"
  
class Tienda():
    def __init__(self):
        self.num_factura = 0
        self.dinero_caja = 0
        self.facturas = []
        self.productos = self.cargar_archivo()   
       #self.productos = [Producto(1, "Lápiz", "papeleria", 50, 10, 1500),Producto(2, "Arroz 1kg", "supermercado", 30, 5, 2800),Producto(3,"Jabón Antibacterial", "drogueria", 40, 8, 3200),Producto(4, "Cuaderno ", "papeleria", 25, 5, 4500)]
    
    def agregar_producto(self, producto):
        self.productos.append(producto)
    
    def mostrar_productos(self): #cambiar esta parte luego
        print(f"{'Código':<10} {'Nombre':<25} {'Tipo':<15} {'Stock':<10} {'Mínimo':<10} {'Precio':<16}")

        for producto in self.productos:
            print(f" {producto.codigo:<9} {producto.nombre:<24} {producto.tipo_producto:<14} "
                f"{producto.cantidad_bodega:<9} {producto.cantidad_minima:<9} "
                f"${producto.valor_unitario:<14.2f}")
    
    def mostrar_facturas(self):
        if self.facturas == []:
            print("no hay ninguna venta")
            return None

        for factura in self.facturas:
            print("")
            print(f"numero de factura: {factura.num_factura}")
            factura.mostrar_factura()
            print("")
            print("_"*50)
            print("")

    def mostrar_facturas_detalladas(self):
        if self.facturas == []:
            print("no hay ninguna venta")
            return None

        for factura in self.facturas:
            print("")
            print(f"numero de factura: {factura.num_factura}")
            factura.mostrar_factura_detallada()
            print("")
            print("_"*50)
            print("")
            
    def comprobar_existencia_producto_por_codigo(self, codigo):
        for producto in self.productos:
            if producto.codigo == codigo:
                return producto
        return False
    
    def vender_productos(self,factura):
        if not factura.factura:
            print("la factura esta vacia :/")
            return None

        factura.num_factura = self.num_factura
        self.num_factura += 1
        self.facturas.append(factura)
        print(f"la venta se realizo correctamente- n°factura {factura.num_factura}")

    def pedir_codigo_producto(self):
        try:
            codigo = int(input("Digita el código del producto para consultar todas sus ventas: "))
            if codigo <= 0:
                print("El código debe ser un número positivo")
                return None 
            return codigo
        except ValueError:
            print("Error: El código debe ser un número entero")
            return None
    
    def consultar_venta_por_producto(self):        
        if self.facturas == []:
            print("no hay ninguna venta")
            return None

        codigo = self.pedir_codigo_producto()

        if self.comprobar_existencia_producto_por_codigo(codigo):
            print("")
            cantidad_producto_vendida = 0
            ganancia_producto = 0
            print(f"{'CÓDIGO':<10} {'PRODUCTO':<20} {'CANT':<8} {'P.UNIT':<10} {'IVA':<6} {'P.TOTAL':<10} {'TOTAL':<10}")
            for factura in self.facturas:
                for producto in factura.factura:
                    if producto.codigo == codigo:
                        print(f"{producto} factura n° {factura.num_factura}")
                        cantidad_producto_vendida += producto.cantidad_vendida
                        ganancia_producto += producto.total
            print("")
            if cantidad_producto_vendida > 0:
                print(f"cantidad del producto vendida = {cantidad_producto_vendida}")                
                print(f"ganancias del producto = {ganancia_producto}")
            else:
                limpiar_pantalla()
                print("no se ha encontrado ninguna venta de este producto")
        else:
            print("el producto no existe en el inventario")
    
    def realizar_pedido_por_productos(self):
        self.mostrar_productos()
        print("")
        try:
            codigo = int(input("digita el codigo del producto: ")) 
            producto = self.comprobar_existencia_producto_por_codigo(codigo)
            if not producto:
                limpiar_pantalla()
                print("producto no encontrado, seleccione un producto que exista")
                return None
        except :
            print("digita un numero correcto por favor")
            return None
        limpiar_pantalla()

        try:
            cantidad = int(input("cuantos productos vas a comprar: "))
            if cantidad <= 0:
                print("digita un numero mayor a 0")
                return None
        except :
            print("digita un numero correcto")
            return None
        limpiar_pantalla()
        producto = self.comprobar_existencia_producto_por_codigo(codigo)
        
        if producto:
            producto.cantidad_bodega += cantidad
            print("la cantidad del producto se añadio correctamente")
        else:
            print("producto no encontrado")
            return None
    
    def realizar_todos_los_pedidos(self):
        self.mostrar_productos()
        print("")
        try:
            cantidad = int(input("cuantos cantidad vas a comprar en general: "))
            if cantidad <= 0:
                print("digita una cantidad valida")
                return None        
        except:
            print("digita un numero correcto")
            return None
        
        productos_actualizados = 0
        for producto in self.productos:        
                producto.cantidad_bodega += cantidad
                productos_actualizados += 1
        print(f"se actualizaron {productos_actualizados} productos")

    def cargar_archivo(self):
        
        productos = []
        # Crear archivo si no existe
        if not os.path.exists("Productos.dat"):
            archivo = open("Productos.dat", "w")
        
        archivo = open("Productos.dat", "r")
        
        for linea in archivo.readlines():
            producto = self.convertir_texto_a_producto(linea)
            productos.append(producto)
        
        return productos
    
    def convertir_texto_a_producto(self, linea):
        linea = linea.split(",")
        codigo = int(linea[0])
        nombre = str(linea[1])
        tipo_producto = str(linea[2])
        cantidad_bodega = int(linea[3])
        cantidad_minima = int(linea[4])
        valor_unitario = int(linea[5])
                
        return Producto(codigo,nombre,tipo_producto,cantidad_bodega,cantidad_minima,valor_unitario)

    def guardar_archivo(self):
        archivo = open("Productos.dat", "w")
        for producto in self.productos:
                linea = self.convertir_producto_a_texto(producto)
                archivo.write(linea + "\n")

    def convertir_producto_a_texto(self, producto):
        return f"{producto.codigo},{producto.nombre},{producto.tipo_producto},{producto.cantidad_bodega},{producto.cantidad_minima},{producto.valor_unitario}"
        
class Factura():
    def __init__(self):
        self.num_factura = None
        self.factura = []
           
    def agregar_producto(self,producto,cantidad_venta):
        for ventas in self.factura:
            if ventas.nombre_producto == producto.nombre:#si el producto ya esta en la factura solo lo suma
                ventas.cantidad_vendida += cantidad_venta
                ventas.precio_total = (ventas.precio_unitario + (ventas.iva * ventas.precio_unitario)) * ventas.cantidad_vendida
                producto.cantidad_bodega -= cantidad_venta
                print("el producto se agrego correctamente")
                return None
                        
        self.factura.append(Venta(producto,cantidad_venta))
        
        producto.cantidad_bodega -= cantidad_venta
        
        print("el producto se agrego correctamente")

    def mostrar_factura(self):        
        if not self.factura:
            print("No hay ventas registradas")
            return
        
        print(f"{'Código':<8} {'Producto':<15} {'Cant':>5} {'P.Unit':>8} {'Total':>10}")
        
        total_general = 0
        
        for producto in self.factura:
            codigo = producto.codigo
            nombre = producto.nombre_producto
            cantidad = producto.cantidad_vendida
            precio = producto.precio_total
            total = cantidad * precio
            total_general += total
            
            print(f"{codigo:<8} {nombre:<15} {cantidad:>5} ${precio:>7.2f} ${total:>9.2f}")
        print("")
        print(f"{'TOTAL A PAGAR:':<38} ${total_general:>12.2f}")
    
    def mostrar_factura_detallada(self):
        if not self.factura:
            print("No hay ventas registradas")
            return        
        
        total_general = 0
        subtotal = 0
        total_iva = 0

        print(f"{'Código':<8} {'Producto':<15} {'Cant':>5} {'P.Unit':>8} {'Subtotal':>9} {'IVA%':>5} {'IVA$':>8} {'Total':>10}")
        
        for producto in self.factura:
            codigo = producto.codigo
            nombre = producto.nombre_producto
            cantidad = producto.cantidad_vendida
            precio_unitario = producto.precio_unitario  
            iva_porcentaje = producto.iva  
            precio_total = producto.precio_total  
            
            # Usar los valores directamente de la clase
            subtotal_producto = cantidad * precio_unitario
            iva_producto = cantidad * (precio_total - precio_unitario)  # Diferencia entre con IVA y sin IVA
            total_producto = cantidad * precio_total
            
            subtotal += subtotal_producto
            total_iva += iva_producto
            total_general += total_producto
            
            print(f"{codigo:<8} {nombre:<15} {cantidad:>5} ${precio_unitario:>7.2f} ${subtotal_producto:>8.2f} {iva_porcentaje:>5}% ${iva_producto:>7.2f} ${total_producto:>9.2f}")        

        print("")
        print(f"{'SUBTOTAL:':<48} ${subtotal:>10.2f}")
        print(f"{'IVA:':<48} ${total_iva:>10.2f}")
        print(f"{'TOTAL A PAGAR:':<48} ${total_general:>10.2f}")   
    
    def cancelar_venta_actual(self,tienda):
        if not self.factura:
            print("No hay venta en proceso")
            return False

        for producto_factura in self.factura:
            producto_tienda = tienda.comprobar_existencia_producto_por_codigo(producto_factura.codigo)
            if producto_tienda:
                producto_tienda.cantidad_bodega += producto_factura.cantidad_vendida
                print(f"Stock restaurado: {producto_tienda.nombre} (+{producto_factura.cantidad_vendida})")
        self.factura = []
        
class Venta():
    def __init__(self,producto,cantidad_venta):
        self.codigo = producto.codigo
        self.nombre_producto = producto.nombre
        self.cantidad_vendida = cantidad_venta
        self.precio_unitario = producto.valor_unitario
        self.iva = 0.15 # hay que cambiar
        self.precio_total = self.calcular_iva()
        self.total = self.cantidad_vendida * self.precio_total 
    
    def __str__(self):
        #return (f"{self.codigo}---{self.nombre_producto}---{self.cantidad_vendida}---${self.precio_unitario}---{self.iva*100}%---${self.precio_total}---${self.total}")
        return f"{self.codigo:<10} {self.nombre_producto:<20} {self.cantidad_vendida:<8} ${self.precio_unitario:<9.2f} {self.iva*100:<5.1f}% ${self.precio_total:<9.2f} ${self.total:<9.2f}"  
    def calcular_iva(self):
        return (self.precio_unitario +(self.iva * self.precio_unitario)) * self.cantidad_vendida
        
    


