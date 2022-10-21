def main():
	data = []
	print(hex(id(data)))
	data.append(1)
	data.append(2)
	print(hex(id(data)))
	


if __name__ == '__main__':
	main()
