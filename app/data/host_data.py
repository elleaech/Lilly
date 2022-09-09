from typing import List
from .data import IData

IIpAddress = List[str]

class IHostData(IData):
    hostname: str
    ip_address: IIpAddress

    def __init__(self) -> None:
        super().__init__()
