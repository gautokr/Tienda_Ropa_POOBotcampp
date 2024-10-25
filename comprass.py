class Producto:
    def __init__(self, nombre, precio, cantidad):
        self._nombre = nombre.lower()
        self._precio = precio
        self._cantidad = cantidad

    def nombre(self):
        return self._nombre

    def precio(self):
        return self._precio

    def cantidad(self):
        return self._cantidad

    def mostrar_info(self):
        print(f'Nombre: {self._nombre.capitalize()}, Precio: ${self._precio:.2f}, Stock: {self._cantidad}')

    def comprar(self, cantidad):
        if cantidad <= self._cantidad:
            self._cantidad -= cantidad
            return self._precio * cantidad
        else:
            print(f'No hay suficiente stock de {self._nombre.capitalize()}')
            return 0

class Ropa(Producto):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self._talla = talla

    def talla(self):
        return self._talla

    def mostrar_info(self):
        super().mostrar_info()
        print(f'Talla: {self._talla}')

class Camisa(Ropa):
    def __init__(self, nombre, precio, cantidad, talla, tipo_tela):
        super().__init__(nombre, precio, cantidad, talla)
        self._tipo_tela = tipo_tela

    def mostrar_info(self):
        super().mostrar_info()
        print(f'Tipo de tela: {self._tipo_tela}')

class Pantalon(Ropa):
    def __init__(self, nombre, precio, cantidad, talla, tipo_tela):
        super().__init__(nombre, precio, cantidad, talla)
        self._tipo_tela = tipo_tela

    def mostrar_info(self):
        super().mostrar_info()
        print(f'Tipo de tela: {self._tipo_tela}')

class Zapato(Ropa):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad, talla)

class Tienda:
    def __init__(self):
        self.prendas = []

    def agregar_prenda(self, prenda):
        self.prendas.append(prenda)

    def mostrar_inventario(self):
        for prenda in self.prendas:
            prenda.mostrar_info()

class Carrito:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto, cantidad):
        if producto.cantidad() >= cantidad:
            self.productos.append((producto, cantidad))
            producto.comprar(cantidad)
        else:
            print(f'No hay suficiente stock de {producto.nombre()}')

    def calcular_total(self):
        return sum(producto.precio() * cantidad for producto, cantidad in self.productos)

    def mostrar_carrito(self):
            if not self.productos:
                print("El carrito está vacío.")
                return
            
            print("Contenido del carrito:")
            for producto, cantidad in self.productos:
                print(f'{producto.nombre().capitalize()} - Cantidad: {cantidad}')

    def mostrar_resumen(self):
        self.mostrar_carrito()
        print(f'Total a pagar: ${self.calcular_total():.2f}')

camisa = Camisa("Camisa de Seda", 25.00, 50, "M", "Seda")
pantalon = Pantalon("Pantalón de Lino", 30.00, 30, "M", "Lino")
zapatos = Zapato("Zapatos de Cuero", 60.00, 25, 40)

inventario = Tienda()
inventario.agregar_prenda(camisa)
inventario.agregar_prenda(pantalon)
inventario.agregar_prenda(zapatos)

print('¡Bienvenido! Este es nuestro inventario.')
inventario.mostrar_inventario()

carrito = Carrito()

while True:
    nombre = input('¿Qué prendas desea adquirir? Escriba "salir" si ya no quiere adquirir prendas o "carrito" para ver el carrito: ')
    if nombre.lower() == "salir":
        break
    if nombre.lower() == "carrito":
        carrito.mostrar_resumen()
        continue
    try:
        cantidad = int(input('Ingrese la cantidad: '))
        for prenda in inventario.prendas:
            if prenda.nombre() == nombre.lower():
                carrito.agregar_producto(prenda, cantidad)
                break
        else:
            print('La prenda no existe.')
    except ValueError:
        print('Ingrese un número válido.')

carrito.mostrar_resumen()
