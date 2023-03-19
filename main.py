from random import randint


def generate_number():
	return randint(1, 100)


def is_valid(guessed_number):
	if not guessed_number.isdigit():
		pass
	else:
		guessed_number = int(guessed_number)
		if 0 < guessed_number < 101 and guessed_number % 1 == 0:
			return True
	return False


def print_attempt(attempt):
	if attempt > 0:
		attempt1 = str(attempt)[-1]
		if attempt > 10:
			attempt2 = str(attempt)[-2]
		else:
			attempt2 = '0'
		if attempt2 == '1':
			print(f'Спасибо, что играли в числовую угадайку. Вы угадали число за {attempt} попыток.')
		elif attempt1 == '1':
			print(f'Спасибо, что играли в числовую угадайку. Вы угадали число за {attempt} попытку.')
		elif attempt1 == '2' or attempt1 == '3' or attempt1 == '4':
			print(f'Спасибо, что играли в числовую угадайку. Вы угадали число за {attempt} попытки.')
		else:
			print(f'Спасибо, что играли в числовую угадайку. Вы угадали число за {attempt} попыток.')
	print("Будете ещё играть? (Введите да или нет)")


def play_more():
	g = input()
	while g.lower() != 'да' or g.lower() != 'нет':
		if g.lower() == 'да':
			return 1
		if g.lower() == 'нет':
			return 0
		else:
			print('А может быть все-таки введем да или нет?')
			g = input()


number = generate_number()
attempt = 0
game = 1
print('Добро пожаловать в числовую угадайку')
while game == 1:
	while True:
		guessed_number = input()
		if not is_valid(guessed_number):
			print('А может быть все-таки введем целое число от 1 до 100?')
			break
		if int(guessed_number) < number:
			print('Ваше число меньше загаданного, попробуйте еще разок')
		elif int(guessed_number) > number:
			print('Ваше число больше загаданного, попробуйте еще разок')
		elif int(guessed_number) == number:
			print('Вы угадали, поздравляем!')
			attempt += 1
			break
		attempt += 1
	print_attempt(attempt)
	game = play_more()
	if game == 0:
		print('Еще увидимся...')
		break
	number = generate_number()
	attempt = 0
