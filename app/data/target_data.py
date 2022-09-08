class ITargetData:
    hostname: str

    @property
    def json(self):
        return self.__dict__["hostname"]