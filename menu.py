from os import system
from ventas import Venta
from tienda import Tienda
from fecha import Fecha

class Menu:
    def __init__(self):
        self.tienda = Tienda()
    
    def crear_venta(self):
        system("clear")
        print("Crear ventas")
        print("")

        codigo_venta = input("Ingrese el codigo de la venta: ")
        nombre_producto = input("Ingrese el nombre del producto: ")
        cantidad_producto = int(input("Ingrese la cantidad del producto: "))
        valor_unitario = int(input("Ingrese el valor unitario del producto: "))
        dia = int(input("Ingrese el dia de la venta: "))
        mes = int(input("Ingrese el mes de la venta: "))
        anio = int(input("Ingrese el año de la venta: "))
        nombre_vendedor = int(input("Ingrese el nombre del vendedor: "))
        
        fecha = Fecha(anio, mes, dia)
        venta = Venta(codigo_venta, nombre_producto, cantidad_producto, valor_unitario, fecha, nombre_vendedor)

        if self.tienda.adicionar_venta(venta):
            print("Venta registrada")
        else:
            print("Error: no se pudo registrar la venta")
        
        input("Presione ENTER para continuar")
        
    def mostar_ventas_productos(self):
        system("clear")
        print("Mostrar ventas por producto")
        print("")
        nombre_producto = input("Digite el nombre del producto: ")

        if self.tienda.buscar_ventas_producto(nombre_producto):

        def mostrar_menu(self):
            while True:
                system("clear")
                print("Bienvenido a la tienda")
                print("")
                print("1. Registrar ventas")
                print("2. Mostrar ventas por producto")
                print("0. Salir")
                print("")

                try:
                    op = int(input("Digite la opcion: "))

                    if op == 1:
                        self.crear_venta()
                    elif op == 2:
                        self.mostrar_ventas_productos()
                    elif op == 0:
                        break
                    else:
                        print("Opcion invalida")
                except ValueError:
                    print("Error: opción inválida")

    if __name__ == '__main__':
        menu = Menu()
        menu.mostrar_menu()