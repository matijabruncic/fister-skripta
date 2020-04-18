import datetime

from src.parsing.AbstractLineParser import AbstractLineParser


class Log:
    def __init__(self, line: int, parser: AbstractLineParser):
        self.line = line
        self.user = parser.get_user()
        self.ip_address = parser.get_ip_address()
        self.action = parser.get_action()
        self.timestamp = parser.get_timestamp()
        self.description = parser.get_description()

    def get_date(self):
        element = datetime.datetime.strptime(self.timestamp,"%b %d %Y %H:%M:%S")
        return element.__format__("%b %d")

    def get_hour(self):
        element = datetime.datetime.strptime(self.timestamp,"%b %d %Y %H:%M:%S")
        return element.__format__("%H:%M:%S")

    def get_description_without_spaces(self):
        return str(self.description).replace(" ", "-")
