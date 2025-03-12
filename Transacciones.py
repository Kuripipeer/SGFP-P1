class Transacciones:
    def __init__(self):
        pass

    def menu_transacciones(self):
        print("Transacciones")
        print("1. Depositar")
        print("2. Retirar")
        print("3. Salir")
        option = input("Opción: ")
        return option

    def depositar(self):
        print("Depositar")
        category = ""
        while not category:
            category = input("Categoria: ")
        concept = ""
        while not concept:
            concept = input("Concepto: ")
        amount = 0.0
        while amount <= 0.0:
            amount = float(input("Cantidad a depositar (debe ser mayor a 0.0): "))
        return concept, amount, category

    def retirar(self, balance, limit):
        print("Retirar")
        category = ""
        while not category:
            category = input("Categoria: ")
        concept = ""
        while not concept:
            concept = input("Concepto: ")
        amount = 0.0
        while amount <= 0.0:
            amount = float(input("Cantidad a retirar (debe ser mayor a 0.0): "))

        if amount > balance:
            print("No tienes suficientes fondos")
            concept = ""
            return concept, 0.0

        if amount > limit:
            print("Has excedido el límite de retiro mensual")
            concept = ""
            return concept, 0.0

        return concept, amount, category
