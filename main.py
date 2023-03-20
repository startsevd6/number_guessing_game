from random import randint


def generate_number():
	while True:
		user_input = input('''Введите 2 целых числа через пробел\t
		Первое для левой границы случайного числа\t
		Второе для правой границы случайного числа\n''')
		user_input = user_input.split()
		if len(user_input) != 2 or user_input[0].isdigit() == False or user_input[1].isdigit() == False:
			print("Неверный ввод. Попробуйте еще раз.")
			continue
		user_input[0] = int(user_input[0])
		user_input[1] = int(user_input[1])
		min1 = min(user_input[0], user_input[1])
		max1 = max(user_input[0], user_input[1])
		print(f'Добро пожаловать в числовую угадайку, вы загадали число от {min1} до {max1}.')
		return randint(min1, max1), min1, max1


def is_valid(guessed_number, min1, max1):
	return guessed_number.isnumeric() and min1 <= int(guessed_number) <= max1


def guess_number(min1, max1):
	attempt = 0
	while True:
		guessed_number = input()
		if not is_valid(guessed_number, min1, max1):
			print(f'А может быть все-таки введем целое число от {min1} до {max1}?')
			continue
		if int(guessed_number) < number:
			print('Ваше число меньше загаданного, попробуйте еще разок')
		elif int(guessed_number) > number:
			print('Ваше число больше загаданного, попробуйте еще разок')
		elif int(guessed_number) == number:
			print('Вы угадали, поздравляем!')
			print_attempt(attempt + 1)
			break
		attempt += 1


def print_attempt(attempt):
    attempt_str = str(attempt)
    if attempt_str[-2:] in ['11', '12', '13', '14']:
        attempt_str += ' попыток'
    elif attempt_str[-1] == '1':
        attempt_str += ' попытку'
    elif attempt_str[-1] in ['2', '3', '4']:
        attempt_str += ' попытки'
    else:
        attempt_str += ' попыток'
    print(f'Спасибо, что играли в числовую угадайку. Вы угадали число за {attempt_str}.')


def play_more():
	print('Будете ещё играть? (Введите да или нет):')
	while True:
		user_input = input().lower()
		if user_input.startswith('д'):
			return True
		elif user_input.startswith('н'):
			return False
		else:
			print('А может быть все-таки введем "да" или "нет"?')


game = True
while game == True:
	number, min1, max1 = generate_number()
	attempt = 0
	guess_number(min1, max1)
	game = play_more()
print('Еще увидимся...')
