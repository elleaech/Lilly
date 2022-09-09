from app.footprint import IData

class TestIData:
    def _before_each(self) -> None:
        self._interface_data = IData()
        self._assert_dict: dict = {}

    def test_simple_json(self) -> None:
        self._before_each()
        self._assert_dict = {"hostname": "google.com",
                        "ip_addr": "192.168.1.0",
                        "dns_server": "8.8.8.8"}
        self._interface_data.hostname = "google.com"
        self._interface_data.ip_addr = "192.168.1.0"
        self._interface_data.dns_server = "8.8.8.8"

        assert self._interface_data.json == self._assert_dict

    def test_json_with_arrays(self) -> None:
        self._before_each()
        self._assert_dict = {"hostname": "google.com",
                        "ip_addr": ["192.168.1.0", "192.168.1.1"],
                        "dns_server": "8.8.8.8"}
        self._interface_data.hostname = "google.com"
        self._interface_data.ip_addr = ["192.168.1.0", "192.168.1.1"]
        self._interface_data.dns_server = "8.8.8.8"

        assert self._interface_data.json == self._assert_dict

    def test_json_with_sets(self) -> None:
        self._before_each()
        self._assert_dict = {"hostname": "google.com",
                        "ip_addr": "192.168.1.0",
                        "dns_server": {"std": "8.8.8.8",
                                        "fake": "1.1.1.1"}}
        self._interface_data.hostname = "google.com"
        self._interface_data.ip_addr = "192.168.1.0"
        self._interface_data.dns_server = {"std": "8.8.8.8", "fake": "1.1.1.1"}

        assert self._interface_data.json == self._assert_dict

    def test_json_with_sets_and_arrays(self) -> None:
        self._before_each()
        self._assert_dict = {"hostname": "google.com",
                        "ip_addr": ["192.168.1.0", "192.168.1.1"],
                        "dns_server": {"std": "8.8.8.8",
                                        "fake": "1.1.1.1"}}
        self._interface_data.hostname = "google.com"
        self._interface_data.ip_addr = ["192.168.1.0", "192.168.1.1"]
        self._interface_data.dns_server = {"std": "8.8.8.8", "fake": "1.1.1.1"}

        assert self._interface_data.json == self._assert_dict