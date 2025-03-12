account = "prueba"
accountPassword = "prueba"


def login():
    print("Bienvenido al banco de tus sueños")
    print("Por favor, introduce tu usuario y contraseña")
    user = input("Usuario: ").lower()
    password = input("Contraseña: ")
    if user == account and password == accountPassword:
        print("Has iniciado sesión correctamente")
        return True
    else:
        print("Usuario o contraseña incorrectos")
        return False


def main():
    while not login():
        print("Vuelve a intentarlo")

    if login():
        print("¡Bienvenido!")
    else:
        print("Vuelve a intentarlo")


main()
