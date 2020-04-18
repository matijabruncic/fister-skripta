import abc
import re


class LineParser(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'get_user') and
                callable(subclass.get_user) and
                hasattr(subclass, 'get_ip_address') and
                callable(subclass.get_ip_address) and
                hasattr(subclass, 'get_description') and
                callable(subclass.get_description) and
                hasattr(subclass, 'get_timestamp') and
                callable(subclass.get_timestamp) and
                hasattr(subclass, 'get_action') and
                callable(subclass.get_action) or
                NotImplemented)

    @abc.abstractmethod
    def get_user(self):
        """Load in the data set"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_ip_address(self):
        """Load in the data set"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_description(self):
        """Load in the data set"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_timestamp(self):
        """Load in the data set"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_action(self):
        """Load in the data set"""
        raise NotImplementedError


class InvalidPasswordParser(LineParser):

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


class ConnectParser(LineParser):

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


class DisconnectParser(LineParser):

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


def create_parser(line):
    if line.__contains__('Invalid password'):
        return InvalidPasswordParser(line)
    elif line.__contains__('.anyconnect.devicetype'):
        return ConnectParser(line)
    elif line.__contains__('Session Type: SSL') or line.__contains__('Session Type: AnyC'):
        return DisconnectParser(line)
    else:
        ValueError("Missing parser for line " + line)
