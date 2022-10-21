class Calculator:

    @staticmethod
    def add(number_1, number_2):
        return number_1 + number_2

    @staticmethod
    def subtract(number_1, number_2):
        return number_1 - number_2

    @staticmethod
    def multiply(number_1, number_2):
        return number_1 * number_2

    @staticmethod
    def divide(number_1, number_2):
        return number_1 / number_2

    @staticmethod
    def calculate(number_1, numder_2, operation):
        result = None

        if operation == 'D':
            result = my_calc.add(number_1, number_2)
        elif operation == 'O':
            result = my_calc.subtract(number_1, number_2)
        elif operation == 'M':
            result = my_calc.multiply(number_1, number_2)
        elif operation == 'Z':
            result = my_calc.divide(number_1, number_2)
        else:
            print('Podano nieobsługiwane działanie')

        if result:
            print(result)



my_calc = Calculator()

print('Jakie działanie chcesz wykonać?\n(D)dodawanie\n(O)dejmowanie\n(M)nożenie\nd(Z)ielenie')
action = input()
print('Podaj pierwszą liczbę')
number_1 = float(input())
print('Podaj drugą liczbę')
number_2 = float(input())

my_calc.calculate(number_1, number_2, action)
