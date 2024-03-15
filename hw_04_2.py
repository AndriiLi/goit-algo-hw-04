from func.functions import get_cats_info


def main() -> None:
    cats_info = get_cats_info("./mock_data/cats_info.txt")
    for info in cats_info:
        print(info)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
