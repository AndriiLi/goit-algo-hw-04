from chatbot.exceptions import CantParseInputCommand


def parse_input(user_input: str) -> tuple[str, str]:
    user_input_value = user_input.split()
    len_user_input = len(user_input_value)

    if len_user_input < 1:
        raise CantParseInputCommand

    cmd, *args = user_input_value
    cmd = cmd.strip().lower()
    return cmd, *args
