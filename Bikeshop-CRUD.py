# a)	Crear la clase Bicicleteria. listo
# b)	Declarar los atributos bicicletas, ganancias y cantidad_de_ventas. listo
# c)	Implementar el método vender_bicicleta() de la clase Bicicleteria.
# d)	Implementar el método comprar_bicicleta().
# e)	Crear la clase Bicicleta.
# f)	Declarar los atributos de la clase Bicicleta: nro_de_serie, modelo, año y precio.
# g)	Implementar el método get_precio().
# h)	Implementar el método set_precio().
# i)	Implementar el método get_nro_de_serie().
# j)	Se deberán crear al menos cuatro bicicletas y una bicicleteria. Deben usarse todos los métodos al menos una vez.


# ----------------------------EJERCICIO 2-----------------------------------------------------------------------------------

class Bicicleteria():
    pass

    def __init__(self, nombre, ganancias, cant_ventas):
        self.ganancias = ganancias
        self.bicicletas = []
        self.nombre = nombre
        self.cantidad_de_ventas = cant_ventas

    def __str__(self):
        print(f'Nombre: {self.nombre}\nGanancias: {self.ganancias}\nCant de ventas: {self.cantidad_de_ventas}')
        print(f'-------Stock de {self.nombre}---------\n')

        self.list_bici()

    def comprar_bicicleta(self, bici):
        self.bicicletas.append(bici)
        print('Bicicleta agregada al inventario')

    def vender_bici(self, bici):
        self.bicicletas.remove(bici)
        print('Bicicleta eliminada del inventario')

    def list_bici(self):
        if len(self.bicicletas) == 0:
            print('No tiene bicicletas en stock')
        else:
            for bici in self.bicicletas:
                bici.__str__()
                print('----------------------------')

    def get_bici(self, nro_s):
        for bici in self.bicicletas:
            if bici.nro_serie == nro_s:
                print('Bicicleta encontrada!')
                return bici


class Bicicleta():
    pass

    def __init__(self, modelo, nro_serie, anio, precio):
        self.modelo = modelo
        self.nro_serie = nro_serie
        self.anio = anio
        self.precio = precio

    def __str__(self):
        print(
            f'Modelo: {self.modelo}\nnumero de serie: {self.nro_serie}\nAño de fabricacion: {self.anio}\nPrecio:{self.precio}')

    def set_precio(self):
        print('----------------PRECIO BICICLETA--------------')
        precio = float(input('Ingrese el nuevo precio de la bicicleta: '))
        self.precio = precio
        print('Precio actualizado')

    def get_precio(self):
        print('--------------BUSCANDO PRECIO--------------')
        return self.precio

    def get_nro_serie(self):
        return self.nro_serie;


def crear_bici():
    nro_serie = input('Ingrese el numero de serie: ')
    modelo = input('Ingrese el modelo: ')
    anio = int(input('Año: '))
    precio = float(input('Ingrese el precio: '))
    return Bicicleta(modelo, nro_serie, anio, precio)


def crear_bicicleteria():
    nombre = input('Ingrese el nombre de la bicicleteria: ')
    ganancias = input('Ingrese sus ganacias actuales: ')
    ganancias = float(ganancias)
    cant_v = int(input('Ingrese su cant de ventas actuales: '))
    bicicleteria = Bicicleteria(nombre, ganancias, cant_v)
    return bicicleteria


def main():
    print('----------------BIENVENIDO-----------------')
    print('Primeramente cargue los datos que refieren a su Local\n')
    shop = crear_bicicleteria();

    print('------------Bicicleteria creada--------------')

    opc = 0
    while opc != 7:
        print('\n\n\n---------------------MENU--------------------')
        print('Eliga una opcion:'
              '\n1-Comprar Bicicleta'
              '\n2-Vender Bicicleta'
              '\n3-Ver stock de bicicletas'
              '\n4-Ver precio de bicicleta'
              '\n5-Modificar precio de Bicicleta'
              '\n6-Datos del local'
              '\n7-Salir')
        opc = int(input('Ingrese su opc: '))
        if opc == 1:
            print('---------Agregando Bicicleta a stock-------')
            bici = crear_bici()
            shop.comprar_bicicleta(bici)

        elif opc == 2:
            print('-------------------Vender Bicicleta-------------')
            nro_serie = input('Ingrese el numero de serie a buscar:')
            bici = shop.get_bici(nro_serie)
            if bici is None:
                print('Error al vender la Bici')
            else:
                shop.vender_bici(bici)
                shop.cantidad_de_ventas = shop.cantidad_de_ventas + 1
                shop.ganancias = shop.ganancias + bici.precio
                print(f'ganancias actualizadas: {shop.ganancias}')

        elif opc == 3:
            print(f'-------Bicicletas en Stock en {shop.nombre}-------')
            shop.list_bici()

        elif opc == 4:
            print('---------------Buscar Precio-------------')
            nro_serie = input('Ingrese el numero de serie a buscar:')
            bici = shop.get_bici(nro_serie)
            if bici is None:
                print('Error al buscar la bicicleta')
            else:
                print(f'modelo: {bici.modelo}---precio: {bici.precio}')

        elif opc == 5:
            print('-------------Modificar Precio--------------')
            nro_serie = input('Ingrese el numero de serie a buscar:')
            bici = shop.get_bici(nro_serie)
            if bici is None:
                print('Error al modificar precio de la Bici')
            else:
                precio = input('Ingrese el precio actualizado: ')
                bici.precio = float(precio)
                print('-----------Precio Actualizado---------')

        elif opc == 6:
            print('\n-----Datos de la tienda-----------')
            shop.__str__()
        elif opc == 7:
            print(f'Adios {shop.nombre}!')


main()

