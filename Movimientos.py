class Movimientos:

    def __init__(self):
        self.movimientos = []

    def agregar_movimiento(self, movimiento):
        self.movimientos.append(movimiento)

    def mostrar_movimientos(self):
        if not self.movimientos:
            print("No hay movimientos")
        else:
            for movimiento in self.movimientos:
                print(movimiento)
