from ventas import Venta

class Tienda:
    def __init__(self):
        self.lista_ventas = []

    def buscar_venta(self,codigo):
        for i in range(len(self.lista_ventas)):
            if self.lista_ventas[i].codigo_venta == codigo:
                return i
        return -1
    
    def adicionar_venta(self, venta):
        if self.buscar_venta(venta.codigo_venta) == -1:
            self.lista_ventas.append(venta)
            return True
        return False