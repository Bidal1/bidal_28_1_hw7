import random

while True:
        attempts = 0
        guess_list = []
        low = 0
        high = 100
        guess = random.randint(low, high)

        while True:
            print(f"Я думаю, что это число {guess}.")
            response = input("Введите 'да', 'больше' или 'меньше': ")
            if response == "да":
                attempts += 1
                guess_list.append(guess)
                with open("results.txt", "w") as f:
                    f.write(f"Количество попыток: {attempts}\n")
                    f.write(f"Список попыток: {guess_list}\n")
                    f.write(f"Загаданное число: {guess}\n")
                break
            elif response == "больше":
                attempts += 1
                guess_list.append(guess)
                low = guess + 1
                guess = random.randint(low, high)
            elif response == "меньше":
                attempts += 1
                guess_list.append(guess)
                high = guess - 1
                guess = random.randint(low, high)
            else:
                print("Пожалуйста, введите 'да', 'больше' или 'меньше'.")