from colorama import Fore

from func.functions import total_salary, print_colored


def main() -> None:
    try:
        total = total_salary(path_to_file="./mock_data/company.txt")
        if total:
            total, average = total
            print("Загальна сума заробітної плати:", end='')
            print_colored(color=Fore.BLUE, message=f"${total:.2f}")
            print("Середня заробітна плата:", end='')
            print_colored(color=Fore.GREEN, message=f"${average:.2f}")

    except TypeError:
        print('Помилка данних у файлі')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
