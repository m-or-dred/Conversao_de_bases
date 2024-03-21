# inclui as funções de conversão e de verificação do input;
from conversores import baseA_para_base10, base10_para_baseB
from tratamento import verifica

# o input recebe as 3 variáveis, separadas por espaço (' '). Um espaço no início ou no final representa a base 10 como base de origem ou destino;
# se o usuário digitar uma letra maiúscula o método .lower() a transforma em minúscula;
print('\nDigite a base de origem, o valor e a base de destino, nessa ordem, separados por espaço. Se quiser, use espaço no início ou no final para a base 10.\n')
baseA, valor, baseB = input().lower().split(' ')

# se a base receber uma string vazia no input, ela é base 10;
if not baseA:
	baseA = '10'
if not baseB:
	baseB = '10'

# verifica o input;
if not verifica(baseA, valor, baseB):

	# chamada das funções de conversão
	baseA = int(baseA)
	baseB = int(baseB)
	# se a base de origem é 10;
	if baseA == 10:
		valorBase_B = base10_para_baseB(int(valor), baseB)
		print(f'\nbase de origem: \t10\nvalor na base 10:\t{valor}\nbase de destino:\t{baseB}\nvalor na base {baseB}:\t{valorBase_B}\n')

	# se a base de destino é 10;
	elif baseB == 10:
		valorBase10 = baseA_para_base10(valor, baseA)
		print(f'\nbase de origem: \t{baseA}\nvalor na base {baseA}:\t{valor}\nbase de destino:\t10\nvalor na base 10:\t{valorBase10:,}\n')
	# a cada 4 casas nos valores de base 10, será impressa uma vírgula (',') antes da quarta casa, para melhor vizualização do valor;

	# se a base 10 não é de origem nem de destino.
	else:
		valorBase10 = baseA_para_base10(valor, baseA)
		valorBase_B = base10_para_baseB(valorBase10, baseB)
		print(f'\nbase de origem: \t{baseA}\nvalor na base {baseA}:\t{valor}\nbase de destino:\t{baseB}\nvalor na base {baseB}:\t{valorBase_B}\nvalor na base 10:\t{valorBase10:,}\n')
