from dataclasses import dataclass


@dataclass
class Message:
    pass


class Event(Message):
    pass


class Command(Message):
    pass
