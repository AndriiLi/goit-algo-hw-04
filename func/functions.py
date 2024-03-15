from pathlib import Path
from typing import Callable
from colorama import Fore


def print_colored(message: str, color=Fore.BLUE) -> None:
    print(f"{color} {message} {Fore.RESET}")


def colored_string(message: str, color=Fore.YELLOW) -> str:
    return f"{color}{message}{Fore.RESET}"


def read_file(path: str | Path = '') -> list:
    try:
        with open(path, 'r', encoding='utf-8') as fh:
            return [row.strip() for row in fh.readlines() if len(row.strip()) > 0]

    except OSError as e:
        print("Файл не знайдено або він відсутній :" + str(e))
        return []


def convert_to_developer_salary(item: str) -> float | None:
    try:
        _, salary = item.split(',')
    except ValueError:
        return None

    return float(salary)


def convert_to_cats(item: str) -> dict | None:
    try:
        _id, name, age = item.split(',')
        return {
            'id': _id.strip(),
            'name': name.strip(),
            'age': int(age.strip())
        }
    except ValueError:
        return None


def get_data(raw_data: list, func: Callable[[str], dict | float]) -> list:
    return [func(row) for row in raw_data if func(row) is not None]


def total_salary(path_to_file: str | Path) -> tuple[float, float] | None:
    raw_data = read_file(path_to_file)
    developer_list = get_data(raw_data, convert_to_developer_salary)

    if developer_list is None or len(developer_list) == 0:
        return None

    developer_count = len(developer_list)

    total = sum([salary for salary in developer_list])

    try:
        average = total / developer_count
        return total, average
    except ZeroDivisionError:
        return None


def get_cats_info(path_to_file: str = '') -> list | None:
    path_to_file = str(Path(path_to_file))
    raw_data = read_file(path_to_file)

    if len(raw_data) == 0:
        return None

    return get_data(raw_data, convert_to_cats)


def list_dir_recursive(directory, indent=0) -> str:
    path = Path(directory)

    if not path.exists():
        raise ValueError

    content = ''
    for item in sorted(path.iterdir()):
        inner_path = path / item.name

        if inner_path.is_dir():
            content += f"{"-" * indent}{Fore.GREEN}[{item.name}]{Fore.RESET}\n"
            content += list_dir_recursive(inner_path, indent + 1)

        if inner_path.is_file():
            content += f"{"-" * indent}{Fore.BLUE}{item.name}{Fore.RESET}\n"

    return content
