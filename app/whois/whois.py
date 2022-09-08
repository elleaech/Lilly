from data import ITargetData, _print_target_data

class WhoIs:
    def __init__(self) -> None:
        self._target = ITargetData()

    def host(self, name: str) -> ITargetData:
        self._target.hostname = name
        return _print_target_data(self._target)
