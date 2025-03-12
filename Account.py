class Account:
    def __init__(self, name, password, balance, limitPerMonth, goal, value):
        self.__name = name
        self.__balance = balance
        self.__password = password
        self.__limitPerMonth = limitPerMonth
        self.__goal = goal
        self.__value = value
        self.__limit = limitPerMonth

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password

    def get_limitPerMonth(self):
        return self.__limitPerMonth

    def set_limitPerMonth(self, limitPerMonth):
        self.__limitPerMonth = limitPerMonth

    def get_goal(self):
        return self.__goal

    def set_goal(self, goal):
        self.__goal = goal

    def get_value(self):
        return self.__value

    def set_value(self, value):
        self.__value = value

    def get_limit(self):
        return self.__limit

    def set_limit(self, limit):
        self.__limit = limit

    def menu_goals(self):
        print("Metas")
        print("1. Modificar meta")
        print("2. Ver metas")
        print("3. Modificar límite de retiro mensual")
        print("4. Salir")
        option = input("Opción: ")
        return option

    def complete_goal(self):
        remaining = self.get_value() - self.get_balance()
        if remaining <= 0:
            print("Felicidades, has completado tu meta")
