from typing import List
from .data import IData

IIpAddress = List[str]

class IHostData(IData):
    hostname: str
    ip_addresses: List[IIpAddress]

    def __init__(self) -> None:
        super().__init__()

    def is_resilient(self) -> bool:
        if ('hostname' in self.__dict__
            and 'ip_addresses' in self.__dict__):
            return True
        else:
            return False
