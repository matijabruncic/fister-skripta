import re

from src.parsing.AbstractLineParser import AbstractLineParser


class InvalidPasswordParser(AbstractLineParser):

    def __init__(self, line: str):
        self.line = line

    def get_user(self) -> str:
        search = re.search('user = (.*) : user IP =', self.line, re.IGNORECASE)
        return search.group(1)
        pass

    def get_ip_address(self)-> str:
        search = re.search('user IP = (.*) ', self.line, re.IGNORECASE)
        return search.group(1)
        pass

    def get_description(self)-> str:
        return 'Invalid password'
        pass

    def get_timestamp(self)-> str:
        search = re.search('&gt;(.*): %ASA', self.line, re.IGNORECASE)
        return search.group(1)
        pass

    def get_action(self)-> str:
        return 'b'
        pass

    @classmethod
    def get_filters(cls):
        return ['Invalid password']
        pass
