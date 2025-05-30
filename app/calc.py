import app
import math
from app.util import validate_permissions


class InvalidPermissions(Exception):
    pass

class Calculator:
    def add(self, x, y):
        self.check_types(x, y)
        return x + y

    def substract(self, x, y):
        self.check_types(x, y)
        return x - y

    def multiply(self, x, y):
        if not app.util.validate_permissions(f"{x} * {y}", "user1"):
            raise InvalidPermissions('User has no permissions')

        self.check_types(x, y)
        return x * y

    def divide(self, x, y):
        self.check_types(x, y)
        if y == 0:
            raise TypeError("Division by zero is not possible")

        return x / y

    def power(self, x, y):
        self.check_types(x, y)
        return x ** y
    # Se agrega las funcionalidades (raiz cuadrada, log)

    def sqrt(self, x):
        if not isinstance(x, (int, float)):
            raise TypeError("Parameter must be a number")
        if x < 0:
            raise ValueError("Cannot calculate square root of a negative number")
        return math.sqrt(x)

    def log10(self, x):
        if not isinstance(x, (int, float)):
            raise TypeError("Parameter must be a number")
        if x <= 0:
            raise ValueError("Logarithm undefined for non-positive values")
        return math.log10(x)

    def check_types(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Parameters must be numbers")

    # Se agreag un metodo estatico para determinar si n es par
    @staticmethod
    def is_even(n):
        if not isinstance(n, int):
            raise TypeError("Parameter must be an integer")
        return n % 2 == 0

if __name__ == "__main__":  # pragma: no cover
    calc = Calculator()
    print(f"La suma de 5+2 es: {calc.add(5,2)}")
    print(f"La resta de 3-2 es: {calc.substract(3,2)}")
    print(f"La multiplicacion de 10*2 es: {calc.multiply(10,2)}")
    print(f"La division de 10/2 es: {calc.divide(10,2)}")
    print(f"La potencia de 5 elevado a 3 es: {calc.power(5,3)}")
    print(f"La raiz cuadrada de 16 es: {calc.sqrt(16)}")
    print(f"El logaritmo de base 10 de 1000 es: {calc.log10(1000)}")
    print(f"El numero ingresado 10 es par: {calc.is_even(10)}")
