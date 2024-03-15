from pathlib import Path

from colorama import Fore

from chatbot.constants import DB_PATH
from chatbot.exceptions import PhoneMustBeDigits, ContactAlreadyExists, CommandAddContactNotFormatted, ContactNotFound, \
    WrongPathToDbFile, CommandUpdateContactNotFormatted
from func.functions import read_file, colored_string, print_colored


def add_contact(args: tuple[str, str], contacts: dict[str, str]) -> str:
    try:
        name = args[0].strip()
        phone = args[1].strip()

        if not phone.isdigit():
            raise PhoneMustBeDigits

        if name in contacts.keys():
            raise ContactAlreadyExists

        contacts[name] = phone
        return colored_string(message="Contact added.")

    except (TypeError, IndexError):
        raise CommandAddContactNotFormatted


def all_contacts(contacts: dict[str, str]) -> str:
    if not contacts:
        return colored_string(message="Contact list is empty.")

    sorted_contacts = sorted(contacts.items())
    return colored_string("\n".join([name + " - " + phone for name, phone in sorted_contacts]), color=Fore.MAGENTA)


def show_phone(args: tuple[str], contacts: dict[str, str]) -> str:
    try:
        name = args[0]
        return colored_string(message=f"{name} phone is: {contacts[name]}", color=Fore.MAGENTA)
    except IndexError:
        raise ContactNotFound


def change_phone(args: tuple[str, str], contacts: dict[str, str]) -> str:
    try:

        if len(args) < 2:
            raise CommandUpdateContactNotFormatted

        name = args[0]
        phone = args[1]

        if not phone.isdigit():
            raise PhoneMustBeDigits

        contacts[name] = phone
        return colored_string(message="Contact updated.")

    except IndexError:
        raise ContactNotFound


def export_contacts(contacts: dict[str, str]) -> str:
    try:
        with open(Path(DB_PATH).absolute(), 'w') as f:
            for contact, phone in contacts.items():
                f.write(f"{contact} {phone}\n")

        return colored_string(message="Contacts saved into file.")
    except FileNotFoundError:
        raise WrongPathToDbFile


def import_contacts(contacts: dict[str, str]) -> str:
    try:
        for row in read_file(Path(DB_PATH).absolute()):
            name, phone = row.split(' ')
            contacts[name.strip()] = phone.strip()

        return colored_string(message="Contacts loaded from file.")

    except FileNotFoundError:
        raise WrongPathToDbFile
