account = "prueba"
password = "prueba"


def login():
    print("Bienvenido al banco de tus sueños")
    print("Por favor, introduce tu usuario y contraseña")
    user = input("Usuario: ").lower()
    password = input("Contraseña: ")
    if user == account and password == password:
        print("Has iniciado sesión correctamente")
        return True
    else:
        print("Usuario o contraseña incorrectos")
        return False


def main():
    if login():
        print("¡Bienvenido!")
    else:
        print("Vuelve a intentarlo")


if __name__ == "__main__":
    main()
