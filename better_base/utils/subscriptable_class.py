from abc import ABC


class Subscriptable(ABC):
    """
    Usage:
        Create a class inheriting from Subscriptable.
    """

    def __class_getitem__(cls, item):
        return cls._dict()[item]

    @classmethod
    def _dict(cls):
        return {k: v for k, v in cls.__dict__.items() if not k.startswith('_')}
