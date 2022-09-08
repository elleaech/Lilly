from data import ITargetData
from tools import Lilly

class Footprint:
    def __init__(self) -> None:
        self._target = ITargetData()

    def host(self, name: str) -> ITargetData:
        self._target.hostname = name
        return self._target.json
