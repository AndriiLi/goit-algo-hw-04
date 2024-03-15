class CantParseInputCommand(Exception):
    """" Program can't parse console command """


class PhoneMustBeDigits(Exception):
    """" Phone must have digits """


class ContactAlreadyExists(Exception):
    """" Contact already exists """


class CommandAddContactNotFormatted(Exception):
    """" Add contact command error format """


class ContactNotFound(Exception):
    """" Contact not found """


class WrongPathToDbFile(Exception):
    """" Wrong path to db file """
