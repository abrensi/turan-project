def calculator():
    while True:
        try:
            # Ввод чисел
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))

            print("\nВыберите операцию:")
            print("1 - Сложение")
            print("2 - Вычитание")
            print("3 - Умножение")
            print("4 - Деление")
            print("5 - Выход")

            choice = input("Выбор операции: ")

            if choice == "1":
                print(f"Результат: {num1 + num2}")
            elif choice == "2":
                print(f"Результат: {num1 - num2}")
            elif choice == "3":
                print(f"Результат: {num1 * num2}")
            elif choice == "4":
                if num2 == 0:
                    print("Ошибка: деление на ноль невозможно!")
                else:
                    print(f"Результат: {num1 / num2}")
            elif choice == "5":
                print("Выход из программы...")
                break
            else:
                print("Ошибка: некорректный выбор операции!")

        except ValueError:
            print("Ошибка: введите корректное число!")

        print("\n---\n")


if __name__ == "__main__":
    calculator()
