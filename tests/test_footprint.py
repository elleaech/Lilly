from app import Footprint

class TestFootprint:
    def _before_each(self) -> None:
        pass

    def _before_all(self) -> None:
        self._test = Footprint("google.com")

    def test_host(self) -> None:
        self._before_all()
        self._before_each()
        assert self._test.host().is_resilient()
