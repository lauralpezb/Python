"""
Caja registradora con Pruebas unitarias:
1. El sistema debe poder escanear un producto (el cajero puede tipear el código del producto) 
    y agregarlo a la lista de productos comprados para ese cliente.
2. Además debe mostrar el subtotal. 
3. El cajero cuando lo desee puede finalizar la compra y el sistema deberá aplicar los descuentos correspondientes a los productos.
4. Luego, el cajero indica con cuánto paga el cliente y el sistema debe mostrar el cambio que debe devolver al cliente.
"""

import unittest

mercancia={}
subtotal = 0
total = 0
devuelta = 0

class ingreso_articulos():
    def productos(self, producto, precio, finalizar):
        mercancia[producto]=precio
        print("Tiene los siguiente articulos: ")

        for articulo in mercancia:
            print(articulo,":",mercancia[articulo])
        subtotal = sum(mercancia.values())
        print('El subtotal es de: ',subtotal)

        if finalizar.lower()=='f':
            total = (subtotal - (subtotal * 0.2))
        elif finalizar.lower()=='c':
            total = 0
        print('El total de la compra con descuento es: ',total)
        
        return mercancia, subtotal, total

    def pago(self,total,pago_cliente):
        devuelta = pago_cliente - total
        print('Debe darle al cliente: ', devuelta)
        return devuelta

class ingreso_articulosTest(unittest.TestCase):
    
    def setUp(self):
        self.mercancia = ingreso_articulos()
        self.devuelta = ingreso_articulos()

    def test_registro_articulos(self):
        mercancia = self.mercancia.productos('2312',1520,'c')
        self.assertEqual({'2312':1520},mercancia[0])
    
    def test_registro_tres_articulos(self):
        mercancia = self.mercancia.productos('202',2600,'c')
        mercancia = self.mercancia.productos('2412',1750,'c')
        self.assertEqual({'2312':1520,'202':2600,'2412':1750},mercancia[0])
        self.assertTrue(len(mercancia[0])==3)

    def test_subtotal(self):
        mercancia = self.mercancia.productos('212',200,'c')
        self.assertEqual(6070,mercancia[1])

    def test_total_continuar_compra(self):
        mercancia = self.mercancia.productos('982',240,'c')
        self.assertEqual(0,mercancia[2])

    def test_total_finalizar_compra_descuentos(self):
        mercancia = self.mercancia.productos('214',900,'f')
        self.assertEqual(5768,mercancia[2])
        devuelta = self.devuelta.pago(mercancia[2],10000)
        self.assertEqual(4232,devuelta)


if __name__ == "__main__":
    unittest.main()

