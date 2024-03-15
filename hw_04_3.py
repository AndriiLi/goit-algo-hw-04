import sys
from colorama import Fore
from func.functions import list_dir_recursive, print_colored


def main() -> None:
    try:
        str_to_folder = sys.argv[1]
        if len(str_to_folder.split()) == 0:
            raise IndexError

        print(list_dir_recursive(str_to_folder))

    except IndexError:
        print_colored('Шлях до існуючої папки в параметрах не передано', Fore.RED)
    except ValueError:
        print_colored('Шлях повинен бути до існуючої папки', Fore.RED)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
