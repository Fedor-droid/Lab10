import random
import logging

# Настройка логгера
logging.basicConfig(filename='game_log.log', level=logging.INFO)

# Функция для загадывания числа
def generate_number(N):
    logging.info(f"Загадано число от 1 до {N}")
    return random.randint(1, N)

# Функция для основной игры
def game():
    N = int(input("Введите максимальную границу числа: "))
    k = int(input("Введите количество попыток: "))
    secret_number = generate_number(N)
    logging.info(f"Загаданное число: {secret_number}")

    attempts = 0
    while attempts < k:
        user_guess = int(input("Введите вашу попытку: "))
        attempts += 1
        logging.info(f"Попытка {attempts}: {user_guess}")

        if user_guess < secret_number:
            logging.info(f"Попытка {attempts}: Загаданное число больше")
            print("Загаданное число больше")
        elif user_guess > secret_number:
            logging.info(f"Попытка {attempts}: Загаданное число меньше")
            print("Загаданное число меньше")
        else:
            logging.info(f"Попытка {attempts}: Вы угадали")
            print("Вы угадали")
            break

    if attempts == k:
        logging.info("Попытки закончились")
        print("Попытки закончились")

    logging.info("Игра завершена")

# Запуск игры
game()
input("Хорошего время препровождения")