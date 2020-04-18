import re

from src.parsing.AbstractLineParser import AbstractLineParser


class ConnectParser(AbstractLineParser):

    def __init__(self, line: str):
        self.line = line

    def get_user(self) -> str:
        search = re.search('DAP: User (.*) Addr ', self.line, re.IGNORECASE)
        return search.group(1)
        pass

    def get_ip_address(self)-> str:
        search = re.search('Addr (.*): Session Attribute', self.line, re.IGNORECASE)
        return search.group(1)
        pass

    def get_description(self)-> str:
        search = re.search('Session Attribute endpoint.anyconnect.devicetype = ""(.*)""', self.line, re.IGNORECASE)
        return search.group(1)
        pass

    def get_timestamp(self)-> str:
        search = re.search('&gt;(.*): %ASA', self.line, re.IGNORECASE)
        return search.group(1)
        pass

    def get_action(self)-> str:
        return 'c'
        pass

    @classmethod
    def get_filters(cls):
        return ['.anyconnect.devicetype']
        pass

