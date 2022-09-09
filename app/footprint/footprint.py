from data import IHostData

class Footprint:
    def __init__(self, hostname: str) -> None:
        self._target = hostname
        self._host_data = IHostData()

    def host(self) -> IHostData:
        self._host_data.hostname = self._target
        self._host_data.ip_address = ["255", "255", "255", "255"]
        return self._host_data

    def services(self) -> IServicesData:
        pass

    def dns(self) -> IDNSData:
        pass

    def openPorts(self) -> IPortsData:
        pass

    def fingerprint(self) -> IOSData:
        pass
