import re

from src.parsing.AbstractLineParser import AbstractLineParser


class DisconnectParser(AbstractLineParser):

    def __init__(self, line: str):
        self.line = line

    def get_user(self) -> str:
        search = re.search('Username = (.*) IP = ', self.line, re.IGNORECASE)
        return search.group(1)
        pass

    def get_ip_address(self)-> str:
        search = re.search('IP = (.*) Session disconnected', self.line, re.IGNORECASE)
        return search.group(1)
        pass

    def get_description(self)-> str:
        reason_search = re.search('Reason: (.*) </attr>', self.line, re.IGNORECASE)
        duration_search = re.search('Duration: (.*) Bytes xmt', self.line, re.IGNORECASE)
        description = reason_search.group(1) + " " + duration_search.group(1)
        return description.strip()
        pass

    def get_timestamp(self)-> str:
        search = re.search('&gt;(.*): %ASA', self.line, re.IGNORECASE)
        return search.group(1)
        pass

    def get_action(self)-> str:
        return 'd'
        pass

    @classmethod
    def get_filters(cls):
        return ['Session Type: SSL', 'Session Type: AnyC']
        pass
