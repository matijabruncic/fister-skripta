import abc


class AbstractLineParser(metaclass=abc.ABCMeta):
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
