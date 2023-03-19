from random import randint


def is_valid(guessed_number):
	if not guessed_number.isdigit():
		pass
	else:
		if 0 < int(guessed_number) < 100 and guessed_number % 1 == 0:
			return True
	return False


number = randint(1, 100)
attempt = 0
print('Добро пожаловать в числовую угадайку')
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

if attempt > 0:
	(f'Спасибо, что играли в числовую угадайку. Вы угадали число за {attempt} попыток. Еще увидимся...')
