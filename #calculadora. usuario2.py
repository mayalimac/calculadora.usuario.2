#calculadora2
def calculadora(num1, num2, op):
	if op== 1:
		resultado = num1 + num2
	elif op== 2:
		resultado = num1 - num2
	elif op== 3:
		resultado = num1 * num2
	elif op== 4:
		resultado = num1 / num2
	elif op== 0:
         op == 0
	
	return resultado

op = None
while (op != 0):

	op = int(input('Escolha a opção desejada:\n1: Soma\n2: Subtração\n3: Multiplicação\n4: Divisão\n0: Sair\n'))
	if op == 0:
		print('Saindo da calculadora')
		break
	elif op >= 5:
		print('\nEssa opção não existe!\n')
	else:
		num1 = float(input('Digite o primeiro número: '))
		num2 = float(input('\nDigite o segundo número: '))
		resultado = calculadora(num1, num2, op)
		print('O resultado da sua operação é : '+ str(resultado))
	
