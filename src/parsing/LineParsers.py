from src.parsing.impl.ConnectParser import ConnectParser
from src.parsing.impl.DisconnectParser import DisconnectParser
from src.parsing.impl.InvalidPasswordParser import InvalidPasswordParser


def line_contains_any(line: str, filters) -> bool:
    for filter in filters:
        if line.__contains__(filter):
            return True
    return False
    pass


def create_parser(line):
    if line_contains_any(line, InvalidPasswordParser.get_filters()):
        return InvalidPasswordParser(line)
    elif line_contains_any(line, ConnectParser.get_filters()):
        return ConnectParser(line)
    elif line_contains_any(line, DisconnectParser.get_filters()):
        return DisconnectParser(line)
    else:
        ValueError("Missing parser for line " + line)


def get_all_filters():
    filters = []
    filters.extend(InvalidPasswordParser.get_filters())
    filters.extend(ConnectParser.get_filters())
    filters.extend(DisconnectParser.get_filters())
    return filters
