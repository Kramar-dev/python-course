from calculator import Calculator as Calc


def main():
	print("Wpisz dane w formacie:\nliczba_1 spacja działanie [+ - * /] spacja liczba_2\n albo nic aby wyjść:")
	while True:
		data = input()
		if data == '':
			print('=(')
			exit()
		result = Calc.run(data)
		if result == '':
			print("Błąd w danych, spóbój ponownie...")
			continue
		elif result == ZeroDivisionError:
			print("Nie można dzielić przez zero!")
			continue
		print(f'Wynik: {result}\ndawaj jeszcze...')


if __name__ == '__main__':
	main()
