def verifica(baseA, valor, baseB):
# casos que impedem uma conversão indesejada;

	# valor com caractere que não é letra, número ou '|';
	if not valor.isalnum() and max(valor) != '|':
		print("\nValor inválido. Use somente letras e/ou números ou '|'.\n")
		exit()

	# base de origem e/ou destino não é um número;
	elif not str(baseA).isdigit() or not str(baseB).isdigit():
		print("\nAs bases devem ser um número entre 1 e 36.\n")
		exit()

	# as bases são números;
	baseA = int(baseA); baseB = int(baseB)

	# base de origem fora do range;
	if baseA not in range(1,37):
		print("\nBase de origem inválida. Escolha uma base de origem entre 1 e 36.\n")
		exit()

	# base de destino fora do range ou igual à base de origem;
	elif baseB not in range(1,37) or baseB == baseA:
		print('\nBase de destino inválida. Escolha outra base de destino entre 1 e 36.\n')
		exit()

	# valor possui símbolo fora da base de origem;
	elif max(valor).isdigit() and int(max(valor)) >= baseA or max(valor).isalpha() and ord(max(valor)) - 86 > baseA or max(valor) == '|' and baseA != 1:
		if baseA in range(2,11):
			print(f"\nO caractere '{max(valor)}' é inválido. O maior símbolo da base {baseA} é '{baseA - 1}'.\n")
		elif baseA > 11:
			print(f"\nO caractere '{max(valor)}' é inválido. O maior símbolo da base {baseA} é '{chr(baseA + 86)}'.\n")
		else:
			print(f"\nO caractere '{max(valor)}' é inválido. O único símbolo da base 1 é '|'.\n")
		exit()
# fim dos casos;

	# passou em todos os testes.
	else:
		return 0
