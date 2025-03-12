# Importing libraries
import os
from Movimientos import Movimientos
from Transacciones import Transacciones
from Account import Account

# User account and password default
account = "prueba"
accountPassword = "prueba"
balance = 0.0
limitPerMonth = 1000.0

# Instances
movimientos = Movimientos()
transacciones = Transacciones()
cuenta = Account(account, accountPassword, balance, limitPerMonth, "Meta 1", 1000.0)


def login():
    clear_console()
    print("Bienvenido al banco de tus sueños")
    print("Por favor, introduce tu usuario y contraseña")
    user = input("Usuario: ").lower()
    password = input("Contraseña: ")
    if user == account and password == accountPassword:
        print("\nHas iniciado sesión correctamente")
        pause()
        return True
    else:
        print("\nUsuario o contraseña incorrectos")
        pause()
        return False


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    input("Presiona Enter para continuar...")


def main():
    while not login():
        print("Vuelve a intentarlo")

    while True:
        clear_console()
        print("Bienvenido al banco de tus sueños\n")
        print(f"Saldo: ${cuenta.get_balance()}")
        print("\n¿Qué operación deseas realizar?")
        print("1. Transacciones")
        print("2. Metas")
        print("3. Estado de cuenta")
        print("4. Salir")
        option = input("Opción: ")
        clear_console()
        match option:
            case "1":
                while True:
                    sub_option = transacciones.menu_transacciones()
                    clear_console()
                    match sub_option:
                        case "1":
                            concept, amount, category = transacciones.depositar()
                            cuenta.set_balance(cuenta.get_balance() + amount)
                            movimientos.agregar_movimiento(
                                f"Depósito - Categoria: {category} - Concepto: {concept} - Cantidad: +${amount}"
                            )
                            cuenta.complete_goal()
                            pause()
                            break
                        case "2":
                            concept, amount, category = transacciones.retirar(
                                cuenta.get_balance(), cuenta.get_limitPerMonth()
                            )
                            if not concept or amount == 0.0:
                                pause()
                                break

                            cuenta.set_balance(cuenta.get_balance() - amount)
                            cuenta.set_limitPerMonth(
                                cuenta.get_limitPerMonth() - amount
                            )
                            movimientos.agregar_movimiento(
                                f"Retiro - Categoria: {category} - Concepto: {concept} - Cantidad: -${amount}"
                            )
                            pause()
                            break
                        case "3":
                            print("Regresando al menú principal")
                            pause()
                            break
                        case _:
                            print("Opción no válida")
                            pause()
            case "2":
                while True:
                    sub_option = cuenta.menu_goals()
                    clear_console()
                    match sub_option:
                        case "1":
                            goal = input("Meta: ")
                            value = float(input("Cantidad: "))
                            cuenta.set_goal(goal)
                            cuenta.set_value(value)
                            print("Meta modificada")
                            cuenta.complete_goal()
                            movimientos.agregar_movimiento(
                                f"Meta modificada a {goal} - Cantidad: ${value}"
                            )
                            pause()
                            break
                        case "2":
                            remaining = cuenta.get_value() - cuenta.get_balance()
                            if remaining <= 0:
                                remaining = 0
                                percentage = 100
                                status = "completada"
                            else:
                                percentage = (
                                    cuenta.get_balance() / cuenta.get_value()
                                ) * 100
                                status = "pendiente"
                            print(
                                f"Meta: {cuenta.get_goal()} - Cantidad: ${cuenta.get_value()} - Restante: ${remaining} - Progreso: {percentage:.2f}% - Estado: {status}"
                            )
                            pause()
                            break
                        case "3":
                            print("Límite de retiro mensual")
                            new_limit = float(input("Nuevo límite de retiro mensual: "))
                            cuenta.set_limitPerMonth(new_limit)
                            cuenta.set_limit(new_limit)
                            print("Límite modificado")
                            movimientos.agregar_movimiento(
                                f"Límite de retiro mensual modificado a ${new_limit}"
                            )
                            pause()
                            break
                        case "4":
                            print("Regresando al menú principal")
                            pause()
                            break
                        case _:
                            print("Opción no válida")
                            pause()

            case "3":
                print("Estado de cuenta\n\n")
                print(
                    f"Saldo: ${cuenta.get_balance()}\t|\tLímite de retiro mensual disponible: ${cuenta.get_limitPerMonth()}\t|\tLímite de retiro mensual: ${cuenta.get_limit()}\n\n------------------------------------\n"
                )
                print("\tMovimientos\n")
                movimientos.mostrar_movimientos()

                print("\n------------------------------------\n")

                pause()
            case "4":
                print("Salir")
                break
            case _:
                print("Opción no válida")
                pause()


main()
