from calculator import Calculator as Calc


def main():
	print("Wpisz dane w formacie:\nliczba_1 spacja działanie(+,-,*,/) spacja liczba_2\n")
	while True:
		data = input()
		result = Calc.run(data)
		if result == '':
			print("Błąd w danych, spóbój ponownie...")
			continue
		print(result)
		break


if __name__ == '__main__':
	main()
