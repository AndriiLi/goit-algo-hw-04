from colorama import Fore

from chatbot.command_parser import parse_input
from chatbot.command_handlers import add_contact, change_phone, show_phone, all_contacts, export_contacts, \
    import_contacts
from chatbot.exceptions import CantParseInputCommand, CommandAddContactNotFormatted, PhoneMustBeDigits, \
    ContactAlreadyExists, ContactNotFound, WrongPathToDbFile
from func.functions import print_colored


def run_chat_bot() -> None:
    contacts = {}
    print_colored(color=Fore.BLUE, message="Welcome to the assistant bot!")

    while True:

        user_input = input("Enter a command: ")
        try:
            command, *args = parse_input(user_input)
            match command:
                case "close" | "exit" | "q" | "quit":
                    print("Good bye!")
                    break
                case "hello" | "hi":
                    print("How can I help you?")
                case "add":
                    print(add_contact(args=args, contacts=contacts))
                case "change":
                    print(change_phone(args=args, contacts=contacts))
                case "phone":
                    print(show_phone(args=args, contacts=contacts))
                case "all":
                    print(all_contacts(contacts=contacts))
                case "save":
                    print(export_contacts(contacts=contacts))
                case "load":
                    print(import_contacts(contacts=contacts))
                case _:
                    print_colored(color=Fore.RED, message="Invalid command.")

        except CantParseInputCommand:
            print_colored(color=Fore.RED, message="Invalid command.")
        except CommandAddContactNotFormatted:
            print_colored(color=Fore.RED, message="Invalid command for add contact.")
        except PhoneMustBeDigits:
            print_colored(color=Fore.RED, message="Phone of contact must have digits")
        except ContactAlreadyExists:
            print_colored(color=Fore.RED, message="This contact already exist")
        except ContactNotFound:
            print_colored(color=Fore.RED, message="This contact not found")
        except WrongPathToDbFile:
            print_colored(color=Fore.RED, message="Wrong path to file")
